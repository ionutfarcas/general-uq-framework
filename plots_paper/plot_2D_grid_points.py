import numpy as np
from matplotlib.pyplot import *

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



# left and right bounds
left_stoch_boundary 	= np.array([left_Tref, left_nref, left_omt, left_omn, \
						   left_tau, left_zeff, left_q0, left_shat])

right_stoch_boundary 	= np.array([right_Tref, right_nref, right_omt, right_omn, \
						   right_tau, right_zeff, right_q0, right_shat])

left_stoch_boundary_flipped 	= np.flip(left_stoch_boundary)
right_stoch_boundary_flipped 	= np.flip(right_stoch_boundary)


print(left_stoch_boundary)
print(right_stoch_boundary)



left_bounds 	= np.array([0.97*left_Tref, 0.98*left_nref, 0.96*left_omt, 0.97*left_omn, \
								0.97*left_tau, 0.96*left_zeff, 0.955*left_q0, 0.97*left_shat])

right_bounds 	= np.array([1.015*right_Tref, 1.01*right_nref, 1.02*right_omt, 1.01*right_omn, \
								1.025*right_tau, 1.02*right_zeff, 1.03*right_q0, 1.02*right_shat])

left_bounds_flipped 	= np.flip(left_bounds)
right_bounds_flipped 	= np.flip(right_bounds)



x_ticks = [[0.35, 0.44], [4.00, 4.95], [145, 225], [70, 105], [1.15, 1.75], [1.55, 2.4], [3.55, 5.5], [4, 6]]
y_ticks = x_ticks[::-1]

x_ticks_labels = [[0.35, 0.44], ['4.00', 4.95], [145, 225], [70, 105], [1.15, 1.75], [1.55, '2.40'], [3.55, '5.50'], [4, 6]]
y_ticks_labels = x_ticks_labels[::-1]



indices_ascend 	= [6, 7, 5, 4, 0, 1, 2, 3]
indices_descend = [3, 2, 1, 0, 4, 5, 7, 6]

if __name__ == '__main__':

	dim 		= 8
	no_sg_sims 	= 57
	

	map_rv = lambda left, right, x: left + (right - left)*x

	params = [r'$T_{e}[\mathrm{keV}]$', r'$n_{e}[10^{19} \mathrm{m^{-3}}]$', r'$\omega_{T_e}$', r'$\omega_{n_e}$', r'$\tau$', r'$Z_{\rm eff}$', r'$q$', r'$\hat{s}$']

	all_sg_points = np.load('results/all_sg_points.npy')
	all_sg_points = all_sg_points[:57, :]

	sg_points_ascend 	= all_sg_points[:, indices_ascend]
	sg_points_descend 	= all_sg_points[:, indices_descend]

	rc("figure", dpi=400)           # High-quality figure ("dots-per-inch")
	rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica"})
	rc("legend", edgecolor='none')  # No boxes around legends
	rcParams["figure.figsize"] = (8, 7)
	rcParams.update({'font.size': 8})

	bboard 			= "#323E48" # blackboard slate gray
	chalk_white 	= "#DCDCDC"
	chalk_orange 	= "#fc9d28"
	transp 			= (1,1,1,0)

	# white base settings
	rc("figure",facecolor='w')
	rc("axes",facecolor='w',edgecolor='k',labelcolor='k')
	rc("savefig",facecolor='w')
	rc("text",color='k')
	rc("xtick",color='k')
	rc("ytick",color='k')

	fig = figure()

	axs = []

	for i in range(dim - 2, -1, -1):

		temp = []
		for j in range(i + 1):
			
			ax = subplot2grid((7, 7), (i, j))

			ax.spines['right'].set_visible(False)
			ax.spines['top'].set_visible(False)

			ax.minorticks_on()

			ax.grid(which='major', linestyle='None', linewidth='0.5', color='k')
			ax.grid(which='minor', linestyle='--', linewidth='0.4', color='k')

			# ax.tick_params(which='both', # Options for both major and minor ticks
			#                 top='off', # turn off top ticks
			#                 left='off', # turn off left ticks
			#                 right='off',  # turn off right ticks
			#                 bottom='off') # turn off bottom ticks

			temp.append(ax)

		axs.append(temp)



	for i in range(dim - 2, -1, -1):
	
		axs[0][i].set_xlabel(params[i])
		axs[i][0].set_ylabel(params[::-1][i])


	for i in range(len(axs)):
		for j in range(len(axs[i])):

			points_x = map_rv(left_stoch_boundary[j], right_stoch_boundary[j], sg_points_ascend[:, j])
			points_y = map_rv(left_stoch_boundary_flipped[i], right_stoch_boundary_flipped[i], sg_points_descend[:, i])


			axs[i][j].set_xticks(x_ticks[j])
			axs[i][j].set_xticklabels(x_ticks_labels[j])

			axs[i][j].set_yticks(y_ticks[i])
			axs[i][j].set_yticklabels(y_ticks_labels[i])


			axs[i][j].set_xlim(left_bounds[j], right_bounds[j])
			axs[i][j].set_ylim(left_bounds_flipped[i], right_bounds_flipped[i])

			axs[i][j].plot(points_x, points_y, 'o', color='k', ms=2)

	
	tight_layout()

	# show()

	savefig('figures/grid_points_proj_2D.png', pad_inches=3)
	close()
