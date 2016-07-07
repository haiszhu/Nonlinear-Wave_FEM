"""
Create figure of characteristic for 11.8a.
"""

# load numpy, matplotlib commands...
from pylab import *

clf()  # clear figure

"""
plot shock position
"""
plot([0, (exp(1)-1)*4], [0, 4])

for t in range(1, 5):
    x = (exp(1)-1)*t
    xr = x - t
    plot([xr, x],[0, t],'k')
    xl = x - exp(1)*t
    plot([xl, x],[0, t],'k')
xlabel('x')
ylabel('t')
fname = 'problem_11_8a_char.png'
savefig(fname)
print 'Created ',fname

