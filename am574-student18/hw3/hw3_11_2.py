"""
Create sketch of 11.2.
"""

# load numpy, matplotlib commands...
from pylab import *

clf()  # clear figure

def plot_w(ul, ur, epsilon):
    """
    plot profile of w
    """
    n = 200
    xi = linspace(-10, 10, n)
    w = ur + 1.0/2.0*(ul-ur)*(1.0 - tanh(((ul-ur)*xi)/(4.0*epsilon)))
    plot(xi, w, 'k')

plot_w(4, 0, 1.0)
plot_w(4, 0, 0.3)
plot_w(4, 0, 0.000001)

ylim(-0.2,4.2)

fname = 'problem_11_2.png'
savefig(fname)
print 'Created ',fname

