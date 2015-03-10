
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

#--------------------------
def setplot(plotdata):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of clawpack.visclaw.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 


    plotdata.clearfigures()  # clear any old figures,axes,items data

    # Figure for q[0]
    plotfigure = plotdata.new_plotfigure(name='Strain', figno=1)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.axescmd = 'subplot(1,1,1)'   # top figure
    plotaxes.xlimits = 'auto'#[0,30]
    plotaxes.ylimits = [-5,5]
    #plotaxes.title = 'strain'
    plotaxes.title = 'stress'

    #def movingframe(current_data):
    # 	if (current_data.t>80):
    #		plotaxes.xlimits = [(current_data.t-80)*240/320,(current_data.t-80)*240/320+120]
    #plotaxes.afteraxes = movingframe
    

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')

    # plotitem.plot_var = 0
    def Stress(current_data):
	from numpy import exp
	# make sure q and K have same dimension
        q = current_data.q
	K = current_data.aux
	Stress = exp(q[0,:]*K[0,:]) - 1 
	#Stress = K[0,:]
	return Stress

    plotitem.plot_var = Stress
    plotitem.plotstyle = '-'
    plotitem.color = 'b'

    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via clawpack.visclaw.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

    
