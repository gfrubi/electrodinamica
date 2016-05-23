# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *

theta = linspace(0, 2*pi, 200)
fig=figure()
ax = fig.add_subplot(1, 1, 1, projection='polar') #define el subplot de la figura en proyeccion polar

colores = ['black', 'green','blue','red']
betas = [0,0.3,0.5,0.6]
for i in range(4):
	r = (sin(theta))**2/(1-betas[i]*cos(theta))**5
	ax.plot(theta, r, color=colores[i], linewidth=2.0, label=r'$\beta = $'+str(betas[i]))

ax.arrow(0, 0.05, 0, 8, linewidth=4, color='blue', head_width=0.02, head_length=0.2) 
ax.text(0.07,7, r'$\vec{a}$', fontsize=25)
ax.legend(loc='best')

# borra labels del eje radial
for tick in ax.axes.get_yticklabels():
        tick.set_visible(False)
savefig("fig-carga-relativista.pdf")

