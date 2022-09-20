import numpy as np
import matplotlib.pyplot as plt

color1 = '#d95f02'
color2 = '#1b9e77'
color3 = '#7570b3'


plt.rc("figure", dpi=400)           # High-quality figure ("dots-per-inch")
# plt.rc("text", usetex=True)         # Crisp axis ticks
plt.rc("font", family="serif") 


colors = [color3, color2, color1]
f = lambda m,c: plt.plot([],[],marker=m, color=c, ls="none")[0]
handles = [f("s", colors[i]) for i in range(len(colors))]
labels = ['subspaces added upon refinement', 'subspaces active set', 'subspaces old-index set']
legend = plt.legend(handles, labels, loc=3, ncol=1, framealpha=1, frameon=False)

for i, text in enumerate(legend.get_texts()):
    text.set_color(colors[i])

def export_legend(legend, filename="figures/sens_driven_summary_example_legend.png", expand=[-5,-5,5,5]):
    fig  = legend.figure
    fig.canvas.draw()
    bbox  = legend.get_window_extent()
    bbox = bbox.from_extents(*(bbox.extents + np.array(expand)))
    bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(filename, dpi="figure", bbox_inches=bbox)

export_legend(legend)
plt.show()