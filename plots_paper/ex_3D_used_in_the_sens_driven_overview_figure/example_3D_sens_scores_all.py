from sg_lib.grid.grid import *
from sg_lib.algebraic.multiindex import *
from sg_lib.operation.interpolation_to_spectral import *
from sg_lib.adaptivity.spectral_scores_all import *

def test_function(x):
	x1 = x[0]
	x2 = x[1]
	x3 = x[2]

	a = 0.05
	b = 7

	test = np.sin(x1) + a*(np.sin(x2)**2) + b*(x3**4)*np.sin(x1)
	
	return test
    
if __name__ == '__main__':
	dim 			= 3
	left_bounds 	= np.zeros(dim)
	right_bounds 	= np.ones(dim)
	grid_level 		= 1
	level_to_nodes 	= 1
	weights 		= [lambda x: 1. for i in range(dim)]

	tols 		= 1e-4*np.ones(2**dim - 1)
	max_level 	= 20

	init_multiindex = np.ones(dim, dtype=int)
	
	
	print 'started simulation for tol', tols

	Grid_obj1 				= Grid(dim, grid_level, level_to_nodes, left_bounds, right_bounds, weights)
	Multiindex_obj 			= Multiindex(dim)
	InterpToSpectral_obj1 	= InterpolationToSpectral(dim, level_to_nodes, left_bounds, right_bounds, weights, max_level, Grid_obj1)
	Adaptivity_obj 			= SpectralScoresAll(dim, tols, init_multiindex, max_level, level_to_nodes, InterpToSpectral_obj1)

	init_multiindex_set = Multiindex_obj.get_std_total_degree_mindex(grid_level)
	init_grid_points 	= Grid_obj1.get_std_sg_surplus_points(init_multiindex_set)
	init_no_points 		= Grid_obj1.get_no_fg_grid_points(init_multiindex_set)


	multiindex_bin = Multiindex_obj.get_poly_mindex_binary(dim)

	InterpToSpectral_obj1.get_local_global_basis(Adaptivity_obj)

	for sg_point in init_grid_points:
		sg_val 		= test_function(sg_point)
		InterpToSpectral_obj1.update_sg_evals_all_lut(sg_point, sg_val)

	InterpToSpectral_obj1.update_sg_evals_multiindex_lut(init_multiindex, Grid_obj1)
	
	Adaptivity_obj.init_adaption()

	prev_len 		= len(init_no_points)
	no_adapt_steps 	= 0
	total_len 		= 1
	while not Adaptivity_obj.stop_adaption:
		no_adapt_steps += 1

		new_multiindices = Adaptivity_obj.do_one_adaption_step_preproc()

		for multiindex in new_multiindices:
			new_grid_points = Grid_obj1.get_sg_surplus_points_multiindex(multiindex)
			total_len 		+= len(new_grid_points)

			for sg_point in new_grid_points:
				sg_val = test_function(sg_point)
			
				InterpToSpectral_obj1.update_sg_evals_all_lut(sg_point, sg_val)

			InterpToSpectral_obj1.update_sg_evals_multiindex_lut(multiindex, Grid_obj1)
			
		Adaptivity_obj.do_one_adaption_step_postproc(new_multiindices)
		Adaptivity_obj.check_termination_criterion()

	print 'adaptivity done'
	print('total len = ', total_len)

	mindex_set = np.array(Adaptivity_obj.multiindex_set)

	print(np.max(mindex_set[:, 0]))
	print(np.max(mindex_set[:, 1]))
	print(np.max(mindex_set[:, 2]))

	print('old index')
	print(Adaptivity_obj.O.values())

	print('active set')
	print(Adaptivity_obj.A.values())

	grid_points_old_index_set = []
	for multiindex in Adaptivity_obj.O.values():
		grid_points = Grid_obj1.get_sg_surplus_points_multiindex(multiindex)
		grid_points_old_index_set.append(grid_points.tolist()[0])


	grid_points_active_set = []
	for multiindex in Adaptivity_obj.A.values():
		grid_points = Grid_obj1.get_sg_surplus_points_multiindex(multiindex)
		grid_points_active_set.append(grid_points.tolist()[0])



	InterpToSpectral_obj1.get_local_global_basis(Adaptivity_obj)

	sg_approx_eval = lambda x: InterpToSpectral_obj1.eval_operation_sg(Adaptivity_obj.multiindex_set, x)	

	coeff_scores = InterpToSpectral_obj1.get_spectral_coeff_sg(Adaptivity_obj.multiindex_set)

	mean_est 		= InterpToSpectral_obj1.get_mean(coeff_scores)
	var_est 		=  InterpToSpectral_obj1.get_variance(coeff_scores)
	local_sobol_est = InterpToSpectral_obj1.get_first_order_sobol_indices(coeff_scores, Adaptivity_obj.multiindex_set)
	total_sobol_est = InterpToSpectral_obj1.get_total_sobol_indices(coeff_scores, Adaptivity_obj.multiindex_set)

	sobol_all = InterpToSpectral_obj1.get_all_sobol_indices(multiindex_bin, coeff_scores, Adaptivity_obj.multiindex_set)

	print(mean_est, var_est)
	print(local_sobol_est)
	print(total_sobol_est)
	print(sobol_all)

	np.save('results/old_index_set.npy', Adaptivity_obj.O.values())
	np.save('results/active_set.npy', Adaptivity_obj.A.values())

	np.save('results/old_index_set_points.npy', np.array(grid_points_old_index_set))
	np.save('results/active_set_points.npy', np.array(grid_points_active_set))
