import matplotlib.pyplot as plt
import numpy as np
plt.style.use('bmh')

theta = np.linspace(0, 2*np.pi, 200)
plt.subplot(1, 1, 1, projection='polar') #define el subplot de la figura en proyeccion polar
r1 = 0.5*(1+np.cos(theta)**2)
plt.plot(theta, r1, color='red', linewidth=2.0)
plt.text(0.07,1.12, r'$\theta$', fontsize=25)
plt.legend(fontsize=7)
plt.yticks([0.2,0.4,0.6,0.8,1],['','','','',''])
plt.savefig("fig-Thomson.pdf")
plt.show()

