
import math
import numpy as np

#Funciones a probar

#Polinomica (Razin simple) : f(x) = x^3 - x - 2
def funcion_polinomica(x):
    return (x**3) - x - 2

#Derivada funcion Polinomica
def Dfuncion_polinomica(x):
    return 3 * (x**2) - 1

#Derivada 2 funcion Polinomica
def D2funcion_polinomica(x):
    return 6 * x

#Funcion G Polinomica (Raiz simple)
def g_polinomica_simple(x):
    return (2 + x)**(1/3)

#Polonomica (Raiz doble) : f(x) = (x - 2)^2
def raiz_doble(x):
    return (x - 2)**2



#Derivada funcion Raiz doble
def Dfuncion_raiz_doble(x):
    return 2 * (x - 2)

#Exponencial : f(x) = e^(-x) - x
def funcion_exponencial(x):
    return math.exp(-x) - x

#Derivada funcion Exponencial
def Dfuncion_exponencial(x):
    return -math.exp(-x) - 1

#trigonometrica : f(x) = cos(x) - x
def f_trigonometrica(x):
    return np.cos(x) - x

#derivada funcion Trigonometrica
def df_trigonometrica(x):
    return -np.sin(x) - 1.0

#funcion mixta : f(x) = sqrt(x) - cos(x)
def f_mixta(x):
    return np.sqrt(x) - np.cos(x)

#derivada funcion mixta
def df_mixta(x):
    return 1.0 / (2.0 * np.sqrt(x)) + np.sin(x)
