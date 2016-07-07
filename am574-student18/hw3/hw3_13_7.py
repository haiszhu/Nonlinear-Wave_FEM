"""
Create figure of characteristic for 13.7(d)(i).
"""

# load numpy, matplotlib commands...
from pylab import *

clf()  # clear figure

def plot_HL(v_star, u_star):
    """
    plot positive part
    """
    n = 200
    v = linspace(-3, 5, n)
    u = u_star + (-(exp(v_star)-exp(v))/(v-v_star))**0.5*(v-v_star)
    plot(v, u, 'b',label='positive')
    legend(loc='upper right')
    """
    plot negative part
    """
    u = u_star - (-(exp(v_star)-exp(v))/(v-v_star))**0.5*(v-v_star)
    plot(v, u, 'k',label='negative')
    legend(loc='upper right')
    title('Hugoniot loci')

plot_HL(1, 1)

fname = 'problem_13_7.png'
savefig(fname)
print 'Created ',fname
