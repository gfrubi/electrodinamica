# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:56:14 2013

@author: gr
"""

import numpy
from scipy import integrate
from scipy.special import *
from pylab import *

b=0.5
m=numpy.array(range(1,6))
plt.figure()
# se define el resultado de la integral, para cada m como una función
def f(m):
        f=lambda theta: (b**2)*m**2*(tan(theta)**2)*jv(m,b*m*cos(theta))**2*sin(theta)
# calcula la integral, usando el método de cuadraturas
        return integrate.quad(f, 0, pi)[0]
# calcula la integral para toda la lista de valores de m
y=numpy.array(map(f,m))
# normaliza la integral, dividiendo por la suma sobre todos los m's
ynorm=y/numpy.sum(y)
#grafica 
plot(m,ynorm,'ro')
axis([0.8,5.2,0,1])
grid(True)
minorticks_on()
xlabel('$m$')
ylabel('$\left\langle {P_m}\\right\\rangle $')
savefig("fig-mas-potencia-total-raw.svg")

