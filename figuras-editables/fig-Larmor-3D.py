# coding: utf-8
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import *
from numpy import *

fig = figure()
#ax = fig.add_subplot(111, projection='3d')
ax = Axes3D(fig)
ax.set_axis_off() # desactiva ejes

t = linspace(0, pi, 100)
p = linspace(0, 2*pi-pi/2, 100)
theta,phi = meshgrid(t,p)

r= (sin(theta))**2
x = r * sin(theta) * cos(phi)
y = r * sin(theta) * sin(phi)
z = r * cos(theta)

ax.plot_surface(x, y, z, rstride=4, cstride=4, color='red', alpha=0.5)
#ax.view_init(elev=45, azim=0)
ax.quiver(0,0,0,0,0,1, length=0.7, arrow_length_ratio=0.15, pivot='tail', color='blue', linewidth=5)
ax.text(0.1,0,0.60, r'$\vec{a}$', fontsize=25)
savefig('fig-Larmor.pdf')
