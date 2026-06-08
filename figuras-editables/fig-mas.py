import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv
plt.style.use('bmh')

b = 0.5
theta = np.linspace(0, 2*np.pi, 200)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='polar') #define el subplot de la figura en proyeccion polar
for m in range(1,6):
    r = (b**2)*(m**2)*(np.tan(theta)**2)*jv(m,b*m*np.cos(theta))**2
    plt.plot(theta, r, linewidth=2.0, label='$m= $'+str(m))
rmax = ax.get_ylim()[1] # valor maximo de r en el grafico
plt.arrow(0, 0.01*rmax, 0, 0.8*rmax, linewidth=4, color='blue',head_length=0.07*rmax, head_width=3*rmax) 
plt.text(0.07,0.7*rmax, r'$\vec{a}$', fontsize=25)
plt.legend()
# borra labels del eje radial
for tick in ax.axes.get_yticklabels():
        tick.set_visible(False)
plt.savefig("fig-mas.pdf")

