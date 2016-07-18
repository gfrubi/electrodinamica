# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *
from scipy.special import *

theta = linspace(0, 2*pi, 200)
fig=figure()
ax = fig.add_subplot(1, 1, 1, projection='polar') #define el subplot de la figura en proyeccion polar
r = 0.5*(1+cos(theta)**2)
ax.plot(theta, r, color='red', linewidth=2.0)
ax.text(0.07,1.12, r'$\theta$', fontsize=25)


# borra labels del eje radial
for tick in ax.axes.get_yticklabels():
        tick.set_visible(False)
savefig("fig-Thomson.pdf")

