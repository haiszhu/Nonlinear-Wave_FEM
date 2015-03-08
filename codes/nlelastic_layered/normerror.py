"""
Compute error in elastic solution

Right now, read in data seems working. Also xclaw is excutable with for loop
Not sure whatelse to imoport. 
Need to find a way to output result.
Need to compute 'exact' solution, and compute L1 norm of error.

"""

import numpy as np
import matplotlib.pyplot as pl
from clawpack.clawutil.runclaw import runclaw	# find the right place of runclaw
from clawpack.visclaw.data import ClawPlotData	# find the right place of ClawPlotData
import setrun

reload(setrun)

outdir='./_output'
frame=1
err=[]

#for mx in [200,400,800,1600,3200]:
for mx in [200,400]:
    #Set setrun clawdata (some maybe unnecessary, will see)
    rundata=setrun.setrun('classic')
    rundata.clawdata.num_cells[0]=mx
    rundata.clawdata.num_output_times=1		# only produce final results for error computation
    rundata.clawdata.tfinal=4.0000e+02
    rundata.write()
    runclaw(xclawcmd='xclaw',outdir=outdir)	# xclaw.exe file produced after make .exe 

    #Get the material parameters
    aux = np.loadtxt(outdir+'/fort.a0001',skiprows=5)	# don't delate skiprows or set it equal 6 

    plotdata = ClawPlotData()
    plotdata.outdir=outdir

    #Read in the solution
    dat = plotdata.getframe(frame)
    u = dat.q[0,:]

    stress = np.exp(u*aux) - 1	# not sure why here don't need aux[0,:]

