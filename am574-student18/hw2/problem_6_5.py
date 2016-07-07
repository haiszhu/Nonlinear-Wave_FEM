"""
Create figure to accompany problem 4.2.
"""

# load numpy, matplotlib commands...
from pylab import *

clf()  # clear figure

f, axarr = plt.subplots(1,figsize=(8,4))

axarr.plot([0,0], [0,10], color='k',linewidth=0.5)
axarr.plot([3,3], [0,10], color='k',linewidth=0.5)
axarr.plot([6,6], [0,10], color='k',linewidth=0.5)
axarr.plot([9,9], [0,10], color='k',linewidth=0.5)

axarr.plot([0,3], [3,3], color='k',linewidth=2.0)
axarr.plot([3,6], [5,5], color='k',linewidth=2.0)
axarr.plot([6,9], [9,9], color='k',linewidth=2.0)

axarr.plot([3,6], [4,6], '--', color='k',linewidth=1.0)

axarr.text(1.0, 2.0, r'$Q_{i-1}^n$', fontsize=20)
axarr.text(4.0, 4.0, r'$Q_i^n$', fontsize=20)
axarr.text(7.0, 8.0, r'$Q_{i+1}^n$', fontsize=20)
axarr.text(2.8, -0.5, r'$x_{i-1/2}$', fontsize=15)
axarr.text(4.3, -0.5, r'$x_{i}$', fontsize=15)
axarr.text(5.8, -0.5, r'$x_{i+1/2}$', fontsize=15)
axarr.text(4.5, 6.0, r'$\tilde{p}^n(\cdot,t_n)$', fontsize=15)

axarr.arrow( 2.3, 4.0, 0.5, 0, width=0.01, head_width=0.2, head_length=0.2, fc='k', ec='k')
axarr.text(1.0, 4.0, r'$\frac{Q_i^n+Q_{i-1}^n}{2}$', fontsize=15)

axarr.arrow( 6.7, 7.0, -0.5, 0, width=0.01, head_width=0.2, head_length=0.2, fc='k', ec='k')
axarr.text(6.7, 6.8, r'$\frac{Q_i^n+Q_{i+1}^n}{2}$', fontsize=15)


axarr.axis('off')
axarr.set_xlim(-1,10)
axarr.set_ylim(0,10.5)

fname = 'problem_6_5.png'
savefig(fname)
print 'Created ',fname

