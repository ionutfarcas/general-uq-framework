from sg_lib.grid.grid import *
from sg_lib.algebraic.multiindex import *
from sg_lib.operation.interpolation_to_spectral import *
from sg_lib.adaptivity.spectral_scores_all import *
from sg_lib.util.serialize import *

import sys
sys.path.append('./configuration/')
from prob_parameters import *

# dens ions
left_omn  	= 88 - 0.2*88
right_omn  	= 88 + 0.2*88

### fastD ###
# omt fastD
left_omt 	= 186 - 0.2*186 
right_omt 	= 186 + 0.2*186
    
if __name__ == '__main__':

	sg_evals = [0.61348292596845, \
				0.5412175549873134, 0.6168676914394483, 0.5674822363494763, 0.6233697201658177, 0.3028601462581284, 1.4598106247588252, 0.7181418263508086, 0.6342369569524193, \
				0.19911996330874773, \
	 		 	1.2176418385888925, 0.8172419028328397, \
	 		 	1.0353871671769022, \
	 		 	0.0739474188275456, \
	 		 	0.40976244616792556, 2.5336681132334626,\
	 		 	0.4705470080153765, \
	 		 	0.3560362342104805, 1.7187308011925584, 0.5158765198830032, \
	 		 	0.23282318497424428, \
	 		 	0.7242830368341155, 0.2727348511235845, 1.2151074693793693, 0.6308016096509583,\
	 		 	0.18247141698483577, \
	 		 	0.4870198372997431, 0.7058952154712363, 0.2752941318687094, 1.471117867858046, 0.6674123952109071,\
	 		 	0.1747207687454509, \
	 		 	1.4180720205212722, 0.9586411328162069, \
	 		 	0.5826550275978518, 1.5752982945156135, \
	 		 	0.23385301998982863, \
	 		 	1.0517456971655021, 0.687611418536378, \
	 		 	2.0872365610362436, 0.06753316276407874, \
	 		 	2.9707744599997663, 0.08772357862328531, \
	 		 	0.5701035599664347, 0.34579168146679445, 1.859051190041283, \
	 		 	0.21925994932976461, \
	 		 	1.461796184066567, 1.031401098180107, \
	 		 	0.08223762166493676, \
	 		 	0.5542452144487008, 0.5915777393216851, 0.3141619756435272, 1.5146565245721624, 0.740157904356016, 0.592161749981647, \
	 		 	0.20641336318402603, \
	 		 	0.8815794523980833, 1.005706905368122, 0.5489808574007238, 0.30641014338292566, 1.2139336226120983, 1.0692405248241579, \
	 		 	0.3653601167003414, 0.9682573328234629, 1.04936582329158, 0.48038763812087076, \
	 		 	0.35455481412556034, 1.1322151377707192, 0.8245050343785368, \
	 		 	1.3724139384488272, 0.37499021107805924, \
	 		 	0.5501452092806046, 0.5729376326740432, 0.6074379330122902, 0.30628747354429076, 1.4824302125517437, 0.7279975829326205, 0.6416375765202585, \
	 		 	0.8514145207945262, 0.32055998674810904, 1.4153690222453972, \
	 		 	0.21305546943018489, \
	 		 	0.8959506558442462, 2.4874880858591877, 0.06680093423429759] # 86 sims

	print dim, tols_all[0]

	Grid_obj 				= Grid(dim, grid_level_init, level_to_nodes, left_bounds, right_bounds, weights)
	Multiindex_obj 			= Multiindex(dim)
	InterpToSpectral_obj 	= InterpolationToSpectral(dim, level_to_nodes, left_bounds, right_bounds, weights, max_level, Grid_obj)
	Adaptivity_obj 			= SpectralScoresAll(dim, tols_all, init_multiindex, max_level, level_to_nodes, InterpToSpectral_obj)

	init_multiindex_set = Multiindex_obj.get_std_total_degree_mindex(grid_level_init)
	init_grid_points 	= Grid_obj.get_std_sg_surplus_points(init_multiindex_set)
	init_no_points 		= Grid_obj.get_no_fg_grid_points(init_multiindex_set)

	InterpToSpectral_obj.get_local_global_basis(Adaptivity_obj)

	mapped_sg_points = Grid_obj.map_std_sg_surplus_points(init_grid_points, left_stoch_boundary, right_stoch_boundary)

	global_index = 0
	for sg_point, mapped_sg_point in zip(init_grid_points, mapped_sg_points):
		sg_val 		= sg_evals[global_index]

		print 'input pairs'
		print mapped_sg_point, sg_val
		InterpToSpectral_obj.update_sg_evals_all_lut(sg_point, sg_val)

	InterpToSpectral_obj.update_sg_evals_multiindex_lut(init_multiindex, Grid_obj)
	
	Adaptivity_obj.init_adaption()

	prev_len 		= len(init_no_points)
	no_adapt_steps 	= 0
	total_len 		= 1
	
	print 'enter loop'
	not_finished = False
	while not not_finished:

		print 'ADAPT STEP ' + str(no_adapt_steps + 1)
		no_adapt_steps += 1

		new_multiindices = Adaptivity_obj.do_one_adaption_step_preproc()

		for multiindex in new_multiindices:
			new_grid_points = Grid_obj.get_sg_surplus_points_multiindex(multiindex)
			total_len 		+= len(new_grid_points)

			mapped_sg_points = Grid_obj.map_std_sg_surplus_points(new_grid_points, left_stoch_boundary, right_stoch_boundary)

			for sg_point, mapped_sg_point in zip(new_grid_points, mapped_sg_points):
				global_index += 1

				sg_val = sg_evals[global_index]

				print 'input pairs'
				print mapped_sg_point, sg_val
				InterpToSpectral_obj.update_sg_evals_all_lut(sg_point, sg_val)

			InterpToSpectral_obj.update_sg_evals_multiindex_lut(multiindex, Grid_obj)
			
		Adaptivity_obj.do_one_adaption_step_postproc(new_multiindices)
		Adaptivity_obj.check_termination_criterion()

		print 'TERMINATION CRITERION', Adaptivity_obj.stop_adaption

		if global_index >= len(sg_evals) - 1:
			not_finished = True


	InterpToSpectral_obj.get_local_global_basis(Adaptivity_obj)

	coeff_scores = InterpToSpectral_obj.get_spectral_coeff_sg(Adaptivity_obj.multiindex_set)

	mean_est 		= InterpToSpectral_obj.get_mean(coeff_scores)
	var_est 		=  InterpToSpectral_obj.get_variance(coeff_scores)
	local_sobol_est = InterpToSpectral_obj.get_first_order_sobol_indices(coeff_scores, Adaptivity_obj.multiindex_set)
	total_sobol_est = InterpToSpectral_obj.get_total_sobol_indices(coeff_scores, Adaptivity_obj.multiindex_set)

	print mean_est, var_est, local_sobol_est, total_sobol_est


	do_one_more_ref_step = False

	while not do_one_more_ref_step:

		print 'new adapt step'
		no_adapt_steps += 1

		new_multiindices = Adaptivity_obj.do_one_adaption_step_preproc()

		if len(new_multiindices):
			do_one_more_ref_step = True

		print 'multiindices adaptivity'
		print new_multiindices

		for multiindex in new_multiindices:
			new_grid_points = Grid_obj.get_sg_surplus_points_multiindex(multiindex)
			total_len 		+= len(new_grid_points)

			mapped_sg_points = Grid_obj.map_std_sg_surplus_points(new_grid_points, left_stoch_boundary, right_stoch_boundary)

			for sg_point, mapped_sg_point in zip(new_grid_points, mapped_sg_points):

				print('new simulation')
				print mapped_sg_point