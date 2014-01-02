# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:41:43 2013

@author: gr
"""
from matplotlib.pyplot import *
from numpy import *
from scipy.special import *

theta = linspace(0, 2*pi, 200)
fig=figure()
ax = fig.add_subplot(1, 1, 1, polar=True)
#matplotlib.pyplot.figure()
r1 = (cos(pi*cos(theta)/2)/sin(theta))**2
r2 = sin(theta)**2
ax.plot(theta, r1, lw=2.0, label='antena $\\lambda/2$')
ax.plot(theta, r2, lw=2.0, label='$\\sin^2\\theta$')
legend(loc=5)
# borra labels del eje radial
for tick in ax.axes.get_yticklabels():
        tick.set_visible(False)
#savefig("fig-antena-media-onda.svg")
show()