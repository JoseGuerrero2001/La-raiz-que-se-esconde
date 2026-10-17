# Trabajo de Computacion numerica
# Autores : Ricardo Yañez Vega, Jose Guerrero

# Importamos modulo estandar "math"
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from pathlib import Path

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








if __name__ == "__main__":
    print("\n=== PRUEBA DE MÉTODOS NUMÉRICOS CON ELEMENTOS NATIVOS ===")

    #Definicion de tolerancia
    TOLERANCIA = 1e-6

    print("\nLa tolerancia por defecto sera 1e-6")

    iteraciones = 100
    """
    print("\nFUNCION POLINOMICA (RAIZ SIMPLE)")

    print("\nMetodo de la biseccion con la funcion polinomica (raiz simple) ")
    lista_raiz_biseccion, lista_iteracion_biseccion , lista_Fx_biseccion = bisecccion(funcion_polinomica , intervaloA = 1 , intervaloB = 2 , tol = TOLERANCIA , max_iter = iteraciones)

    funcion_archivo_csv(lista_raiz_biseccion, lista_Fx_biseccion, lista_iteracion_biseccion, "1-1funcion_poli_raiz_simple_biseccion.csv")
    
    print("\nMetodo de la falsa posicion con la funcion polinomica (raiz simple) ")
    lista_raiz_falsa_posicion, lista_iteracion_falsa_posicion , lista_Fx_falsa_posicion = falsa_posicion(funcion_polinomica , intervaloA = 1 , intervaloB = 2 , tol = TOLERANCIA , max_iter = iteraciones)

    funcion_archivo_csv(lista_raiz_falsa_posicion, lista_Fx_falsa_posicion, lista_iteracion_falsa_posicion, "1-2funcion_poli_raiz_simple_falsa_posicion.csv")

    

    print("\nMetodo de punto fijo con la funcion polinomica (raiz simple) ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 ")
    print("\nLa funcion g(x) utilizada sera g(x) = (2 + x)^(1/3)")
    lista_raiz_punto_fijo, lista_iteracion_punto_fijo, lista_Fx_punto_fijo = punto_fijo(g_polinomica_simple , x0 = 1 , tol = TOLERANCIA , max_iter = iteraciones)

    funcion_archivo_csv(lista_raiz_punto_fijo, lista_Fx_punto_fijo, lista_iteracion_punto_fijo, "1-3funcion_poli_raiz_simple_punto_fijo.csv")

    print("\nMetodo de la secante con la funcion polinomica (raiz simple) ")
    print("\nComo se utiliza dos puntos de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 y (el mayor numero del intervalo) x1 = 2 ")
    lista_raiz_secante, lista_iteracion_secante, lista_Fx_secante = secante(funcion_polinomica , x0 = 1 , x1 = 2 , tol = TOLERANCIA , max_iter = iteraciones)

    funcion_archivo_csv(lista_raiz_secante, lista_Fx_secante, lista_iteracion_secante, "1-4funcion_poli_raiz_simple_secante.csv")

    """


    print("\nMetodo de Newton-Raphson con la funcion polinomica (raiz simple) ")
    print("\nComo se utiliza un punto de partida a diferencia de los metodos anteriores, se utilizara (el menor numero del intervalo) x0 = 1 ")
    raiz_newton_raphson, iteracion_newton_raphson = newton_raphson(funcion_polinomica , Dfuncion_polinomica , x0 = 1 , tol = TOLERANCIA , max_iter = iteraciones)

    print(f"\nLos resultado de Newton-Raphson con la funcion polinomica (raiz simple) son -> Raíz: {raiz_newton_raphson:.6f} | Iteraciones: {iteracion_newton_raphson}")

