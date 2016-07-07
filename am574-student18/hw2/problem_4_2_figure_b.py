"""
Create figure to accompany problem 4.2.
"""

# load numpy, matplotlib commands...
from pylab import *

clf()  # clear figure

f, axarr = plt.subplots(3,1,figsize=(5,8))

axarr[0].plot([0,0], [0,10], color='k',linewidth=0.5)
axarr[0].plot([3,3], [0,10], color='k',linewidth=0.5)
axarr[0].plot([6,6], [0,10], color='k',linewidth=0.5)
axarr[0].plot([9,9], [0,10], color='k',linewidth=0.5)

axarr[0].plot([0,1], [9,9], color='k',linewidth=2.0)
axarr[0].plot([1,1], [9,7], color='k',linewidth=2.0)
axarr[0].plot([1,4], [7,7], color='k',linewidth=2.0)
axarr[0].plot([4,4], [7,3], color='k',linewidth=2.0)
axarr[0].plot([4,7], [3,3], color='k',linewidth=2.0)
axarr[0].plot([7,7], [3,4], color='k',linewidth=2.0)
axarr[0].plot([7,9], [4,4], color='k',linewidth=2.0)

axarr[0].arrow( 3, 8, -1.5, 0, width=0.01, head_width=0.2, head_length=0.2, fc='k', ec='k')
axarr[0].arrow( 6, 5, -1.5, 0, width=0.01, head_width=0.2, head_length=0.2, fc='k', ec='k')
axarr[0].arrow( 9, 3.5, -1.5, 0, width=0.01, head_width=0.2, head_length=0.2, fc='k', ec='k')

axarr[0].axis('off')
axarr[0].set_xlim(-1,10)
axarr[0].set_ylim(0,10.5)




axarr[1].plot([0,0], [0,3], color='k',linewidth=0.5)
axarr[1].plot([3,3], [0,3], color='k',linewidth=0.5)
axarr[1].plot([6,6], [0,3], color='k',linewidth=0.5)
axarr[1].plot([9,9], [0,3], color='k',linewidth=0.5)
axarr[1].plot([-1,10], [0,0], color='k',linewidth=0.5)
axarr[1].plot([-1,10], [2.6,2.6], color='k',linewidth=0.5)

axarr[1].arrow( 3, 0, -2.8, 2.4, width=0.01, head_width=0.2, head_length=0.2, fc='k', ec='k')
axarr[1].arrow( 6, 0, -2.8, 2.4, width=0.01, head_width=0.2, head_length=0.2, fc='k', ec='k')
axarr[1].arrow( 9, 0, -2.8, 2.4, width=0.01, head_width=0.2, head_length=0.2, fc='k', ec='k')

axarr[1].text(-0.7, 0.1, r'$t_n$', fontsize=15)
axarr[1].text(-1.1, 2.8, r'$t_{n+1}$', fontsize=15)
axarr[1].text(2.8, -0.4, r'$x_{i-1/2}$', fontsize=20)
axarr[1].text(5.8, -0.4, r'$x_{i+1/2}$', fontsize=20)
axarr[1].text(1.0, 1.0, r'$W_{i-1/2}$', fontsize=20)

axarr[1].axis('off')
axarr[1].set_xlim(-1,10)
axarr[1].set_ylim(-1,3.5)





axarr[2].plot([0,0], [0,10], color='k',linewidth=0.5)
axarr[2].plot([3,3], [0,10], color='k',linewidth=0.5)
axarr[2].plot([6,6], [0,10], color='k',linewidth=0.5)
axarr[2].plot([9,9], [0,10], color='k',linewidth=0.5)

axarr[2].plot([-1,0], [9,9], color='k',linewidth=2.0)
axarr[2].plot([0,0], [9,8], color='k',linewidth=2.0)
axarr[2].plot([0,3], [8,8], color='k',linewidth=2.0)
axarr[2].plot([3,3], [8,6], color='k',linewidth=2.0)
axarr[2].plot([3,6], [6,6], color='k',linewidth=2.0)
axarr[2].plot([6,6], [6,1], color='k',linewidth=2.0)
axarr[2].plot([6,9], [1,1], color='k',linewidth=2.0)
axarr[2].plot([9,9], [1,2], color='k',linewidth=2.0)
axarr[2].plot([9,10], [2,2], color='k',linewidth=2.0)

axarr[2].text(1.0, 8.5, r'$Q_{i-1}^n$', fontsize=20)
axarr[2].text(4.0, 6.5, r'$Q_{i}^n$', fontsize=20)
axarr[2].text(7.0, 1.5, r'$Q_{i+1}^n$', fontsize=20)

axarr[2].axis('off')
axarr[2].set_xlim(-1,10)
axarr[2].set_ylim(-1,10)



fname = 'problem_4_2_figure_b.png'
savefig(fname)
print 'Created ',fname

