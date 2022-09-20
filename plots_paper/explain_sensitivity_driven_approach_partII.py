from matplotlib import patches, pyplot as plt
import numpy as np



if __name__ == '__main__':

    plt.rc("figure", dpi=400)           # High-quality figure ("dots-per-inch")
    # plt.rc("text", usetex=True)         # Crisp axis ticks
    plt.rc("font", family="serif")      # Crisp axis labels
    # plt.rc("legend", edgecolor='none')  # No boxes around legends
    # plt.rcParams["figure.figsize"] = (8, 6)
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
    ax1 = fig.add_subplot(111, aspect='equal')
    
    ax1.spines['left'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)

    ax1.axes.xaxis.set_visible(False)
    ax1.axes.yaxis.set_visible(False)


 
    # hi-fi model
    textstr = 'continue refinement?'
    props   = dict(boxstyle='round', facecolor='coral', alpha=0.5)

    ax1.text(0.1, 0.4, textstr, transform=ax1.transAxes,
            verticalalignment='center', bbox=props, fontsize=5)

  
 

    textstr = 'compute sensitivity scores'
    props   = dict(boxstyle='round', facecolor='tan', alpha=0.5)

    ax1.text(0.05, 0.25, textstr, transform=ax1.transAxes,
            verticalalignment='center', bbox=props, fontsize=5)
    
    # plt.tight_layout()

    plt.show()

    # plt.savefig('figures/sens_driven_summary.png', pad_inches=3)
    # plt.close()

    fig_name = 'figures/sens_driven_summary_partII.pdf'
    fig.savefig(fig_name, format="pdf", bbox_inches='tight')