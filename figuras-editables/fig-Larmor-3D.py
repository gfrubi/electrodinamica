from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)
ax.set_axis_off() # desactiva ejes

t = np.linspace(0, np.pi, 100)
p = np.linspace(0, 2*np.pi-np.pi/2, 100)
theta, phi = np.meshgrid(t,p)

r = (np.sin(theta))**2
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

ax.plot_surface(x, y, z, rstride=4, cstride=4, color='red', alpha=0.5)
#ax.view_init(elev=45, azim=0)
ax.quiver(0,0,0,0,0,1, length=0.7, arrow_length_ratio=0.15, pivot='tail', color='blue', linewidth=5)
ax.text(0.1,0,0.60, r'$\vec{a}$', fontsize=25)
#plt.savefig('fig-Larmor.pdf')
plt.show()