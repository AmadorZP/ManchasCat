import math
from math import pi,cos,sin,acos,tan,asin,sqrt
import numpy as np
import matplotlib.pyplot as plt

def Angulo_vectores(vec1,vec2):
    x1, y1, z1 = vec1
    x2, y2, z2 = vec2
    producto_interno=x1*x2+y1*y2+z1*z2
    modulo_vec1= sqrt(x1*x1+y1*y1+z1*z1)
    modulo_vec2= sqrt(x2*x2+y2*y2+z2*z2)
    theta=(math.acos(producto_interno/(modulo_vec1*modulo_vec2)))*180/pi
    return theta
def vectorizacion(punto1,punto2):
    x1, y1, z1 = punto1
    x2, y2, z2 = punto2
    vector=[x2-x1,y2-y1,z2-z1]
    return vector
def simetrico(X):
    X=np.fliplr(X)
    X = X + X.T - np.diag(np.diag(X))
    X=np.fliplr(X)
    return X
def Distancia(p, q, r):
    x = p-q
    t=np.dot(r-q, x)/np.dot(x, x)
    distancia=np.linalg.norm(t*(p-q)+q-r)
    return distancia
