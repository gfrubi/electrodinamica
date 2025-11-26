import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.special import jv
plt.style.use('bmh')

m = np.arange(1,6)
betas = [0.5,0.1]
colores = ['ro','bs']
plt.figure()
for b,c in zip(betas,colores):
# se define el resultado de la integral, para cada m como una función
    def f(m):
            f = lambda theta: (b**2)*m**2*(np.tan(theta)**2)*jv(m,b*m*np.cos(theta))**2*np.sin(theta)
            return integrate.quad(f, 0, np.pi)[0] # calcula la integral, usando el método de cuadraturas
    # calcula la integral para toda la lista de valores de m
    f_vec = np.vectorize(f) # versión vectorizada
    y = f_vec(m)
    ynorm = y/np.sum(y) # normaliza la integral, dividiendo por la suma sobre todos los m's
    #grafica 
    plt.plot(m,ynorm,c,label='$\\beta= $'+str(b), markersize=4) 
plt.legend()
plt.xlim(0.8,5.2)
plt.ylim(0,1.2)
#plt.yscale('log')
plt.grid(True)
plt.minorticks_on()
plt.xlabel('$m$', fontsize=15)
plt.ylabel('$\\left\\langle {P_m}\\right\\rangle /\\left\\langle {P}\,\\right\\rangle $',  fontsize=15)
plt.savefig("fig-mas-potencia-total-comparacion.pdf")
