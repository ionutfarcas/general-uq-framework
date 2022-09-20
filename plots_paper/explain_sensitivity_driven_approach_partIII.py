from matplotlib import patches, pyplot as plt
import numpy as np


def draw_arrow(xyA, xyB, ax1, ax2):

    transFigure = fig.transFigure.inverted()
    coord1 = transFigure.transform(ax1.transData.transform(xyA))
    coord2 = transFigure.transform(ax2.transData.transform(xyB))
    arrow = patches.FancyArrowPatch(
        coord1,  # posA
        coord2,  # posB
        shrinkA=0,  # so tail is exactly on posA (default shrink is 2)
        shrinkB=0,  # so head is exactly on posB (default shrink is 2)
        transform=fig.transFigure,
        color="black",
        arrowstyle="-|>",  # "normal" arrow
        mutation_scale=5,  # controls arrow head size
        linewidth=0.5,
        label='some arrow',
    )
    fig.patches.append(arrow)



if __name__ == '__main__':

    plt.rc("figure", dpi=400)           # High-quality figure ("dots-per-inch")
    # plt.rc("text", usetex=True)         # Crisp axis ticks
    plt.rc("font", family="serif")      # Crisp axis labels
    # plt.rc("legend", edgecolor='none')  # No boxes around legends
    # plt.rcParams["figure.figsize"] = (6, 3)
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
    color1 = '#e66101'
    color2 = '#b2abd2'
    color3 = '#5e3c99'


    fig = plt.figure()

    # First subplot
    ax3 = fig.add_subplot(121, aspect='equal')
    ax4 = fig.add_subplot(122, aspect='equal')




    ax3.spines['left'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['top'].set_visible(False)
    ax3.spines['bottom'].set_visible(False)

    ax3.axes.xaxis.set_visible(False)
    ax3.axes.yaxis.set_visible(False)


    ax4.spines['left'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.spines['top'].set_visible(False)
    ax4.spines['bottom'].set_visible(False)

    ax4.axes.xaxis.set_visible(False)
    ax4.axes.yaxis.set_visible(False)
   

    textstr = 'postprocessing'
    props   = dict(boxstyle='round', facecolor='tan', alpha=0.5)

    ax3.text(0.6, 0.5, textstr, transform=ax3.transAxes,
            verticalalignment='center', bbox=props)

    # UQ
    textstr = 'uncertainty quantification' + '\n' + r'$\mathbb{E}[y_{\mathrm{hi-fi}}], \mathrm{Var}[y_{\mathrm{hi-fi}}], ...$'
    props   = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    ax4.text(0.0, 0.75, textstr, transform=ax4.transAxes,
            verticalalignment='center', bbox=props, fontsize=6)

    # SA
    # xyA = [0.90, 0.5]
    # xyB = [0.1, 0.5]
    # draw_arrow(xyA, xyB, ax2, ax4)

    textstr = 'sensitivity analysis' + '\n' + r'$S_{\theta_1}, S_{\theta_2}, S_{\theta_3}, S_{\theta_1, \theta_2}, ...$'
    props   = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    ax4.text(0.00, 0.5, textstr, transform=ax4.transAxes,
            verticalalignment='center', bbox=props, fontsize=6)


    # reduced model
    # xyA = [0.90, 0.5]
    # xyB = [0.1, 0.30]
    # draw_arrow(xyA, xyB, ax2, ax4)

    textstr = 'reduced model' + '\n' + r'$y_{\mathrm{SG}}(\theta_1, \theta_2, \theta_3)$'
    props   = dict(boxstyle='round', facecolor='lavender', alpha=0.5)

    ax4.text(0.00, 0.25, textstr, transform=ax4.transAxes,
            verticalalignment='center', bbox=props, fontsize=6)


    # xyA = [0.65, 0.3]
    # xyB = [0.8, 0.35]
    # draw_arrow(xyA, xyB, ax4, ax4)

    textstr = 'optimization'
    props   = dict(boxstyle='round', facecolor='lavender', alpha=0.0)

    ax4.text(-0.6, -0.1, textstr, transform=ax4.transAxes,
            verticalalignment='center', bbox=props, fontsize=6)


    # xyA = [0.65, 0.3]
    # xyB = [0.8, 0.3]
    # draw_arrow(xyA, xyB, ax4, ax4)

    textstr = 'multi-fidelity modeling'
    props   = dict(boxstyle='round', facecolor='lavender', alpha=0.0)

    ax4.text(-0.1, -0.1, textstr, transform=ax4.transAxes,
            verticalalignment='center', bbox=props, fontsize=6)


    # xyA = [0.65, 0.3]
    # xyB = [0.8, 0.25]
    # draw_arrow(xyA, xyB, ax4, ax4)

    textstr = '...'
    props   = dict(boxstyle='round', facecolor='lavender', alpha=0.0)

    ax4.text(0.7, -0.1, textstr, transform=ax4.transAxes,
            verticalalignment='center', bbox=props, fontsize=6)



   

    # plt.tight_layout()

    plt.show()

    # plt.savefig('figures/sens_driven_summary.png', pad_inches=3)
    # plt.close()

    fig_name = 'figures/sens_driven_summary_partIII.pdf'
    fig.savefig(fig_name, format="pdf", bbox_inches='tight')