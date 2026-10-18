# Trabajo de Computacion numerica
# Autores : Ricardo Yañez Vega, Jose Guerrero

# Importamos modulo estandar "math"
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from pathlib import Path

#Las funciones a probar estan en el archivo funciones.py

from funciones import funcion_polinomica, Dfuncion_polinomica , D2funcion_polinomica , g_polinomica_simple
from funciones import raiz_doble, Dfuncion_raiz_doble , D2funcion_raiz_doble, g_polinomica_doble
from funciones import funcion_exponencial, Dfuncion_exponencial , D2funcion_exponencial , g_exponencial
from funciones import f_trigonometrica, df_trigonometrica, D2f_trigonometrica , g_trigonometrica
from funciones import f_mixta, df_mixta , d2f_mixta , g_mixta

#Metodos de busqueda raices estan en el archivo
#biseccion.py, falsa_posicion.py, punto_fijo.py, secante.py, newton_raphson.py , newton_raphson_modificado.py

from biseccion import bisecccion
from falsa_posicion import falsa_posicion
from punto_fijo import punto_fijo
from secante import secante
from newton_raphson import newton_raphson
from newton_raphson_modificado import newton_raphson_modificado


def funcion_archivo_csv(lista_raices, lista_Fx, lista_iteraciones, nombre_archivo):
    """
    Función para guardar los resultados en un archivo CSV.
    """
    DIR_ACTUAL = Path(__file__).resolve().parent
    DIR_PADRE = DIR_ACTUAL.parent
    CARPETA_DESTINO = DIR_PADRE / "data"
    CARPETA_DESTINO.mkdir(parents=True, exist_ok=True)
    RUTA_CSV = CARPETA_DESTINO / nombre_archivo

    # Guardar los resultados en un archivo CSV
    with open(RUTA_CSV, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        # Escribimos los encabezados
        escritor.writerow(["X", "F(x)", "Iteraciones"])

        # Escribimos las filas combinando las listas
        for x, fx, iteracion in zip(lista_raices, lista_Fx, lista_iteraciones):
            escritor.writerow([x, fx, iteracion])

    print(f"\nArchivo guardado en : {RUTA_CSV}")



def FUNCION_POLINOMICA_RAIZ_SIMPLE():
    print("\nMetodo de la biseccion con la funcion polinomica (raiz simple) ")
    lista_raiz_biseccion, lista_iteracion_biseccion , lista_Fx_biseccion = bisecccion(funcion_polinomica , intervaloA = 1 , intervaloB = 2 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_biseccion} \nLista iteracion {lista_iteracion_biseccion} \nLista F(x) {lista_Fx_biseccion}")
    funcion_archivo_csv(lista_raiz_biseccion, lista_Fx_biseccion, lista_iteracion_biseccion, "1-1funcion_poli_raiz_simple_biseccion.csv")

    print("\nMetodo de la falsa posicion con la funcion polinomica (raiz simple) ")
    lista_raiz_falsa_posicion, lista_iteracion_falsa_posicion , lista_Fx_falsa_posicion = falsa_posicion(funcion_polinomica , intervaloA = 1 , intervaloB = 2 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_falsa_posicion} \nLista iteracion {lista_iteracion_falsa_posicion} \nLista F(x) {lista_Fx_falsa_posicion}")
    funcion_archivo_csv(lista_raiz_falsa_posicion, lista_Fx_falsa_posicion, lista_iteracion_falsa_posicion, "1-2funcion_poli_raiz_simple_falsa_posicion.csv")


    print("\nMetodo de punto fijo con la funcion polinomica (raiz simple) ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 ")
    print("\nLa funcion g(x) utilizada sera g(x) = (2 + x)^(1/3)")
    lista_raiz_punto_fijo, lista_iteracion_punto_fijo, lista_Fx_punto_fijo = punto_fijo(g_polinomica_simple , x0 = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_punto_fijo} \nLista iteracion {lista_iteracion_punto_fijo} \nLista F(x) {lista_Fx_punto_fijo}")
    funcion_archivo_csv(lista_raiz_punto_fijo, lista_Fx_punto_fijo, lista_iteracion_punto_fijo, "1-3funcion_poli_raiz_simple_punto_fijo.csv")



    print("\nMetodo de la secante con la funcion polinomica (raiz simple) ")
    print("\nComo se utiliza dos puntos de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 y (el mayor numero del intervalo) x1 = 2 ")
    lista_raiz_secante, lista_iteracion_secante, lista_Fx_secante = secante(funcion_polinomica , x0 = 1 , x1 = 2 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_secante} \nLista iteracion {lista_iteracion_secante} \nLista F(x) {lista_Fx_secante}")
    funcion_archivo_csv(lista_raiz_secante, lista_Fx_secante, lista_iteracion_secante, "1-4funcion_poli_raiz_simple_secante.csv")


    print("\nMetodo de Newton-Raphson con la funcion polinomica (raiz simple) ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 ")
    lista_raices_newton_raphson, lista_iteraciones_newton_raphson, lista_Fx_newton_raphson = newton_raphson(funcion_polinomica , Dfuncion_polinomica , x0 = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raices_newton_raphson} \nLista iteracion {lista_iteraciones_newton_raphson} \nLista F(x) {lista_Fx_newton_raphson}")
    funcion_archivo_csv(lista_raices_newton_raphson, lista_Fx_newton_raphson, lista_iteraciones_newton_raphson, "1-5funcion_poli_raiz_simple_newton_raphson.csv")


    print("\nMetodo de Newton-Raphson Modificado con la funcion polinomica (raiz simple) ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 ")
    lista_raices_newton_raphson_modificado, lista_iteraciones_newton_raphson_modificado, lista_Fx_newton_raphson_modificado = newton_raphson_modificado(funcion_polinomica , Dfuncion_polinomica , D2funcion_polinomica , x0 = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raices_newton_raphson_modificado} \nLista iteracion {lista_iteraciones_newton_raphson_modificado} \nLista F(x) {lista_Fx_newton_raphson_modificado}")
    funcion_archivo_csv(lista_raices_newton_raphson_modificado, lista_Fx_newton_raphson_modificado, lista_iteraciones_newton_raphson_modificado, "1-6funcion_poli_raiz_simple_newton_raphson_modificado.csv")

def FUNCION_POLINOMICA_RAIZ_DOBLE():
    print("\nMetodo de la biseccion con la funcion polinomica (raiz doble) ")
    lista_raiz_biseccion, lista_iteracion_biseccion , lista_Fx_biseccion = bisecccion(raiz_doble , intervaloA = 1 , intervaloB = 2 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_biseccion} \nLista iteracion {lista_iteracion_biseccion} \nLista F(x) {lista_Fx_biseccion}")
    #print("\nComo no cumple el teroema de Bolzano, no se puede aplicar el metodo de biseccion")

    print("\nMetodo de la falsa posicion con la funcion polinomica (raiz doble) ")
    lista_raiz_falsa_posicion, lista_iteracion_falsa_posicion , lista_Fx_falsa_posicion = falsa_posicion(raiz_doble , intervaloA = 1 , intervaloB = 2 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_falsa_posicion} \nLista iteracion {lista_iteracion_falsa_posicion} \nLista F(x) {lista_Fx_falsa_posicion}")
    #print("\nComo no cumple el teroema de Bolzano, no se puede aplicar el metodo de biseccion")


    print("\nMetodo punto fijo con la funcion polinomica (raiz doble) ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 ")
    print("\nLa funcion g(x) utilizada sera g(x) = 1 + ((x^2) / 4)")
    lista_raiz_punto_fijo, lista_iteracion_punto_fijo, lista_Fx_punto_fijo = punto_fijo(g_polinomica_doble , x0 = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_punto_fijo} \nLista iteracion {lista_iteracion_punto_fijo} \nLista F(x) {lista_Fx_punto_fijo}")
    funcion_archivo_csv(lista_raiz_punto_fijo, lista_Fx_punto_fijo, lista_iteracion_punto_fijo, "2-3funcion_poli_raiz_doble_punto_fijo.csv")

    print("\nMetodo de la secante con la funcion polinomica (raiz doble)")
    print("\nComo se utiliza dos puntos de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 y (el mayor numero del intervalo) x1 = 2 ")
    lista_raiz_secante, lista_iteracion_secante, lista_Fx_secante = secante(g_polinomica_doble , x0 = 1 , x1 = 2 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_secante} \nLista iteracion {lista_iteracion_secante} \nLista F(x) {lista_Fx_secante}")
    funcion_archivo_csv(lista_raiz_secante, lista_Fx_secante, lista_iteracion_secante, "2-4funcion_poli_raiz_doble_secante.csv")


    print(f"\nMetodo de newton-raphson con la funcion polinomica (raiz doble) ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 ")
    lista_raices_newton_raphson, lista_iteraciones_newton_raphson, lista_Fx_newton_raphson = newton_raphson(raiz_doble , Dfuncion_raiz_doble , x0 = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raices_newton_raphson} \nLista iteracion {lista_iteraciones_newton_raphson} \nLista F(x) {lista_Fx_newton_raphson}")
    funcion_archivo_csv(lista_raices_newton_raphson, lista_Fx_newton_raphson, lista_iteraciones_newton_raphson, "2-5funcion_poli_raiz_doble_newton_raphson.csv")


    print(f"\nMetodo de newton-raphson modificado con la funcion polinomica (raiz doble) ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 ")
    lista_raices_newton_raphson_modificado, lista_iteraciones_newton_raphson_modificado, lista_Fx_newton_raphson_modificado = newton_raphson_modificado(raiz_doble , Dfuncion_raiz_doble , D2funcion_raiz_doble , x0 = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raices_newton_raphson_modificado} \nLista iteracion {lista_iteraciones_newton_raphson_modificado} \nLista F(x) {lista_Fx_newton_raphson_modificado}")
    funcion_archivo_csv(lista_raices_newton_raphson_modificado, lista_Fx_newton_raphson_modificado, lista_iteraciones_newton_raphson_modificado, "2-6funcion_poli_raiz_doble_newton_raphson_modificado.csv")

def FUNCION_EXPONENCIAL():
    print(f"\nMetodo de biseccion con la funcion exponencial ")
    lista_raiz_biseccion, lista_iteracion_biseccion , lista_Fx_biseccion = bisecccion(funcion_exponencial , intervaloA = 0 , intervaloB = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_biseccion} \nLista iteracion {lista_iteracion_biseccion} \nLista F(x) {lista_Fx_biseccion}")
    funcion_archivo_csv(lista_raiz_biseccion, lista_Fx_biseccion, lista_iteracion_biseccion, "3-1funcion_exponencial_biseccion.csv")


    print("\nMetodo de la falsa posicion con la funcion exponencial ")
    lista_raiz_falsa_posicion, lista_iteracion_falsa_posicion , lista_Fx_falsa_posicion = falsa_posicion(funcion_exponencial , intervaloA = 0 , intervaloB = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_falsa_posicion} \nLista iteracion {lista_iteracion_falsa_posicion} \nLista F(x) {lista_Fx_falsa_posicion}")
    funcion_archivo_csv(lista_raiz_falsa_posicion, lista_Fx_falsa_posicion, lista_iteracion_falsa_posicion, "3-2funcion_exponencial_falsa_posicion.csv")


    print("\nMetodo de punto fijo con la funcion exponencial ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 0 ")
    print("\nLa funcion g(x) utilizada sera g(x) = e^(-x)")
    lista_raiz_punto_fijo, lista_iteracion_punto_fijo, lista_Fx_punto_fijo = punto_fijo(g_exponencial , x0 = 0 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_punto_fijo} \nLista iteracion {lista_iteracion_punto_fijo} \nLista F(x) {lista_Fx_punto_fijo}")
    funcion_archivo_csv(lista_raiz_punto_fijo, lista_Fx_punto_fijo, lista_iteracion_punto_fijo, "3-3funcion_exponencial_punto_fijo.csv")


    print("\nMetodo de la secante con la funcion exponencial ")
    print("\nComo se utiliza dos puntos de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 0 y (el mayor numero del intervalo) x1 = 1 ")
    lista_raiz_secante, lista_iteracion_secante, lista_Fx_secante = secante(funcion_exponencial , x0 = 0 , x1 = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_secante} \nLista iteracion {lista_iteracion_secante} \nLista F(x) {lista_Fx_secante}")
    funcion_archivo_csv(lista_raiz_secante, lista_Fx_secante, lista_iteracion_secante, "3-4funcion_exponencial_secante.csv")


    print("\nMetodo de Newton-Raphson con la funcion exponencial ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 0 ")
    lista_raices_newton_raphson, lista_iteraciones_newton_raphson, lista_Fx_newton_raphson = newton_raphson(funcion_exponencial , Dfuncion_exponencial , x0 = 0 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raices_newton_raphson} \nLista iteracion {lista_iteraciones_newton_raphson} \nLista F(x) {lista_Fx_newton_raphson}")
    funcion_archivo_csv(lista_raices_newton_raphson, lista_Fx_newton_raphson, lista_iteraciones_newton_raphson, "3-5funcion_exponencial_newton_raphson.csv")


    print("\nMetodo de Newton-Raphson Modificado con la funcion exponencial ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 0 ")
    lista_raices_newton_raphson_modificado, lista_iteraciones_newton_raphson_modificado, lista_Fx_newton_raphson_modificado = newton_raphson_modificado(funcion_exponencial , Dfuncion_exponencial , D2funcion_exponencial , x0 = 0 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raices_newton_raphson_modificado} \nLista iteracion {lista_iteraciones_newton_raphson_modificado} \nLista F(x) {lista_Fx_newton_raphson_modificado}")
    funcion_archivo_csv(lista_raices_newton_raphson_modificado, lista_Fx_newton_raphson_modificado, lista_iteraciones_newton_raphson_modificado, "3-6funcion_exponencial_newton_raphson_modificado.csv")

def FUNCION_TRIGONOMETRICA():

    print("\nMetodo de biseccion con la funcion trigonometrica ")
    lista_raiz_biseccion, lista_iteracion_biseccion , lista_Fx_biseccion = bisecccion(f_trigonometrica , intervaloA = 0 , intervaloB = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_biseccion} \nLista iteracion {lista_iteracion_biseccion} \nLista F(x) {lista_Fx_biseccion}")
    funcion_archivo_csv(lista_raiz_biseccion, lista_Fx_biseccion, lista_iteracion_biseccion, "4-1funcion_trigonometrica_biseccion.csv")


    print("\nMetodo de la falsa posicion con la funcion trigonometrica ")
    lista_raiz_falsa_posicion, lista_iteracion_falsa_posicion , lista_Fx_falsa_posicion = falsa_posicion(f_trigonometrica , intervaloA = 0 , intervaloB = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_falsa_posicion} \nLista iteracion {lista_iteracion_falsa_posicion} \nLista F(x) {lista_Fx_falsa_posicion}")
    funcion_archivo_csv(lista_raiz_falsa_posicion, lista_Fx_falsa_posicion, lista_iteracion_falsa_posicion, "4-2funcion_trigonometrica_falsa_posicion.csv")


    print("\nMetodo de punto fijo con la funcion trigonometrica ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 0 ")
    print("\nLa funcion g(x) utilizada sera g(x) = 1 - (x^3)^(1/3)")
    lista_raiz_punto_fijo, lista_iteracion_punto_fijo, lista_Fx_punto_fijo = punto_fijo(g_trigonometrica , x0 = 0 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_punto_fijo} \nLista iteracion {lista_iteracion_punto_fijo} \nLista F(x) {lista_Fx_punto_fijo}")
    funcion_archivo_csv(lista_raiz_punto_fijo, lista_Fx_punto_fijo, lista_iteracion_punto_fijo, "4-3funcion_trigonometrica_punto_fijo.csv")


    print("\nMetodo de la secante con la funcion trigonometrica ")
    print("\nComo se utiliza dos puntos de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 0 y (el mayor numero del intervalo) x1 = 1 ")
    lista_raiz_secante, lista_iteracion_secante, lista_Fx_secante = secante(f_trigonometrica , x0 = 0 , x1 = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_secante} \nLista iteracion {lista_iteracion_secante} \nLista F(x) {lista_Fx_secante}")
    funcion_archivo_csv(lista_raiz_secante, lista_Fx_secante, lista_iteracion_secante, "4-4funcion_trigonometrica_secante.csv")


    print("\nMetodo de Newton-Raphson con la funcion trigonometrica ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 0 ")
    lista_raices_newton_raphson, lista_iteraciones_newton_raphson, lista_Fx_newton_raphson = newton_raphson(f_trigonometrica , df_trigonometrica , x0 = 0 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raices_newton_raphson} \nLista iteracion {lista_iteraciones_newton_raphson} \nLista F(x) {lista_Fx_newton_raphson}")
    funcion_archivo_csv(lista_raices_newton_raphson, lista_Fx_newton_raphson, lista_iteraciones_newton_raphson, "4-5funcion_trigonometrica_newton_raphson.csv")


    print("\nMetodo de Newton-Raphson Modificado con la funcion trigonometrica ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 0 ")
    lista_raices_newton_raphson_modificado, lista_iteraciones_newton_raphson_modificado, lista_Fx_newton_raphson_modificado = newton_raphson_modificado(f_trigonometrica , df_trigonometrica , D2f_trigonometrica , x0 = 0 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raices_newton_raphson_modificado} \nLista iteracion {lista_iteraciones_newton_raphson_modificado} \nLista F(x) {lista_Fx_newton_raphson_modificado}")
    funcion_archivo_csv(lista_raices_newton_raphson_modificado, lista_Fx_newton_raphson_modificado, lista_iteraciones_newton_raphson_modificado, "4-6funcion_trigonometrica_newton_raphson_modificado.csv")

def FUNCION_MIXTA():

    print("\nMetodo de biseccion con la funcion mixta ")
    lista_raiz_biseccion, lista_iteracion_biseccion , lista_Fx_biseccion = bisecccion(f_mixta , intervaloA = 0.1 , intervaloB = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_biseccion} \nLista iteracion {lista_iteracion_biseccion} \nLista F(x) {lista_Fx_biseccion}")
    funcion_archivo_csv(lista_raiz_biseccion, lista_Fx_biseccion, lista_iteracion_biseccion, "5-1funcion_trigonometrica_biseccion.csv")


    print("\nMetodo de la falsa posicion con la funcion mixta")
    lista_raiz_falsa_posicion, lista_iteracion_falsa_posicion , lista_Fx_falsa_posicion = falsa_posicion(f_mixta , intervaloA = 0.1 , intervaloB = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_falsa_posicion} \nLista iteracion {lista_iteracion_falsa_posicion} \nLista F(x) {lista_Fx_falsa_posicion}")
    funcion_archivo_csv(lista_raiz_falsa_posicion, lista_Fx_falsa_posicion, lista_iteracion_falsa_posicion, "5-2funcion_mixta_falsa_posicion.csv")


    print("\nMetodo de punto fijo con la funcion mixta ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 0.1 ")
    print("\nLa funcion g(x) utilizada sera g(x) = (cos(x)) ^ 2")
    lista_raiz_punto_fijo, lista_iteracion_punto_fijo, lista_Fx_punto_fijo = punto_fijo( g_mixta , x0 = 0.1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_punto_fijo} \nLista iteracion {lista_iteracion_punto_fijo} \nLista F(x) {lista_Fx_punto_fijo}")
    funcion_archivo_csv(lista_raiz_punto_fijo, lista_Fx_punto_fijo, lista_iteracion_punto_fijo, "5-3funcion_mixta_punto_fijo.csv")


    print("\nMetodo de la secante con la funcion mixta")
    print("\nComo se utiliza dos puntos de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 0.1 y (el mayor numero del intervalo) x1 = 1 ")
    lista_raiz_secante, lista_iteracion_secante, lista_Fx_secante = secante(f_mixta , x0 = 0.1 , x1 = 1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raiz_secante} \nLista iteracion {lista_iteracion_secante} \nLista F(x) {lista_Fx_secante}")
    funcion_archivo_csv(lista_raiz_secante, lista_Fx_secante, lista_iteracion_secante, "5-4funcion_mixta_secante.csv")


    print("\nMetodo de Newton-Raphson con la funcion mixta ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 0.1 ")
    lista_raices_newton_raphson, lista_iteraciones_newton_raphson, lista_Fx_newton_raphson = newton_raphson(f_mixta , df_mixta , x0 = 0.1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raices_newton_raphson} \nLista iteracion {lista_iteraciones_newton_raphson} \nLista F(x) {lista_Fx_newton_raphson}")
    funcion_archivo_csv(lista_raices_newton_raphson, lista_Fx_newton_raphson, lista_iteraciones_newton_raphson, "5-5funcion_mixta_newton_raphson.csv")


    print("\nMetodo de Newton-Raphson Modificado con la funcion mixta")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 0.1 ")
    lista_raices_newton_raphson_modificado, lista_iteraciones_newton_raphson_modificado, lista_Fx_newton_raphson_modificado = newton_raphson_modificado(f_mixta , df_mixta , d2f_mixta , x0 = 0.1 , tol = TOLERANCIA , max_iter = iteraciones)
    print(f"\nLista raiz {lista_raices_newton_raphson_modificado} \nLista iteracion {lista_iteraciones_newton_raphson_modificado} \nLista F(x) {lista_Fx_newton_raphson_modificado}")
    funcion_archivo_csv(lista_raices_newton_raphson_modificado , lista_Fx_newton_raphson_modificado , lista_iteraciones_newton_raphson_modificado , "5-6funcion_mixta_newton_raphson_modificado.csv")









if __name__ == "__main__":

    print("\n=== PRUEBA DE MÉTODOS NUMÉRICOS CON ELEMENTOS NATIVOS ===")

    #Definicion de tolerancia
    TOLERANCIA = 1e-6

    print("\nLa tolerancia por defecto sera 1e-6")

    iteraciones = 100

    print("\nFUNCION POLINOMICA (RAIZ SIMPLE)")

    #FUNCION_POLINOMICA_RAIZ_SIMPLE()

    print("\nFUNCION POLINOMICA (RAIZ DOBLE)")

    #FUNCION_POLINOMICA_RAIZ_DOBLE()

    print("\nFUNCION EXPONENCIAL ")

    #FUNCION_EXPONENCIAL()

    print("\nFUNCION TRIGONOMETRICA ")

    #FUNCION_TRIGONOMETRICA()

    print("\nFUNCION MIXTA ")

    #FUNCION_MIXTA()




    None