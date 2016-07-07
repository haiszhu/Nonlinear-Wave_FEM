"""
Create figure of characteristic for 11.8a.
"""

# load numpy, matplotlib commands...
from pylab import *

clf()  # clear figure

"""
plot shock position up to t*
"""
t_star = 2/(exp(2)+1)
x_star = exp(2)*t_star
plot([1, x_star],[0, t_star],'b')

"""
plot char on both sides of shock 
"""
for t in [0.5*t_star, t_star]:
    x = 1+0.5*(exp(2)-1)*t
    xr = x - t
    plot([xr, x],[0, t],'k')
    xl = x - exp(2)*t
    plot([xl, x],[0, t],'k')

"""
plot shock position after t*
"""
t = linspace(t_star, 1.5, 100)
c = x_star-2/2.45*(3*t_star)**0.8
x = 2/2.45*(3*t)**0.8+c
plot(x,t,'b')

"""
plot char along shock position after t*
"""
for t in linspace(0.5,1.5,6):
    x = 2/2.45*(3*t)**0.8+c
    plot([0, x],[0, t],'k')
    xi = x - t
    plot([xi, x],[0, t],'k')

"""
plot char on negative x axis
"""
for xi in linspace(-1.5,0,6):
    x = xi + 1.5
    plot([xi, x],[0, 1.5],'k')
"""
plot what's missing in rarefaction fan
"""
for xi in linspace(1.5,3.4,4):
    plot([0,xi],[0,1.5],'k')
"""
plot line seperate two different stages
"""
plot([-1.5,4],[t_star,t_star],'g--')

text(-1.4, t_star, r'$t^*$', fontsize=20)
xlabel('x')
ylabel('t')
ylim(0,1.5)
xlim(-1.5,4)
fname = 'problem_11_8c_char.png'
savefig(fname)
print 'Created ',fname

