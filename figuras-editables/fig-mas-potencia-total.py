# -*- coding: utf-8 -*-

from numpy import *
from scipy import integrate
from scipy.special import jv
from matplotlib.pyplot import *


# se define el resultado de la integral, para cada m como una función
def f(m):
        f=lambda theta: (b**2)*m**2*(tan(theta)**2)*jv(m,b*m*cos(theta))**2*sin(theta)
        return integrate.quad(f, 0, pi)[0]
fv=vectorize(f)

b=0.5
m=arange(1,6)
y=fv(m)
# normaliza la integral, dividiendo por la suma sobre todos los m's
ynorm=y/sum(y)
#grafica 
figure()
plot(m,ynorm,'ro')
axis([0.8,5.2,0,1])
grid()
minorticks_on()
xlabel('$m$')
ylabel('$\left\langle {P_m}\\right\\rangle $')
savefig("fig-mas-potencia-total-raw.svg")

