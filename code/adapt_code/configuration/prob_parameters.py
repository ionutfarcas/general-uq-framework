import numpy as np

# parameters setup

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
left_stoch_boundary 	= [left_tau, left_zeff, left_q0, left_shat, left_omn, \
							left_omt, left_Tref, left_nref]

right_stoch_boundary 	= [right_tau, right_zeff, right_q0, right_shat, right_omn, \
							right_omt, right_Tref, right_nref]

# setup
dim             = 8
grid_level_init = 1
grid_level_ref  = 20
level_to_nodes  = 1
ref_step        = 0
total_no_gp     = 0

tols_all 		= 1e-4*np.ones(2**dim - 1) 
max_level       = grid_level_ref

# left and right bounds
left_bounds 	= np.zeros(dim)
right_bounds 	= np.ones(dim)

weight = lambda x: 1.0

weights 		= [weight for i in xrange(dim)]
init_multiindex = np.ones(dim, dtype=int)
