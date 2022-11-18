import numpy as np 
import matplotlib as mpl 
from matplotlib.lines import Line2D	
mpl.use('TkAgg')
import matplotlib.pyplot as plt


def trunc(values, decs=0):
    return np.trunc(values*10**decs)/(10**decs)


if __name__ == '__main__':

	n = [12, 16, 20, 25, 31, 36, 40, 45, 51, 57]

	n_all = [12, 16, 20, 25, 26, 31, 34, 36, 39, 40, 31, 44, 45, 51, 51, 57]

	ref_evals 	= np.array([0.5443849552520857, 0.13664087170151182, 0.32461651088560795, 0.9316264966235148, 0.7446535523139475, \
								0.9205134276383964, 0.30084836703701734, 1.7141812930949392, 1.8986595325099596, 0.4486339613264476, \
								0.1982889539674602, 1.1167236512441159, 0.366015112959696, 0.6538933718252395, 0.9368233402050214 ,\
								0.5153333707971577, 0.3068912269028179, 1.0822352532862483, 0.2447305737167217, 1.0417863916611547, \
								1.8796472171535723, 0.2903897828074157, 0.43631223846026973, 1.5061839990793537, 0.7774547614256087, \
								0.26714610917557013, 0.5257202336913096, 2.5269272289622875, 0.3721734025607018, 0.5891631003731402, \
								0.4113328104561748,  0.2271838627212292])


	indices_to_plot = [1, 28, 11, 27]

	sg_results_1 = np.zeros(len(n))
	sg_results_2 = np.zeros(len(n))
	sg_results_3 = np.zeros(len(n))
	sg_results_4 = np.zeros(len(n))
	for i, n_ in enumerate(n):

		data 			= np.load('results/SG_lo_fi_evals/SG_evals_' + str(n_) + '.npz')
		sg_results_1[i] = data['sg_evals'][indices_to_plot[0]]
		sg_results_2[i] = data['sg_evals'][indices_to_plot[1]]
		sg_results_3[i] = data['sg_evals'][indices_to_plot[2]]
		sg_results_4[i] = data['sg_evals'][indices_to_plot[3]]


	sg_results_all_1 = np.zeros(len(n_all))
	sg_results_all_2 = np.zeros(len(n_all))
	sg_results_all_3 = np.zeros(len(n_all))
	sg_results_all_4 = np.zeros(len(n_all))
	for i, n_ in enumerate(n_all):

		data 				= np.load('results/SG_lo_fi_evals/SG_evals_' + str(n_) + '.npz')
		sg_results_all_1[i] = data['sg_evals'][indices_to_plot[0]]
		sg_results_all_2[i] = data['sg_evals'][indices_to_plot[1]]
		sg_results_all_3[i] = data['sg_evals'][indices_to_plot[2]]
		sg_results_all_4[i] = data['sg_evals'][indices_to_plot[3]]

	
	plt.rc("figure", dpi=400)           # High-quality figure ("dots-per-inch")
	plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica"})
	# plt.rc("legend", edgecolor='none')  # No boxes around legends
	plt.rcParams["figure.figsize"] = (6, 3)
	plt.rcParams.update({'font.size': 5})

	bboard = "#323E48" # blackboard slate gray
	chalk_white = "#DCDCDC"
	chalk_orange = "#fc9d28"
	transp = (1,1,1,0)

	# white base settings
	plt.rc("figure",facecolor='w')
	plt.rc("axes",facecolor='w',edgecolor='k',labelcolor='k')
	plt.rc("savefig",facecolor='w')
	plt.rc("text",color='k')
	plt.rc("xtick",color='k')
	plt.rc("ytick",color='k')

	# line settings for white base
	charcoal    = [0.1, 0.1, 0.1]
	color1      = '#d95f02'
	color2      = '#1251BF'

	fig 	= plt.figure()
	ax1 	= fig.add_subplot(111)
	# ax2 	= fig.add_subplot(122)

	ax1.spines['right'].set_visible(False)
	ax1.spines['top'].set_visible(False)
	ax1.yaxis.set_ticks_position('left')
	ax1.xaxis.set_ticks_position('bottom')

	# ax2.spines['right'].set_visible(False)
	# ax2.spines['top'].set_visible(False)
	# ax2.yaxis.set_ticks_position('left')
	# ax2.xaxis.set_ticks_position('bottom')

	ax1.semilogy(n, ref_evals[indices_to_plot[0]] * np.ones(len(n)), linestyle='-', lw=0.75, color=color1)
	ax1.semilogy(n, ref_evals[indices_to_plot[1]] * np.ones(len(n)), linestyle='-', lw=0.75, color=color1)
	ax1.semilogy(n, ref_evals[indices_to_plot[2]] * np.ones(len(n)), linestyle='-', lw=0.75, color=color1)
	ax1.semilogy(n, ref_evals[indices_to_plot[3]] * np.ones(len(n)), linestyle='-', lw=0.75, color=color1)

	ax1.semilogy(n, sg_results_1, linestyle='--', lw=0.75, marker='o', markersize=2, color=color2)
	ax1.semilogy(n, sg_results_2, linestyle='--', lw=0.75, marker='o', markersize=2, color=color2)
	ax1.semilogy(n, sg_results_3, linestyle='--', lw=0.75, marker='o', markersize=2, color=color2)
	ax1.semilogy(n, sg_results_4, linestyle='--', lw=0.75, marker='o', markersize=2, color=color2)
	

	ax1.text(50, 0.85*ref_evals[indices_to_plot[0]], 'Sample 32')
	ax1.text(50, 0.85*ref_evals[indices_to_plot[1]], 'Sample 29')
	ax1.text(50, 0.85*ref_evals[indices_to_plot[2]], 'Sample 12')
	ax1.text(50, 0.85*ref_evals[indices_to_plot[3]], 'Sample 28')
	
	ax1.set_xlabel('Number of sparse grid points to construct the interpolation-based surrogate model')
	# ax1.set_xlabel('Number of sparse grid points')
	ax1.set_ylabel('Heat flux '  + r'$Q [\mathrm{MW}]$')

	x_ticks 	= [12, 20, 30, 40, 50, 57]
	x_labels 	= [12, 20, 30, 40, 50, 57]

	y_ticks 	= [ref_evals[indices_to_plot[0]], ref_evals[indices_to_plot[1]], \
					ref_evals[indices_to_plot[2]], ref_evals[indices_to_plot[3]]]
	y_labels 	= [trunc(ref_evals[indices_to_plot[0]], 4), trunc(ref_evals[indices_to_plot[1]], 4), \
					trunc(ref_evals[indices_to_plot[2]], 4), trunc(ref_evals[indices_to_plot[3]], 4)]


	ax1.set_xticks(x_ticks)
	ax1.set_xticklabels(x_labels)

	ax1.set_yticks(y_ticks)
	ax1.set_yticklabels(y_labels)

	ax1.set_xlim([11, 58])


	# # ax2.violinplot([sg_results_all_1, sg_results_all_2, sg_results_all_3, sg_results_all_4], showmedians=True)
	# violin1 = ax2.violinplot(sg_results_all_1, showmeans = True, showextrema = False)
	# ax2.set_yscale('log')
	# ax2.set_xticks([1])
	# ax2.set_xticklabels(['sample 28'])

	# ax2.semilogy([0.7, 1.3], ref_evals[indices_to_plot[0]] * np.ones(2),  linestyle='-', lw=0.75, color=charcoal)

	# y_ticks 	= [0.06, ref_evals[indices_to_plot[0]]]
	# y_labels 	= ['', trunc(ref_evals[indices_to_plot[0]], 4)]


	# ax2.set_yticks(y_ticks)
	# ax2.set_yticklabels(y_labels)


	# for pc in violin1['bodies']:
	#     pc.set_facecolor(color2)
	#     pc.set_edgecolor(color2)


	# ax1.grid(True)
	
	plt.tight_layout()

	# plt.show()

	plt.savefig('figures/red_model_convergence.png', pad_inches=3)
	plt.close()