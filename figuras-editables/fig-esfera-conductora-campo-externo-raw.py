from numpy import *
from matplotlib.pyplot import *

n=21 # numero de nodos por eje
maxi=3
X=linspace(-maxi,maxi,n)
Y=linspace(-maxi,maxi,n)
x,y = meshgrid(X,Y)

Ex=3*x*y*(x**2+y**2)**(-5/2.)
Ey=1-(x**2+y**2)**(-3/2.)+3*y**2*(x**2+y**2)**(-5/2.)

# mascara para remover la parte central. Opcional
#r=1
#mascara=x**2+y**2>r**2
#Ex=mascara*Ex
#Ey=mascara*Ey
E=sqrt(Ex**2+Ey**2)

# Grafico
figure(figsize=(7,7))
Q = quiver(x,y,Ex/E,Ey/E, color='blue',pivot='middle',scale=40)
xlim(-maxi*1.1,maxi*1.1)
ylim(-maxi*1.1,maxi*1.1)
axis('off')
savefig('fig-esfera-conductora-raw.svg')
