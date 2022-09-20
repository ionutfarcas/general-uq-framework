import numpy as np 
import matplotlib as mpl 
from matplotlib.lines import Line2D	
mpl.use('TkAgg')
from matplotlib.pyplot import *

def which_variables(param, multiindex_bin_of_interest):

	variables = []

	for multiindex in multiindex_bin_of_interest:

		vars 	= '$S_{'
		indices = ''
		
		for i, m in enumerate(multiindex):
			if m:
				indices += params_x[i]
				indices += ','

		indices = indices[:-1]

		vars += indices
		vars += '}$'
			
		variables.append(vars)


	var = '$S_{' + param + ',others}$'

	variables.append(var)

	return variables


def select_all_sobol_indices(dim, target_dim, multiindex_bin, all_sobol_indices):

	sobol_indices 		= {}
	bin_indices 		= {}
	bin_indices_perp 	= {}

	eps = 5e-3

	for d in range(dim):

		list_of_sobol_indices 		= []
		list_of_bin_indices 		= []
		list_of_bin_indices_perp 	= []

		for m, multiindex in enumerate(multiindex_bin):

			if multiindex[d]:
				if all_sobol_indices[m] >= eps:
					list_of_sobol_indices.append(all_sobol_indices[m])
					list_of_bin_indices.append(m)
				else:
					list_of_bin_indices_perp.append(m)

		sobol_indices[d] 	= list_of_sobol_indices
		bin_indices[d] 		= list_of_bin_indices
		bin_indices_perp[d] = list_of_bin_indices_perp

	return sobol_indices, bin_indices, bin_indices_perp
    
if __name__ == '__main__':

	dim = 8


	fig 	= figure()
	ax 		= fig.add_subplot(111)

	rcParams['lines.linewidth'] = 0
	rc("figure", dpi=400)           # High-quality figure ("dots-per-inch")
	# rc("text", usetex=True)         # Crisp axis ticks
	rc("font", family="serif")      # Crisp axis labels
	rc("legend", edgecolor='none')  # No boxes around legends
	rcParams["figure.figsize"] = (3, 3)
	rcParams.update({'font.size': 7})

	bboard = "#323E48" # blackboard slate gray
	chalk_white = "#DCDCDC"
	chalk_orange = "#fc9d28"
	transp = (1,1,1,0)

	patch_color1 = '#045a8d' # wT, wn
	patch_color2 = '#0570b0' # tau, wT
	patch_color3 = '#3690c0' # wT, T
	patch_color4 = '#74a9cf' # others
	
	text_color1 = '#fff7ec'
	text_color2 = '#fee8c8'
	text_color3 = '#fee8c8'
	text_color4 = '#fdd49e'

	text_colors = [text_color1, text_color4]
	

	# white base settings
	rc("figure",facecolor='w')
	rc("axes",facecolor='w',edgecolor='k',labelcolor='k')
	rc("savefig",facecolor='w')
	rc("text",color='k')
	rc("xtick",color='k')
	rc("ytick",color='k')

	total_sobol_indices = np.array([3.67337366e-02, 1.47519707e-05, 5.05392794e-03, 1.25864677e-04, \
 		3.55803235e-01, 6.50958127e-01, 2.85350992e-02, 5.54622903e-04])

	names_x = ['tau', 'Zeff', \
			    'q', 'shat', 'omega_{n_e}', 'omega_{T_e}', 'T_e', 'n_e']
	

	params_x = ['\\tau', 'Zeff', 'q', '\hat{s}', \
			  	'\omega_{n_e}', '\omega_{T_e}', \
			  	'T_{e}', 'n_{e}']

	params = ['$\\tau$', '$Z_{eff}$', '$q$', '$\hat{s}$', '$\omega_{n_e}$', '$\omega_{T_e}$', '$T_{e}$', '$n_{e}$']

	multiindex_bin 		= np.load('results/multiindex_bin.npy')
	all_sobol_indices 	= np.load('results/all_Sobol_indices.npy')

	target_dim 	= 4

	param 	= params_x[target_dim]
	qoi 	= params[target_dim]

	sobol_indices_divided, bin_indices, bin_indices_perp = select_all_sobol_indices(dim, target_dim, multiindex_bin, all_sobol_indices)

	multiindex_bin_of_interest 		= multiindex_bin[np.array(bin_indices[target_dim], dtype=int)]
	multiindex_bin_of_interest_per 	= multiindex_bin[np.array(bin_indices_perp[target_dim], dtype=int)]

	variables = which_variables(param, multiindex_bin_of_interest)


	sobol_indices_of_interest = np.zeros(len(sobol_indices_divided[target_dim]) + 1)

	for x in range(len(sobol_indices_divided[target_dim])):
		sobol_indices_of_interest[x] 	= sobol_indices_divided[target_dim][x]

	sobol_indices_of_interest[-1] = np.sum(all_sobol_indices[bin_indices_perp[target_dim]])

	sobol_indices_of_interest = sobol_indices_of_interest[1:]
	variables = variables[1:]


	sobol_indices_of_interest = np.array(sobol_indices_of_interest)/np.sum(sobol_indices_of_interest)
	###

	colors = [patch_color1, patch_color4]
	
	patches, texts, autotexts  = ax.pie(sobol_indices_of_interest, colors=colors, autopct='%1.1f%%', startangle=-40)


	text_sizes 	= []
	y_pos 		= []
	for i, t in enumerate(autotexts):

		if sobol_indices_of_interest[i] < 0.05:
			t.set_fontsize(15)
			text_sizes.append(15)
			y_pos.append(1.0)
			t.set_x(0.68)
			t.set_y(-0.64)

		elif 0.05 <= sobol_indices_of_interest[i] <= 0.15:
			t.set_fontsize(28)
			text_sizes.append(28)
			y_pos.append(1.5)

		elif 0.15 <= sobol_indices_of_interest[i] <= 0.21:
			t.set_fontsize(40)
			text_sizes.append(40)
			y_pos.append(1.2)

		else:
			t.set_fontsize(50)
			text_sizes.append(50)
			y_pos.append(1.1)

		# t.set_color(text_color_map(sobol_indices_of_interest[i]))
		t.set_color(text_colors[i])

	bbox_props  = dict(boxstyle="square,pad=0.1", fc="w", ec="k", lw=0.0)
	kw          = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

	for i, p in enumerate(patches):
	    ang = (p.theta2 - p.theta1)/2. + p.theta1
	    y   = np.sin(np.deg2rad(ang))
	    x   = np.cos(np.deg2rad(ang))
	    
	    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
	    connectionstyle     = "angle,angleA=0,angleB={}".format(ang)
	    kw["arrowprops"].update({"connectionstyle": connectionstyle})
	    ax.annotate(variables[i], xy=(x, y), xytext=(1.0*np.sign(x), y_pos[i]*y), horizontalalignment=horizontalalignment, fontsize=60, **kw)

	for w in patches:
	    w.set_linewidth(2)
	    w.set_edgecolor('black')

	ax.set_title('interactions ' + params[target_dim], fontsize=50)

# tight_layout()

show()

fig_name = 'figures/interactions_wn_2D.pdf'
fig.savefig(fig_name, format="pdf", bbox_inches='tight')