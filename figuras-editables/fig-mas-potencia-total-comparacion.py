# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:04:20 2013

@author: gr
"""


from numpy import *
from scipy import integrate
from scipy.special import jv
from matplotlib.pyplot import *

m = array(range(1,6))
graficos = 2
betas = [0.5,0.1]
colores = ['ro','bs']
figure()
for i in range(graficos):
    b=betas[i]
# se define el resultado de la integral, para cada m como una función
    def f(m):
            f=lambda theta: (b**2)*m**2*(tan(theta)**2)*jv(m,b*m*cos(theta))**2*sin(theta)
            # calcula la integral, usando el método de cuadraturas
            return integrate.quad(f, 0, pi)[0]
    # calcula la integral para toda la lista de valores de m
    y = array(map(f,m))
    # normaliza la integral, dividiendo por la suma sobre todos los m's
    ynorm = y/sum(y)
    #grafica 
    plot(m,ynorm,colores[i],label='$\\beta= $'+str(betas[i])) 
legend()
xlim(0.8,5.2)
ylim(0,1.2)
grid(True)
minorticks_on()
xlabel('$m$', fontsize=15)
ylabel('$\left\langle {P_m}\\right\\rangle $',  fontsize=15)
savefig("fig-mas-potencia-total-comparacion.pdf")
