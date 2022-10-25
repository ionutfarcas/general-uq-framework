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
    plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica"})
    plt.rc('text.latex', preamble=r'\usepackage{amssymb, bm, upgreek}')
    plt.rcParams.update({'font.size': 8})
    plt.rcParams["figure.figsize"] = (5, 5)

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
    ax1 = fig.add_subplot(121, aspect='equal')
    ax2 = fig.add_subplot(122, aspect='equal')
    #ax3 = fig.add_subplot(133, aspect='equal')


    ax1.spines['left'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)

    ax1.axes.xaxis.set_visible(False)
    ax1.axes.yaxis.set_visible(False)


    ax2.spines['left'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)

    ax2.axes.xaxis.set_visible(False)
    ax2.axes.yaxis.set_visible(False)

    # ax3.spines['left'].set_visible(False)
    # ax3.spines['right'].set_visible(False)
    # ax3.spines['top'].set_visible(False)
    # ax3.spines['bottom'].set_visible(False)

    # ax3.axes.xaxis.set_visible(False)
    # ax3.axes.yaxis.set_visible(False)

    
    # arrow sparse grid -> hi-fi model
    xyA = [1.0, 0.5]
    xyB = [0.28, 0.5]
    # draw_arrow(xyA, xyB, ax1, ax1)

    
    # hi-fi model
    textstr = 'perform high-fidelity simulation ' + r'$f_{\mathrm{hi-fi}}(\boldsymbol{\uptheta}_{n + 1})$'
    props   = dict(boxstyle='round', facecolor=color3, alpha=0.4)

    ax1.text(0.05, 0.8, textstr, transform=ax1.transAxes,
            verticalalignment='center', bbox=props)


    # hi-fi model
    textstr = 'perform high-fidelity simulation '  + r'$f_{\mathrm{hi-fi}}(\boldsymbol{\uptheta}_{n + 2})$'
    props   = dict(boxstyle='round', facecolor=color3, alpha=0.4)

    ax1.text(0.05, 0.5, textstr, transform=ax1.transAxes,
            verticalalignment='center', bbox=props)

    # hi-fi model
    textstr = 'perform high-fidelity simulation '  + r'$f_{\mathrm{hi-fi}}(\boldsymbol{\uptheta}_{n + 3})$'
    props   = dict(boxstyle='round', facecolor=color3, alpha=0.4)

    ax1.text(0.05, 0.2, textstr, transform=ax1.transAxes,
            verticalalignment='center', bbox=props)

    # arrow hi-fi model -> UQ
    # xyA = [0.90, 0.5]
    # xyB = [0.1, 0.70]
    # draw_arrow(xyA, xyB, ax2, ax4)
    
    # hi-fi model

    textstr = 'compute output of interest ' + r'$y_{\mathrm{hi-fi}}(\boldsymbol{\uptheta}_{n + 1})$'
    props   = dict(boxstyle='round', facecolor=color3, alpha=0.4)

    ax2.text(0.3, 0.8, textstr, transform=ax2.transAxes,
            verticalalignment='center', bbox=props)

    textstr = 'compute output of interest ' + r'$y_{\mathrm{hi-fi}}(\boldsymbol{\uptheta}_{n + 2})$'
    props   = dict(boxstyle='round', facecolor=color3, alpha=0.4)

    ax2.text(0.3, 0.5, textstr, transform=ax2.transAxes,
            verticalalignment='center', bbox=props)

    textstr = 'compute output of interest ' + r'$y_{\mathrm{hi-fi}}(\boldsymbol{\uptheta}_{n + 3})$'
    props   = dict(boxstyle='round', facecolor=color3, alpha=0.4)

    ax2.text(0.3, 0.2, textstr, transform=ax2.transAxes,
            verticalalignment='center', bbox=props)

    ####
    
    # textstr = 'postprocessing'
    # props   = dict(boxstyle='round', facecolor='mintcream', alpha=0.5)

    # ax3.text(0.8, 0.5, textstr, transform=ax3.transAxes,
    #         verticalalignment='center', bbox=props)

    
 

    plt.tight_layout()

    # plt.show()

    # plt.savefig('figures/sens_driven_summary.png', pad_inches=3)
    # plt.close()

    fig_name = 'figures/sens_driven_summary_partI.png'
    fig.savefig(fig_name, bbox_inches='tight')
    plt.close()