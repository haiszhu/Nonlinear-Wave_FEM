"""
Compute error in elastic solution

Right now, read in data should be right (print check). Also xclaw is excutable with for loop.
Not sure whatelse to imoport. 
Error compute works

Now only need to change mx value set, and then change domain of the problem accordingly.

Getting order 1.2--1.3 for both continuous and layered case. The flux relation is exp. 
Further check for quard

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
h=[]
i = 0

#for mx in [17280, 1080, 2160, 8640]:
for mx in [ 8192, 64,128,256, 512, 1024, 2048]:
#for mx in [ 200, 100]:
#for mx in [ 360*128, 360*8, 360*16, 360*32, 360*64]:
#for mx in [ 360*64, 360*4, 360*8,  360*16, 360*32]:
#for mx in [ 1500*2**5, 1500*2, 1500*2**2, 1500*2**3, 1500*2**4]:
#for mx in [ 1500*2**4, 1500, 1500*2, 1500*2**2,1500*2**3]:
#for mx in [20, 10]:

    if i == 0:
	mx_exact = mx
    xlower = 0.000000e+00
    xupper = 1.000000e+00
    mframe = 10 
    dx = (xupper - xlower)/mx


    #Set setrun clawdata (some maybe unnecessary, will see)
    rundata=setrun.setrun('classic')

    rundata.clawdata.num_cells[0] = mx
    rundata.clawdata.num_output_times = mframe	# output_times=1 won't work for high grid resolution
    rundata.clawdata.tfinal = 0.100000e+00
    rundata.clawdata.lower[0] = xlower
    rundata.clawdata.upper[0] = xupper 
    rundata.clawdata.order = 1
    rundata.clawdata.bc_lower[0] = 'periodic'#'user'   # at xlower
    rundata.clawdata.bc_upper[0] = 'periodic'#'extrap'   # at xupper
    rundata.write()
    runclaw(xclawcmd='xclaw',outdir=outdir)	# xclaw.exe file produced after make .exe 

    #Get the material parameters
    aux = np.loadtxt(outdir+'/fort.a0000',skiprows=5)	# don't delate skiprows or set it equal 6 

    plotdata = ClawPlotData()
    plotdata.outdir=outdir

    #Read in the solution
    dat = plotdata.getframe(mframe)
    u = dat.q[0,:]

#    print u

    stress = np.exp(u*aux) - 1	# not sure why here don't need aux[0,:]
    stress = u

    #Compute parameter for error calculation
    reshape_para = mx_exact/mx

    #Compute error
    if i == 0:
	stress_exact = stress
    i = i + 1
    error = 0.0
    for j in np.linspace(0.0, mx, num=mx, endpoint=False):
	aver = np.sum(stress_exact[j*reshape_para:(j+1)*reshape_para])/reshape_para
	error = error + abs(stress[j]-aver)
#	print aver, stress_exact[j*reshape_para:j*reshape_para+reshape_para]
#    print stress_exact
#    print stress
    error = error * dx
    err.append(error)
    h.append(dx)

print err

ratio = np.zeros(len(err))
order = np.zeros(len(err))

for i in range(2,len(err)):
    ratio[i] = err[i-1]/err[i]
    order[i] = np.log(abs(ratio[i]))/np.log(abs(h[i-1]/h[i]))
#print order


from pylab import *
pl.loglog(h[1:len(err)],err[1:len(err)],'o')
pl.xlim([0.5*min(h[1:len(err)]), 1.5*max(h[1:len(err)])])
pl.ylim([0.5*min(err[1:len(err)]), 1.5*max(err[1:len(err)])])

Ap = np.ones((len(err)-1,2))
Ap[:,1] = np.log(h[1:len(err)])
bp = np.log(err[1:len(err)])
Kp = np.linalg.lstsq(Ap, bp)[0]
K = Kp[0]
p = Kp[1]
print K,p
err1 = np.exp(K)*h[1:len(err)]**p
pl.loglog(h[1:len(err)],err1, 'r')

fname = 'loglog_error.png'
savefig(fname)
print 'Created ',fname

