# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:41:43 2013

@author: gr
"""
from matplotlib.pyplot import *
from numpy import *
from scipy.special import *

b=0.5
theta = linspace(0, 2*pi, 200)
fig=figure()
ax = fig.add_subplot(1, 1, 1, projection='polar') #define el subplot de la figura en proyeccion polar
for m in range(1,6):
    r = (b**2)*(m**2)*(tan(theta)**2)*jv(m,b*m*cos(theta))**2
    ax.plot(theta, r, linewidth=2.0, label='m='+str(m))
legend()
# borra labels del eje radial
for tick in ax.axes.get_yticklabels():
        tick.set_visible(False)
savefig("fig-mas-raw.svg")

