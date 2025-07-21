import matplotlib.pyplot as plt
import numpy as np
plt.style.use('bmh')

theta = np.linspace(0, 2*np.pi, 200)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='polar') #define el subplot de la figura en proyeccion polar
r = 0.5*(1+np.cos(theta)**2)
ax.plot(theta, r, color='red', linewidth=2.0)
ax.text(0.07,1.12, r'$\theta$', fontsize=25)


# borra labels del eje radial
for tick in ax.axes.get_yticklabels():
        tick.set_visible(False)
plt.savefig("fig-Thomson.pdf")

