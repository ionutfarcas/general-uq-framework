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

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


def draw_cube(ax, multiindex, alpha=1.0, color='red', dim=3):

	temp 		= np.ones(dim)
	coords 		= np.array([multiindex - temp, multiindex]).T
	points 		= np.array(list((product(*coords))))

	vert_map 	= {0:0, 1:4, 2:6, 3:2, 4:1, 5:5, 6:7, 7:3}
	# ax.scatter3D(points[:, 0], points[:, 1], points[:, 2], c='k', s=4)

	verts = [[points[vert_map[0]],points[vert_map[1]],points[vert_map[2]],points[vert_map[3]]],
	 [points[vert_map[4]],points[vert_map[5]],points[vert_map[6]],points[vert_map[7]]], 
	 [points[vert_map[0]],points[vert_map[1]],points[vert_map[5]],points[vert_map[4]]], 
	 [points[vert_map[2]],points[vert_map[3]],points[vert_map[7]],points[vert_map[6]]], 
	 [points[vert_map[1]],points[vert_map[2]],points[vert_map[6]],points[vert_map[5]]],
	 [points[vert_map[4]],points[vert_map[7]],points[vert_map[3]],points[vert_map[0]]], 
	 [points[vert_map[2]],points[vert_map[3]],points[vert_map[7]],points[vert_map[6]]]]

	collection = Poly3DCollection(verts, linewidths=0.5, edgecolors='k')
	collection.set_alpha(alpha)
	collection.set_facecolor(color)
	collection.set_edgecolor('black')

	ax.add_collection3d(collection)

def draw_cube_refinement(ax, multiindex, alpha=1.0, color='red', dim=3):

	temp 		= np.ones(dim)
	coords 		= np.array([multiindex - temp, multiindex]).T
	points 		= np.array(list((product(*coords))))

	vert_map 	= {0:0, 1:4, 2:6, 3:2, 4:1, 5:5, 6:7, 7:3}
	# ax.scatter3D(points[:, 0], points[:, 1], points[:, 2], c='k', s=4)

	verts = [[points[vert_map[0]],points[vert_map[1]],points[vert_map[2]],points[vert_map[3]]],
	 [points[vert_map[4]],points[vert_map[5]],points[vert_map[6]],points[vert_map[7]]], 
	 [points[vert_map[0]],points[vert_map[1]],points[vert_map[5]],points[vert_map[4]]], 
	 [points[vert_map[2]],points[vert_map[3]],points[vert_map[7]],points[vert_map[6]]], 
	 [points[vert_map[1]],points[vert_map[2]],points[vert_map[6]],points[vert_map[5]]],
	 [points[vert_map[4]],points[vert_map[7]],points[vert_map[3]],points[vert_map[0]]], 
	 [points[vert_map[2]],points[vert_map[3]],points[vert_map[7]],points[vert_map[6]]]]

	collection = Poly3DCollection(verts, linewidths=0.5, edgecolors='k')
	collection.set_alpha(alpha)
	collection.set_facecolor(color)
	collection.set_edgecolor('black')

	ax.add_collection3d(collection)


if __name__ == '__main__':

	old_index_set 		= np.load('ex_3D_used_in_the_sens_driven_overview_figure/results/old_index_set.npy')
	active_set 			= np.load('ex_3D_used_in_the_sens_driven_overview_figure/results/active_set.npy')


	rc("figure", dpi=400)           # High-quality figure ("dots-per-inch")
	# rc("text", usetex=True)         # Crisp axis ticks
	rc("font", family="serif")      # Crisp axis labels
	rc("legend", edgecolor='none')  # No boxes around legends
	rcParams["figure.figsize"] = (5, 5)
	rcParams.update({'font.size': 18})

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

	ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
	ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
	ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)


	max_index = np.amax(active_set) 

	ax.set_xlim([0, max_index])
	ax.set_ylim([0, max_index])
	ax.set_zlim([0, max_index])

	for mindex in old_index_set:
		draw_cube(ax, mindex, color=color1)

	for mindex in active_set[:-3]:
		draw_cube(ax, mindex, color=color2)

	for mindex in active_set[3:]:
		print(mindex)
		draw_cube(ax, mindex, color=color3)

	ticks = np.array(range(max_index + 1)) + 0.5

	ax.xaxis.set_ticks(ticks)
	ax.xaxis.set_ticklabels([])


	ax.yaxis.set_ticks(ticks)
	ax.yaxis.set_ticklabels([])

	ax.zaxis.set_ticks(ticks)
	ax.zaxis.set_ticklabels([])


	ax.set_xlabel('index ' + r'$\ell_1$', labelpad=-10)
	ax.set_ylabel('index ' + r'$\ell_2$', labelpad=-10)
	ax.set_zlabel('index ' + r'$\ell_3$', labelpad=-10)

	ax.view_init(10, 10)

	tight_layout()

	#show()

	savefig('figures/sens_driven_summary_example_3D_multiindex_set.png', pad_inches=3)
	close()