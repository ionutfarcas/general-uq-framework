from sg_lib.grid.grid import *
from sg_lib.algebraic.multiindex import *
from sg_lib.operation.interpolation_to_spectral import *
from sg_lib.adaptivity.spectral_scores_all import *
from sg_lib.util.serialize import *

from time import clock

import sys
sys.path.append('./configuration/')
from prob_parameters import *

######
def is_in_L(multiindex, multiindex_set):

	is_in = 0

	if multiindex in multiindex_set:
		is_in = 1

	return is_in

def calc_CT_sign(multiindex, multiindex_set):

	dim = len(multiindex)

	Z = list(product([0, 1], repeat=dim))

	sign = 0

	for z in Z:

		z_neigh = add_multiinices(multiindex, z)
		chi_z 	= is_in_L(z_neigh, multiindex_set)

		sign 	+= (-1)**np.sum(z) * chi_z

	return sign

def add_multiinices(m1, m2):

	s = np.zeros_like(m1)

	for i in range(len(m1)):

		s[i] = m1[i] + m2[i]

	return s.tolist()
######

def get_intersection_indices(curr_sg_points, all_sg_points):

	all_sg_points 	= all_sg_points.tolist()
	curr_sg_points 	= curr_sg_points.tolist()

	intersection_indices = [all_sg_points.index(point) for point in curr_sg_points]

	return intersection_indices

def compute_corr_coeff(hi_fi_evals, lo_fi_evals):

	no_model_eval_corr = len(hi_fi_evals)

	print(no_model_eval_corr)

	mean_hi_fi = np.mean(hi_fi_evals)
	mean_lo_fi = np.mean(lo_fi_evals)

	std_hi_fi = np.std(hi_fi_evals, ddof=1)
	std_lo_fi = np.std(lo_fi_evals, ddof=1)

	rho_12 = np.sum(np.array([(hi_fi_eval - mean_hi_fi)*(lo_fi_eval - mean_lo_fi) \
				for hi_fi_eval, lo_fi_eval in zip(hi_fi_evals, lo_fi_evals)]))/(std_hi_fi*std_lo_fi*(no_model_eval_corr - 1.))

	return std_hi_fi, std_lo_fi, rho_12
    
if __name__ == '__main__':

	dim 	= 8 
	no_rv 	= 32

	seed = 981287

	np.random.seed(seed)

	std_rand_vars 	= np.random.uniform(0, 1, size=(no_rv, dim))
	hi_fi_evals 	= np.array([0.5443849552520857, 0.13664087170151182, 0.32461651088560795, 0.9316264966235148, 0.7446535523139475, \
								0.9205134276383964, 0.30084836703701734, 1.7141812930949392, 1.8986595325099596, 0.4486339613264476, \
								0.1982889539674602, 1.1167236512441159, 0.366015112959696, 0.6538933718252395, 0.9368233402050214 ,\
								0.5153333707971577, 0.3068912269028179, 1.0822352532862483, 0.2447305737167217, 1.0417863916611547, \
								1.8796472171535723, 0.2903897828074157, 0.43631223846026973, 1.5061839990793537, 0.7774547614256087, \
								0.26714610917557013, 0.5257202336913096, 2.5269272289622875, 0.3721734025607018, 0.5891631003731402, \
								0.4113328104561748,  0.2271838627212292])

	hi_fi_evals = hi_fi_evals[:no_rv]

	acc_rate_evals 		= []
	runtime_all 		= []
	all_no_sg_points 	= []
	
	real_part = [0.61348292596845, \
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


	Grid_obj 				= Grid(dim, grid_level_init, level_to_nodes, left_bounds, right_bounds, weights)	
	Multiindex_obj 			= Multiindex(dim)
	InterpToSpectral_obj 	= InterpolationToSpectral(dim, level_to_nodes, left_bounds, right_bounds, weights)
	Adaptivity_obj 			= SpectralScoresAll(dim, 1e-4*np.ones(2**dim - 1), init_multiindex, max_level, level_to_nodes, InterpToSpectral_obj)
	Serialize_obj 			= SerializeRefInfo()

	init_multiindex_set = Multiindex_obj.get_std_total_degree_mindex(grid_level_init)
	init_grid_points 	= Grid_obj.get_std_sg_surplus_points(init_multiindex_set)
	init_no_points 		= Grid_obj.get_no_fg_grid_points(init_multiindex_set)
	total_no_gp 		= init_no_points

	all_sg_points 			= np.load('all_sg_points.npy')
	intersection_indices 	= get_intersection_indices(init_grid_points, all_sg_points)

	InterpToSpectral_obj.get_local_global_basis(Adaptivity_obj)

	for i in intersection_indices:
		sg_val = real_part[i]
		InterpToSpectral_obj.update_sg_evals_lut(sg_val)
	InterpToSpectral_obj.update_func_evals(Grid_obj, init_multiindex_set)
	
	Adaptivity_obj.init_adaption()

	ref_step 		= 0
	no_sg_points 	= 1
	while not Adaptivity_obj.stop_adaption:
		ref_step 	+= 1

		print 'adapt step', ref_step

		new_multiindices = Adaptivity_obj.do_one_adaption_step_preproc()

		curr_multiindex_set = Adaptivity_obj.multiindex_set
		curr_grid_points 	= Grid_obj.get_std_sg_surplus_points(curr_multiindex_set)
		curr_len 			= len(curr_grid_points)

		for multiindex in new_multiindices:
			mindex_grid_points 		= Grid_obj.get_sg_surplus_points_multiindex(multiindex)	
			intersection_indices 	= get_intersection_indices(mindex_grid_points, all_sg_points)

			for i in intersection_indices:
				sg_val = real_part[i]
				InterpToSpectral_obj.update_sg_evals_lut(sg_val)

				no_sg_points += 1


				
		InterpToSpectral_obj.update_func_evals(Grid_obj, curr_multiindex_set)

		curr_no_points 	= Grid_obj.get_no_surplus_grid_points(new_multiindices)
		curr_coeffs 	= [] 

		Adaptivity_obj.do_one_adaption_step_postproc(new_multiindices)
		Adaptivity_obj.check_termination_criterion()
		
		total_no_gp 	= curr_len


		################
		InterpToSpectral_obj.get_local_global_basis(Adaptivity_obj)

		if len(new_multiindices):

			all_evals 	= InterpToSpectral_obj._fg_func_evals
			mindex_set 	= Adaptivity_obj.multiindex_set

			np.save('func_evals.npy', all_evals)
			np.save('multiindex_set.npy', mindex_set)

			evals 			= np.load('func_evals.npy', allow_pickle=True, encoding="bytes")
			multiindex_set 	= np.load('multiindex_set.npy', allow_pickle=True, encoding="bytes")
			multiindex_set 	= multiindex_set.tolist()

			CT_signs = [calc_CT_sign(m, multiindex_set) for m in multiindex_set]

			eval_lo_fi_model = lambda x: InterpToSpectral_obj.eval_operation_sg_ct(evals, CT_signs, multiindex_set, x)

			lo_fi_evals = np.zeros(no_rv)
			for nn, rvar in enumerate(std_rand_vars):
				lo_fi_evals[nn] = eval_lo_fi_model(rvar)

			print curr_len, lo_fi_evals
			
			file_name = 'results/SG_evals_' + str(curr_len) + '.npz'
			np.savez(file_name, n=curr_len, sg_evals=lo_fi_evals)



	print 'REFINEMENT FINISHED'

	print 'number of refinement steps', ref_step
	print 'total number of grid points', no_sg_points, total_no_gp

