"""
Create figure of characteristic for 11.8b.
"""

# load numpy, matplotlib commands...
from pylab import *

clf()  # clear figure

"""
plot rarefaction fan
"""
xrare = linspace(1, exp(1), 5)
for i in range(0, 5):
    plot([0, xrare[i]],[0, 1],'b')
for x in range(1, 4):
    plot([x, x+exp(1)],[0, 1],'k')
for x in range(-3, 0):
    plot([x, x+1],[0, 1],'k')

xlim(-3,4)
xlabel('x')
ylabel('t')
fname = 'problem_11_8b_char.png'
savefig(fname)
print 'Created ',fname

