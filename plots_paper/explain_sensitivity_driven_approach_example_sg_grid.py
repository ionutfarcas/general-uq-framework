import numpy as np
from itertools import product
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import FancyArrowPatch
from matplotlib.pyplot import *
from matplotlib.ticker import ScalarFormatter
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.mplot3d import proj3d

def drawSphere(xCenter, yCenter, zCenter, r):
    #draw sphere
    u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
   
    x=np.cos(u)*np.sin(v)
    y=np.sin(u)*np.sin(v)
    z=np.cos(v)
    
    # shift and scale sphere
    x = r*x + xCenter
    y = r*y + yCenter
    z = r*z + zCenter
    
    return (x, y, z)


if __name__ == '__main__':

	grid_points_old_index_set 		= np.load('ex_3D_used_in_the_sens_driven_overview_figure/results/old_index_set_points.npy')
	grid_points_active_set 			= np.load('ex_3D_used_in_the_sens_driven_overview_figure/results/active_set_points.npy')


	rc("figure", dpi=400)           # High-quality figure ("dots-per-inch")
	# rc("text", usetex=True)         # Crisp axis ticks
	rc("font", family="serif")      # Crisp axis labels
	rc("legend", edgecolor='none')  # No boxes around legends
	# rcParams["figure.figsize"] = (5, 8)
	rcParams.update({'font.size': 18})

	rcParams['grid.color'] = (0.5, 0.5, 0.5, 0.1)

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
	color1 = '#d95f02'
	color2 = '#1b9e77'
	color3 = '#7570b3'

	fig 	= figure()
	ax 		= fig.add_subplot(111, projection='3d')

	radius = 0.03

	for point in grid_points_old_index_set.tolist():

		(x, y, z) = zip(point)
		(x, y, z) = drawSphere(x, y, z, radius)
		ax.plot_surface(x, y, z, color=color1)

	for point in grid_points_active_set.tolist()[:-3]:

		(x, y, z) = zip(point)
		(x, y, z) = drawSphere(x, y, z, radius)
		ax.plot_surface(x, y, z, color=color2)

	for point in grid_points_active_set.tolist()[3:]:

		(x, y, z) = zip(point)
		(x, y, z) = drawSphere(x, y, z, radius)
		ax.plot_surface(x, y, z, color=color3)


	ticks = [0.0, 0.25, 0.5, 0.75, 1.0]
	
	ax.xaxis.set_ticks(ticks)
	ax.xaxis.set_ticklabels([])


	ax.yaxis.set_ticks(ticks)
	ax.yaxis.set_ticklabels([])

	ax.zaxis.set_ticks(ticks)
	ax.zaxis.set_ticklabels([])


	ax.set_xlabel('1st uncertain input ' + r'$\theta_1$', labelpad=-10)
	ax.set_ylabel('2nd uncertain input ' + r'$\theta_2$', labelpad=-10)
	ax.set_zlabel('3rd uncertain input ' + r'$\theta_3$', labelpad=-10)

	ax.view_init(10, 10)



	tight_layout()

	#show()

	savefig('figures/sens_driven_summary_example_3D_grid.png', pad_inches=3)
	close()