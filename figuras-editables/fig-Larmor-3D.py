# coding: utf-8

from mayavi.mlab import *
from numpy import *

theta, phi = mgrid[0:pi:101j, 0:2 * pi:101j]
r= (sin(theta))**2
x = r * sin(theta) * cos(phi)
y = r * sin(theta) * sin(phi)
z = r * cos(theta)

options.offscreen = True #desabilita la ventana interactiva
s=1
mesh(x, y, z, color = (0,0,1)) # color azul
view(45,45)
savefig('test.png')
show()
