import numpy as np
from shutil import copy
import os

# q0
left_tau 		= 1.44 - 0.2*1.44 
right_tau 		= 1.44 + 0.2*1.44 

# shat
left_zeff 		= 1.99 - 0.2*1.99
right_zeff 		= 1.99 + 0.2*1.99

### IONS ###
left_q0  	= 4.536233280368855 - 0.2*4.536233280368855
right_q0  	= 4.536233280368855 + 0.2*4.536233280368855

# omt ions
left_shat  	= 5.021235280458611 - 0.2*5.021235280458611
right_shat  = 5.021235280458611 + 0.2*5.021235280458611

# dens ions
left_omn  	= 88 - 0.2*88
right_omn  	= 88 + 0.2*88

### fastD ###
# omt fastD
left_omt 	= 186 - 0.2*186 
right_omt 	= 186 + 0.2*186

# dens fastD
left_Tref   	= 3.9703890681266785E-01 - 0.1*3.9703890681266785E-01
right_Tref   	= 3.9703890681266785E-01 + 0.1*3.9703890681266785E-01

# omn fastD
left_nref 	= 4.4923791885375977E+00 - 0.1*4.4923791885375977E+00
right_nref 	= 4.4923791885375977E+00 + 0.1*4.4923791885375977E+00


if __name__ == '__main__':

	dim 	= 8
	no_rv 	= 32

	seed = 981287

	np.random.seed(seed)

	std_rand_vars 	= np.random.uniform(0, 1, size=(no_rv, dim))
	map_rv 			= lambda left, right, x: left + (right - left)*x

	rand_tau 		= map_rv(left_tau, right_tau, std_rand_vars[:, 0])
	rand_zeff 		= map_rv(left_zeff, right_zeff, std_rand_vars[:, 1])
	
	rand_q0 		= map_rv(left_q0, right_q0, std_rand_vars[:, 2])
	rand_shat 		= map_rv(left_shat, right_shat, std_rand_vars[:, 3])
	
	rand_omn 		= map_rv(left_omn, right_omn, std_rand_vars[:, 4])
	rand_omt 		= map_rv(left_omt, right_omt, std_rand_vars[:, 5])
	
	rand_Tref 	= map_rv(left_Tref, right_Tref, std_rand_vars[:, 6])
	rand_nref 	= map_rv(left_nref, right_nref, std_rand_vars[:, 7])
	
	dir_name 		= lambda n: 'DIIID_test_sample_' + str(n)
	param_file 		= lambda n: 'DIIID_test_sample_' + str(n) + '/parameters'
	gene_exec_file 	= lambda n: 'DIIID_test_sample_' + str(n) + '/gene_frontera'


	out_dir = lambda n: '/scratch1/02910/ionut/DIIID_UQ/nonlin/sim_' + str(n)

	for i in range(no_rv):

		if not os.path.isdir(dir_name(i)):
			os.mkdir(dir_name(i))

		if not os.path.isfile(param_file(i)):
			copy('parameters', dir_name(i))

		if not os.path.isfile(gene_exec_file(i)):
			copy('gene_frontera', dir_name(i))


		modify_param_command = './modify_params_8D ' + param_file(i) + ' ' + out_dir(i) + ' ' + str(rand_tau[i]) + ' ' + str(rand_zeff[i]) + ' ' +  str(rand_q0[i]) + ' ' + str(rand_shat[i]) + ' ' + str(rand_omn[i]) + ' ' + str(rand_omt[i]) + ' ' + str(rand_Tref[i]) + ' ' + str(rand_nref[i])

		os.system(modify_param_command)
		
		print(rand_tau[i], rand_zeff[i], rand_q0[i], rand_shat[i], rand_omn[i], rand_omt[i], rand_Tref[i], rand_nref[i])