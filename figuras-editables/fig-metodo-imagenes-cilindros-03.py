from numpy import *
from matplotlib.pyplot import *

n=21
maxi=2
x,y = meshgrid(linspace(-maxi,maxi,n),linspace(-maxi,maxi,n))

# Se definen las componentes del campo
Ex=-(x+1)/((x+1)**2+y**2)+(x-1)/((x-1)**2+y**2)
Ey=-(y)/((x+1)**2+y**2)+(y)/((x-1)**2+y**2)
E=sqrt(Ex**2+Ey**2)

n=500
maxi=2
x2,y2 = meshgrid(linspace(-maxi,maxi,n),linspace(-maxi,maxi,n))

phi=log(((x2+1)**2+y2**2)/((x2-1)**2+y2**2))

# Grafico
figure(figsize=(7,7))
quiver(x,y,Ex/E,Ey/E, color='blue',pivot='middle',scale=40)
contour(x2,y2,phi,0,colors='grey',linewidths=3, linestyles='-')
contourf(x2,y2,phi,levels=[3,500],colors='grey')
contourf(x2,y2,phi,levels=[-3,-500],colors='grey')
xlim(-maxi*1.1,maxi*1.1)
ylim(-maxi*1.1,maxi*1.1)
axis('off')
savefig('fig-metodo-imagenes-cilindros-03.svg')

