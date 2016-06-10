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
    ax.plot(theta, r, linewidth=2.0, label='$m= $'+str(m))
rmax=ax.get_ylim()[1] # valor maximo de r en el grafico
ax.arrow(0, 0.01*rmax, 0, 0.8*rmax, linewidth=4, color='blue',head_length=0.07*rmax, head_width=3*rmax) 
ax.text(0.07,0.7*rmax, r'$\vec{a}$', fontsize=25)
legend()
# borra labels del eje radial
for tick in ax.axes.get_yticklabels():
        tick.set_visible(False)
savefig("fig-mas.pdf")

