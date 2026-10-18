# Trabajo de Computacion numerica 
# Autores : Ricardo Yañez Vega, José Guerrero

# Importamos modulo estandar "math"
import math
import numpy as np
import matplotlib.pyplot as plt


#Funciones a probar

#Polinomica (Razin simple) : f(x) = x^3 - x - 2
def funcion_polinomica(x):
    return (x**3) - x - 2

#Derivada funcion Polinomica
def Dfuncion_polinomica(x):
    return 3 * (x**2) - 1

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


#Implementacion Metodos de busqueda raices

#Metodo de biceccion
def bisecccion(f , intervaloA , intervaloB , tol , max_iter ):

    if f(intervaloA) * f(intervaloB) >= 0:
        return None, "Error: El intervalo no cumple con el teorema de Bolzano. (f(a) * f(b) >= 0)."

    for i in range(max_iter):
        c = (intervaloA + intervaloB) / 2
        # Con abs obtenemos el valor absolutio del resultado de evaluar el punto medio "c" en la funcion
        if abs(f(c)) < tol or (intervaloB - intervaloA) / 2 < tol:
            return c, i + 1
        if f(intervaloA) * f(c) < 0:
            intervaloB = c
        else:
            intervaloA = c
    return c, max_iter

#Metodo de falsa posicion
def falsa_posicion(f , intervaloA , intervaloB , tol , max_iter):

    if f(intervaloA) * f(intervaloB) >= 0:
        return None, "Error: El intervalo no cumple con el teorema de Bolzano. (f(a)*f(b) >= 0)."

    for i in range(max_iter):
        c = (intervaloA+intervaloB) / 2
        if abs(f(c)) < tol or (intervaloB - intervaloA) / 2 < tol:
            return c, i + 1
        if f(intervaloA) * f(c) < 0:
            intervaloB = c
        else:
            intervaloA = c
    return c, max_iter

#Metodo de punto fijo
def punto_fijo(g, x0, tol , max_iter):
    """Método Abierto: Iteración de Punto Fijo (x = g(x))."""
    x = x0
    for i in range(max_iter):
        x_nuevo = g(x)
        if abs(x_nuevo - x) < tol:
            return x_nuevo, i + 1
        x = x_nuevo
    return x, max_iter

#Metodo de la secante
def secante(f, x0, x1, tol, max_iter):
    for i in range(max_iter):
        fx0, fx1 = f(x0), f(x1)
        if fx1 - fx0 == 0:
            return None, "Error: Division por cero en el metodo de la sec."
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x2 - x1) < tol or abs(f(x2)) < tol:
            return x2, i + 1
        x0, x1 = x1, x2
    return x1, max_iter

#Metodo de Newton-Raphson
def newton_raphson(f, df, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x, i + 1

        dfx = df(x)
        if dfx == 0:
            return None, "Error: Derivada = a cero."

        x_nuevo = x - (fx / dfx)
        if abs(x_nuevo - x) < tol:
            return x_nuevo, i + 1
        x = x_nuevo
    return x, max_iter

def newton_raphson_mejorado(f, df, ddf, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x, i + 1

        dfx = df(x)
        ddfx = ddf(x) 

        denominador = (dfx ** 2) - (fx * ddfx)
        if denominador == 0:
            return None, "Error: Denominador cero en Newton mejorado."

        x_nuevo = x - (fx * dfx) / denominador
        if abs(x_nuevo - x) < tol:
            return x_nuevo, i + 1
        x = x_nuevo
    return x, max_iter



    
if __name__ == "__main__":
    print("\n=== PRUEBA DE MÉTODOS NUMÉRICOS CON ELEMENTOS NATIVOS ===")

    #Definicion de tolerancia
    TOLERANCIA = 1e-6

    print("\nLa tolerancia por defecto sera 1e-6")

    iteraciones = 100

    """
    print("\n=============================================================================================================================================================================")
    print("\nFuncion polinomica (raiz simple) ")

    print("\nMetodo de la biseccion con la funcion polinomica (raiz simple) ")
    raiz_biseccion, iteracion_biseccion = bisecccion(funcion_polinomica , intervaloA = 1 , intervaloB = 2 , tol = TOLERANCIA , max_iter = iteraciones)

    print(f"\nLos resultado de biseccion con la funcion polinomica (raiz simple) son -> Raíz: {raiz_biseccion:.6f} | Iteraciones: {iteracion_biseccion}")

    print("\nMetodo de la falsa posicion con la funcion polinomica (raiz simple) ")
    raiz_falsa_posicion, iteracion_falsa_posicion = falsa_posicion(funcion_polinomica , intervaloA = 1 , intervaloB = 2 , tol = TOLERANCIA , max_iter = iteraciones)

    print(f"\nLos resultado de la falsa posicion con la funcion polinomica (raiz simple) son -> Raíz: {raiz_falsa_posicion:.6f} | Iteraciones: {iteracion_falsa_posicion}")

    """

    print("\nMetodo de punto fijo con la funcion polinomica (raiz simple) ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 ")
    print("\nLa funcion g(x) utilizada sera g(x) = (2 + x)^(1/3)")
    raiz_punto_fijo, iteracion_punto_fijo = punto_fijo(g_polinomica_simple , x0 = 1 , tol = TOLERANCIA , max_iter = iteraciones)

    print(f"\nLos resultado de punto fijo con la funcion polinomica (raiz simple) son -> Raíz: {raiz_punto_fijo:.6f} | Iteraciones: {iteracion_punto_fijo}")


    print("\nMetodo de la secante con la funcion polinomica (raiz simple) ")
    print("\nComo se utiliza dos puntos de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 y (el mayor numero del intervalo) x1 = 2 ")
    raiz_secante, iteracion_secante = secante(funcion_polinomica , x0 = 1 , x1 = 2 , tol = TOLERANCIA , max_iter = iteraciones)

    print(f"\nLos resultado de la secante con la funcion polinomica (raiz simple) son -> Raíz: {raiz_secante:.6f} | Iteraciones: {iteracion_secante}")

    print("\nMetodo de Newton-Raphson con la funcion polinomica (raiz simple) ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 ")
    raiz_newton_raphson, iteracion_newton_raphson = newton_raphson(funcion_polinomica , Dfuncion_polinomica , x0 = 1 , tol = TOLERANCIA , max_iter = iteraciones)

    print(f"\nLos resultado de Newton-Raphson con la funcion polinomica (raiz simple) son -> Raíz: {raiz_newton_raphson:.6f} | Iteraciones: {iteracion_newton_raphson}")

    #probando