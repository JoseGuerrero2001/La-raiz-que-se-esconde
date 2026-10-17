# Trabajo de Computacion numerica
# Autores : Ricardo Yañez Vega, Jose Guerrero

# Importamos modulo estandar "math"
import math
import numpy as np
import matplotlib.pyplot as plt


#Las funciones a probar estan en el archivo funciones.py

from funciones import funcion_polinomica, Dfuncion_polinomica, g_polinomica_simple, raiz_doble, Dfuncion_raiz_doble, funcion_exponencial, Dfuncion_exponencial, f_trigonometrica, df_trigonometrica, f_mixta, df_mixta


#Metodos de busqueda raices estan en el archivo
#biseccion.py, falsa_posicion.py, punto_fijo.py, secante.py, newton_raphson.py , newton_raphson_modificado.py

from biseccion import bisecccion
from falsa_posicion import falsa_posicion
from punto_fijo import punto_fijo
from secante import secante
from newton_raphson import newton_raphson
from newton_raphson_modificado import newton_raphson_modificado




if __name__ == "__main__":
    print("\n=== PRUEBA DE MÉTODOS NUMÉRICOS CON ELEMENTOS NATIVOS ===")

    #Definicion de tolerancia
    TOLERANCIA = 1e-6

    print("\nLa tolerancia por defecto sera 1e-6")

    iteraciones = 100


    print("\n===============================================================================================================================================")
    print("\nFuncion polinomica (raiz simple) ")

    print("\nMetodo de la biseccion con la funcion polinomica (raiz simple) ")
    raiz_biseccion, iteracion_biseccion = bisecccion(funcion_polinomica , intervaloA = 1 , intervaloB = 2 , tol = TOLERANCIA , max_iter = iteraciones)

    print(f"\nLos resultado de biseccion con la funcion polinomica (raiz simple) son -> Raíz: {raiz_biseccion:.6f} | Iteraciones: {iteracion_biseccion}")

    """

    print("\nMetodo de la falsa posicion con la funcion polinomica (raiz simple) ")
    raiz_falsa_posicion, iteracion_falsa_posicion = falsa_posicion(funcion_polinomica , intervaloA = 1 , intervaloB = 2 , tol = TOLERANCIA , max_iter = iteraciones)

    print(f"\nLos resultado de la falsa posicion con la funcion polinomica (raiz simple) son -> Raíz: {raiz_falsa_posicion:.6f} | Iteraciones: {iteracion_falsa_posicion}")



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

    """