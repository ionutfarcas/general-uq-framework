import numpy as np 
import matplotlib as mpl 
from matplotlib.lines import Line2D	
mpl.use('TkAgg')
from matplotlib.pyplot import *
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.patches import ConnectionPatch
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


if __name__ == '__main__':

	dim = 8
	

	vals_color_map = get_cmap('Blues')
	text_color_map = get_cmap('hot')	

	rc("figure", dpi=400)           # High-quality figure ("dots-per-inch")
	# rc("text", usetex=True)         # Crisp axis ticks
	rc("font", family="serif")      # Crisp axis labels
	rc("legend", edgecolor='none')  # No boxes around legends
	rcParams["figure.figsize"] = (5, 3)
	rcParams.update({'font.size': 7})

	bboard = "#323E48" # blackboard slate gray
	chalk_white = "#DCDCDC"
	chalk_orange = "#fc9d28"
	transp = (1,1,1,0)

	# white base settings
	rc("figure",facecolor='w')
	rc("axes",facecolor='w',edgecolor='k',labelcolor='k')
	rc("savefig",facecolor='w')
	rc("text",color='k')
	rc("xtick",color='k')
	rc("ytick",color='k')

	# line settings for white base
	color1 = 'k'
	color2 = '#b2df8a'
	color3 = '#1f78b4'
	color4 = 'tab:red'

	fig = figure()
	ax 	= fig.add_subplot(111, projection='3d')

	# ax.set_aspect('equal')

	ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
	ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
	ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)

	#fig.canvas.manager.window.Move(0, 0)

	ax.yaxis.set_ticks([])
	ax.yaxis.set_ticklabels([])
	for line in ax.yaxis.get_ticklines():
		line.set_visible(False)

	ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([1, 0.1, 1, 1]))


	width = 0.5

	width 		= 0.2
	dx 			= 0.5*np.ones(dim)
	dy 			= 0.3*np.ones(dim)

	xpos = range(dim)
	zpos = np.zeros(dim)
	ypos = np.zeros(dim)


	local_sobol_indices = np.array([1.94252455e-02, 7.76642091e-04, 5.84844864e-01, 2.97989953e-01, \
		1.99052150e-02, 1.48517139e-05, 4.65726865e-03, 1.26715692e-04])

	total_sobol_indices = np.array([2.78564477e-02, 1.10309791e-03, 6.50561083e-01, 3.53937714e-01, \
		3.42227973e-02, 1.48517139e-05, 5.20287577e-03, 1.26715692e-04])


	multiindex_bin 		= np.load('results/multiindex_bin.npy')
	all_sobol_indices 	= np.load('results/all_Sobol_indices.npy')


	interactions = total_sobol_indices - local_sobol_indices
	ax.set_xticks(xpos)


	ax.bar3d(xpos, ypos, zpos, dx, dy, local_sobol_indices, color=color2)
	local = Rectangle((0, 0), 1, 1, fc=color2)

	ax.bar3d(xpos, ypos, local_sobol_indices, dx, dy, interactions, color=color3)
	interactions = Rectangle((0, 0), 1, 1, fc=color3)


	params = [r'$T_{e}$', r'$n_{e}$', r'$\omega_{T_e}$', r'$\omega_{n_e}$', r'$\tau$', r'$Z_{eff}$', r'$q$', r'$\hat{s}$']


	ax.set_xticks(range(dim))
	ax.set_xticklabels(params)

	ax.legend([interactions, local], \
				['sensitivity indices due to interactions', 'first-order sensitivity indices'], \
				bbox_to_anchor=(0.2, 0.8, 0.5, .01), ncol=1)


	ax.set_zlim([0, 0.7])
	

	tight_layout()

	# show()

	savefig('figures/total_sobol_3D.png', pad_inches=3)
	close()