"""
Create figure for 11.8a.
"""

# load numpy, matplotlib commands...
from pylab import *

clf()  # clear figure

"""
plot profile
"""
f, axarr = plt.subplots(1,2,figsize=(12,5))

axarr[ 0].plot([-4,(exp(1)-1)*1.0],[1,1],'k')
axarr[ 0].plot([(exp(1)-1)*1.0,(exp(1)-1)*1.0],[0,1],'k')
axarr[ 0].plot([(exp(1)-1)*1.0,8],[0,0],'k')
axarr[ 0].set_title('t = 1')
axarr[ 0].set_ylim(-0.1,1.1)

axarr[ 1].plot([-4,(exp(1)-1)*2.0],[1,1],'k')
axarr[ 1].plot([(exp(1)-1)*2.0,(exp(1)-1)*2.0],[0,1],'k')
axarr[ 1].plot([(exp(1)-1)*2.0,8],[0,0],'k')
axarr[ 1].set_title('t = 2')
axarr[ 1].set_ylim(-0.1,1.1)


fname = 'problem_11_8a.png'
savefig(fname)
print 'Created ',fname

