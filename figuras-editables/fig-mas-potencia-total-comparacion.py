# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:04:20 2013

@author: gr
"""


import numpy
from scipy import integrate
from scipy.special import *
from pylab import *
from matplotlib.pyplot import *

m=numpy.array(range(1,6))
graficos=2
betas=[0.5,0.1]
colores=['ro','bs']
plt.figure()
for i in range(graficos):
    b=betas[i]
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
    plot(m,ynorm,colores[i],label='$\\beta= $'+str(betas[i])) 
legend()
axis([0.8,5.2,0,1])
grid(True)
minorticks_on()
xlabel('$m$')
ylabel('$\left\langle {P_m}\\right\\rangle $')


savefig("fig-mas-potencia-total-comparacion.svg")
