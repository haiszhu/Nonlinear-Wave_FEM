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

axarr.plot([0,3], [5,5], color='k',linewidth=2.0)
axarr.plot([3,6], [3,3], color='k',linewidth=2.0)
axarr.plot([6,9], [9,9], color='k',linewidth=2.0)

axarr.text(1.0, 5.5, r'$Q_{i-1}^n$', fontsize=20)
axarr.text(4.0, 3.5, r'$Q_i^n$', fontsize=20)
axarr.text(7.0, 9.5, r'$Q_{i+1}^n$', fontsize=20)
axarr.text(2.8, -0.5, r'$x_{i-1/2}$', fontsize=15)
axarr.text(4.3, -0.5, r'$x_{i}$', fontsize=15)
axarr.text(5.8, -0.5, r'$x_{i+1/2}$', fontsize=15)
axarr.text(4.0, 2.0, r'$\tilde{p}^n(\cdot,t_n)$', fontsize=15)
axarr.arrow( 4.5, 2.5, 0, 0.3, width=0.01, head_width=0.1, head_length=0.1, fc='k', ec='k')

axarr.arrow( 2.3, 4.0, 0.5, 0, width=0.01, head_width=0.2, head_length=0.2, fc='k', ec='k')
axarr.text(1.0, 4.0, r'$\frac{Q_i^n+Q_{i-1}^n}{2}$', fontsize=15)

axarr.arrow( 6.7, 6.0, -0.5, 0, width=0.01, head_width=0.2, head_length=0.2, fc='k', ec='k')
axarr.text(6.7, 6.0, r'$\frac{Q_i^n+Q_{i+1}^n}{2}$', fontsize=15)


axarr.axis('off')
axarr.set_xlim(-1,10)
axarr.set_ylim(0,10.5)

fname = 'problem_6_5b.png'
savefig(fname)
print 'Created ',fname

