import numpy as np 
import matplotlib as mpl 
from matplotlib.lines import Line2D	
mpl.use('TkAgg')
import matplotlib.pyplot as plt


if __name__ == '__main__':


	#sg_evals 	= np.load('results/lo_fi_evals_interp_accuracy_test.npy')
	sg_evals = np.array([0.5464996166374166, 0.14800508106333246, 0.3460771647488223, 0.9360532272123246, 0.744181954455008, \
							0.9389382979064639, 0.30921153370705917, 1.6489025582000305, 1.926085241239227, 0.4348140217506337, \
							0.20128814798075148, 1.116179868580432, 0.3870489668342398, 0.653107878472204, 0.9324264923274856, \
							0.4989614260110617, 0.3191694519763938, 1.0964092555367666, 0.24896303168368797, 1.034742784020278, \
							1.8562004355731936, 0.2889304819262536, 0.4444559455934053, 1.5225248356677845, 0.7718830949707165, \
							0.27033744607286536, 0.5249959299380768, 2.56368394312125, 0.3668293322532268, 0.5946583789373023, \
							0.4173590458641391, 0.21902023288742822])

	ref_evals 	= np.array([0.5443849552520857, 0.13664087170151182, 0.32461651088560795, 0.9316264966235148, 0.7446535523139475, \
								0.9205134276383964, 0.30084836703701734, 1.7141812930949392, 1.8986595325099596, 0.4486339613264476, \
								0.1982889539674602, 1.1167236512441159, 0.366015112959696, 0.6538933718252395, 0.9368233402050214 ,\
								0.5153333707971577, 0.3068912269028179, 1.0822352532862483, 0.2447305737167217, 1.0417863916611547, \
								1.8796472171535723, 0.2903897828074157, 0.43631223846026973, 1.5061839990793537, 0.7774547614256087, \
								0.26714610917557013, 0.5257202336913096, 2.5269272289622875, 0.3721734025607018, 0.5891631003731402, \
								0.4113328104561748,  0.2271838627212292])

	
	plt.rc("figure", dpi=400)           # High-quality figure ("dots-per-inch")
	plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica"})
	# plt.rc("legend", edgecolor='none')  # No boxes around legends
	plt.rcParams["figure.figsize"] = (6, 3)
	plt.rcParams.update({'font.size': 6})

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
	color1 = 'k'
	color2 = 'tab:orange'
	color3 = 'tab:blue'
	color4 = 'tab:red'

	fig 	= plt.figure()
	ax1 	= fig.add_subplot(111)

	ax1.spines['right'].set_visible(False)
	ax1.spines['top'].set_visible(False)
	ax1.yaxis.set_ticks_position('left')
	ax1.xaxis.set_ticks_position('bottom')

	x = np.linspace(0, np.max(ref_evals), 100)


	ax1.plot(ref_evals, sg_evals, linestyle='', marker='o', markersize=1.5, color=color1)
	ax1.plot(x, x, linestyle='-', lw=0.5, color='gray', alpha=0.7)
	ax1.set_xlabel('Testing samples: high-fidelity heat flux '  + r'$Q_{\mathrm{hi-fi}} [\mathrm{MW}]$')
	ax1.set_ylabel('Testing samples: surrogate model heat flux '  + r'$Q_{\mathrm{SG}} [\mathrm{MW}]$')
	
	plt.tight_layout()

	# plt.show()

	plt.savefig('figures/red_model_vs_hi_fi_model.png', pad_inches=3)
	plt.close()