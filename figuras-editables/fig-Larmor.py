# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *
from scipy.special import *

theta = linspace(0, 2*pi, 200)
fig=figure()
ax = fig.add_subplot(1, 1, 1, projection='polar') #define el subplot de la figura en proyeccion polar
r = (sin(theta))**2
ax.plot(theta, r, color='red', linewidth=2.0)
ax.arrow(0, 0.05, 0, 0.8, linewidth=4, color='blue', head_width=0.04) 
ax.text(0.07,0.7, r'$\vec{a}$', fontsize=25)


# borra labels del eje radial
for tick in ax.axes.get_yticklabels():
        tick.set_visible(False)
savefig("fig-Larmor.pdf")

