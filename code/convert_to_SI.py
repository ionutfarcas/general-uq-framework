#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import f90nml
import numpy as np
import glob
import os
import csv
import sys
import matplotlib.pyplot as plt

prob_no  = -1 
if len(sys.argv) != 2:
    print('Usage: ' + sys.argv[0] + ' prob_no')
    
    exit(0)
else:
    prob_no = int(sys.argv[1])

folder='/home/ionut/work/postdoc/external_mount/frontera_scratch/DIIID_Nature_CS/nonlin/out_prob_' + str(prob_no) + '/'
# folder='/home/ionut/work/postdoc/external_mount/frontera_scratch/DIIID_Nature_CS/nonlin/test_samples/test_sample_0/'

print('computations for simulation ' + str(prob_no))

t_s=0.5

# find runs
ext=[]
for file in glob.glob(folder+'/nrg*'):
    head, tail = os.path.split(file)
    ext.append(tail.split('nrg')[-1])

print(ext)

# import last geometry found
par=f90nml.read(folder+'parameters'+ext[-1])
with open(folder+"{}{}".format(par['geometry']['magn_geometry'], ext[-1]), "r") as geomfile:
    geom = np.empty((16, int(par['box']['nz0'])), dtype=np.float64)
    k = 0
    for line in geomfile:
        if len(line.split()) == 16:
            geom[:, k] = line.split()[:]
            k += 1
        elif line.startswith('Cy'):
            Cy = float(line.split()[-1])
        elif line.startswith('Cxy'):
            Cxy = float(line.split()[-1])
        elif line.startswith('q0'):
            q = float(line.split()[-1])
            
jac=geom[10]
gxx=geom[0]    
npol=1
S=(2*np.pi)**2*np.abs(Cy)*npol*np.sum(np.sqrt(gxx)*jac, axis=-1)/par['box']['nz0']
dVdx=(2*np.pi)**2*np.abs(Cy)*npol*np.sum(jac, axis=-1)/par['box']['nz0']

S*=par['units']['Lref']**2
dVdx*=par['units']['Lref']**2

qe=1.602e-19;
mp=1.6726219e-27;
cref=np.sqrt(par['units']['Tref']*1e3*qe/(par['units']['mref']*mp))
Oref=qe*par['units']['Bref']/(par['units']['mref']*mp)
rhoref=cref/Oref;
rho_starref=rhoref/par['units']['Lref']
QGB=cref*par['units']['nref']*1e19*par['units']['Tref']*1e3*qe*(rho_starref)**2/1e6
            
print('area: {} [m**2]'.format(S))
print('dVdx: {} [m**2]'.format(dVdx))
print('QGB: {} [MW]'.format(QGB))

# import data
data = []
time = [] 
for i_ext in ext:
    fname = os.path.join(folder, 'nrg' + i_ext)
    with open(fname) as nrgfile:
        csvnrg = csv.reader(nrgfile, delimiter=' ', skipinitialspace=True)
        for line in csvnrg:
            if len(line) == 0:
                continue
            if len(line) == 1:
                time.append(float(line[0]))
                data.append([[] for _ in range(par['box']['n_spec'])])
                ispec = 0
            elif len(line) == par['info']['nrgcols']:
                data[-1][ispec] = line
                ispec += 1
            else:
                raise IOError("Incorrect number of columns")
data=np.asarray(data,dtype=float)
tm=np.asarray(time,dtype=float)
inds=np.argsort(tm)
tm=tm[inds]
data=data[inds,:,:]

i_s=(np.abs(tm-t_s)).argmin()
Q=(data[:,0,6]+data[:,0,7])*dVdx*QGB


Qavg=np.trapz(Q[i_s:],tm[i_s:])/(tm[-1]-tm[i_s])
print('average electron heat flow: {} [MW]'.format(Qavg))
print('average electron heat flow: {} [QGB]'.format(Qavg/dVdx/QGB))

figure = plt.figure(figsize=(5, 5), dpi=100)
ax = figure.add_subplot(1,1,1)
ax.plot(tm,Q,'-b')
ax.plot(tm[i_s:],Qavg*np.ones_like(tm[i_s:]),'--r')
ax.set_xlabel(r'$t [c_s/a]$');ax.set_title (r'$Q_e \cdot S [MW]$')

plt.show()