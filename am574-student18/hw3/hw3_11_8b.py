"""
Create figure for 11.8a.
"""

# load numpy, matplotlib commands...
from pylab import *

clf()  # clear figure

"""
plot profile
"""
f, axarr = plt.subplots(2,2,figsize=(12,10))

axarr[0, 0].plot([-4, 0],[0, 0],'k')
axarr[0, 0].plot([0, 0],[0, 1],'k')
axarr[0, 0].plot([0, 8],[1, 1],'k')
axarr[0, 0].set_title('t = 0')
axarr[0, 0].set_ylim(-0.1,1.1)

axarr[0, 1].plot([-4,0.5],[0, 0],'k')
axarr[0, 1].plot([exp(1)*0.5, 8],[1, 1],'k')
x = linspace(0.5,exp(1)*0.5,100)
y = log(2*x)
axarr[0, 1].plot(x,y,'k')
axarr[0, 1].set_title('t = 0.5')
axarr[0, 1].set_ylim(-0.1,1.1)

axarr[1, 0].plot([-4,1],[0, 0],'k')
axarr[1, 0].plot([exp(1), 8],[1, 1],'k')
x = linspace(1,exp(1),100)
y = log(x)
axarr[1, 0].plot(x,y,'k')
axarr[1, 0].set_title('t = 1')
axarr[1, 0].set_ylim(-0.1,1.1)

axarr[1, 1].plot([-4,2],[0, 0],'k')
axarr[1, 1].plot([exp(1)*2.0, 8],[1, 1],'k')
x = linspace(2.0,exp(1)*2.0,100)
y = log(0.5*x)
axarr[1, 1].plot(x,y,'k')
axarr[1, 1].set_title('t = 2')
axarr[1, 1].set_ylim(-0.1,1.1)

fname = 'problem_11_8b.png'
savefig(fname)
print 'Created ',fname

