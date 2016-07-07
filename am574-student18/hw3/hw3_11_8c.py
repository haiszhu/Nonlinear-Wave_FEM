"""
Create figure of characteristic for 11.8(c).
"""

# load numpy, matplotlib commands...
from pylab import *

clf()  # clear figure

"""
plot profile when second shock forms
"""
x = linspace(-1,1.8,200)
u = 2.0*exp(-(x-1.8)**2)
plot(x,u,'k')
plot([1.8,1.8],[0,2.0],'k')
plot([1.8,10],[0,0],'k')
xlim(-1,10)
ylim(-0.1,2.1)

"""
plot next time profile triple value function
"""
u = linspace(0,2,200)
x = exp(u)+1.8
plot(x,u)
arrow( 1.8, 2, exp(2)-0.1, 0, linewidth=0.03, head_width=0.05, head_length=0.1, fc='k', ec='k')
arrow( 1.8, 1.5, exp(1.5)-0.1, 0, linewidth=0.03, head_width=0.05, head_length=0.1, fc='k', ec='k')
arrow( 1.8, 1, exp(1)-0.1, 0, linewidth=0.03, head_width=0.05, head_length=0.1, fc='k', ec='k')
arrow( 1.8, 0.5, exp(0.5)-0.1, 0, linewidth=0.03, head_width=0.05, head_length=0.1, fc='k', ec='k')
plot([5.4,5.4],[0,2],'g--')


fname = 'problem_11_8c.png'
savefig(fname)
print 'Created ',fname
