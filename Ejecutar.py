from Funciones_Geo import Angulo_vectores,vectorizacion,simetrico,Distancia
import math
from math import pi,cos,sin,acos,tan,asin,sqrt
import numpy as np
import matplotlib.pyplot as plt
from sympy import integrate, init_printing,Integral
from sympy.abc import x
import matplotlib.ticker as ticker

"""
Variables:
"""
P=30#Potencia de la luminaria (W)
L=0.65*sqrt(2) #Longitud de la luminaria en funcion del lado de la proyección (en metros)
h=0.3 #Distancia hacia el plano (en metros)
ord=20#Dimensión de la matriz cuadrada. Preprensenta la cantidad de puntos en el grafico, cada punto representa un color
#Se recomienda no asignar un valor muy alto (>30) a ord por el costo computacional cuadrático




"""
Codigo:
"""

m=ord
n=ord
lado=L/sqrt(2)
i=np.arange(m)
j=np.arange(n)
k=0
fraccion=lado/(np.size(i)-1)

malla=np.zeros(m*n*3).reshape(m, n, 3)

for ii in i:
    for jj in j:
        malla[ii,jj]=np.array([ii,jj,k])*fraccion

matriz_angulos=np.zeros((m,n))
pt1_lamp=[0,lado,h]
pt2_lamp=[lado,0,h]
vector_lampara=vectorizacion(pt1_lamp,pt2_lamp)

for i in range(m):
    for j in range(i+1):
        matriz_angulos[i,(-j-1)]=90-Angulo_vectores(vector_lampara,vectorizacion(pt1_lamp,malla[i,(-j-1)]))


matriz_distancias=np.zeros((m,n))

for i in range(m):
    for j in range(i+1):
        matriz_distancias[i,(-j-1)]=Distancia(np.array(pt1_lamp),np.array(pt2_lamp),malla[i,(-j-1)])


matriz_irradiancia=np.zeros((m,n))
ex=2.0


for i in range(m):
    for j in range(i+1):
        D=matriz_distancias[i,(-j-1)]
        a=L-D*tan(matriz_angulos[i,(-j-1)]*pi/180)
        b=D*tan(matriz_angulos[i,(-j-1)]*pi/180)
        matriz_irradiancia[i,(-j-1)]=Integral(((P*D*D)/(pi*pi*L*((D*D+x**ex))**ex)), (x,-a,b)).n()


matriz_irradiancia=simetrico(matriz_irradiancia)
print(matriz_irradiancia[m-1,n-1])
matriz_irradiancia=np.fliplr(matriz_irradiancia)
fig, ax = plt.subplots()
im = ax.imshow(matriz_irradiancia)
plt.imshow(matriz_irradiancia, extent=[0, lado, 0, lado])
def fmt(x, pos):
    a, b = '{:.2e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)
cbar = plt.colorbar(format=ticker.FuncFormatter(fmt))
ax.set_title("Matriz Irradiancia", y=-0.1)



"""
ax.xaxis.tick_top()
ax.set(xlim=(-0.5, 13.4), ylim=(-0.5, 13.4))
ax.invert_yaxis()
"""
plt.xlabel("x(m)")
ax.xaxis.set_label_position('top')
plt.ylabel("y(m)")
ax.invert_yaxis()
ax.xaxis.tick_top()
cbar.set_label(r'$\frac{mW}{{cm}^2}$',rotation=90,fontsize=20)
fig.tight_layout()
fig.savefig('Irradiancia.png')
plt.show()
