# Trabajo de Computacion numerica 
# Autores : Ricardo Yañez Vega, Jose Guerrero

# Importamos modulo estandar "math"
import math


#Funciones q podemos probar :

#Polinomica (Razin simple) : f(x) = x^3 - x - 2
def funcion_polinomica(x):
    return (x**3) - x - 2

#Derivada funcion Polinomica
def Dfuncion_polinomica(x):
    return 3 * (x**2) - 2

#Exponencial : f(x) = e^(-x) - x
def funcion_exponencial(x):
    return math.exp(-x) - x

def Dfuncion_exponencial(x):
    return -math.exp(-x) - 1


#Implementacion Metodos de busqueda raices

#Metodo de biceccion
def bisecccion(f , a , b , tol , max_iter):

    if f(a) * f(b) >= 0:
        return None, "Error: El intervalo no cumple con el teorema de Bolzano. (f(a) * f(b) >= 0)."

    for i in range(max_iter):
        c = (a + b) / 2
        # Con abs obtenemos el valor absolutio del resultado de evaluar el punto medio "c" en la funcion
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c, i + 1
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, max_iter

def falsa_posicion(f, a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        return None, "Error: El intervalo no cumple con el teorema de Bolzano. (f(a)*f(b) >= 0)."

    for i in range(max_iter):
        c = (a+b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c, i + 1
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, max_iter




if __name__ == "__main__":
    print("\n=== PRUEBA DE MÉTODOS NUMÉRICOS CON ELEMENTOS NATIVOS ===")

    #Definicion de tolerancia
    TOLERANCIA = 1e-6

    print("\nLa tolerancia por defecto sera 1e-6")

    iteraciones = 100

    print("\nMetodo de la biseccion con la funcion polinomica (raiz simple) ")
    raiz_biseccion, iteracion_biseccion = bisecccion(funcion_polinomica , intervaloA = 1 , intervaloB = 2 , tol = TOLERANCIA , max_iter = iteraciones)

    print(f"Los resultado de la con la primera funcion son -> Raíz: {raiz_biseccion:.6f} | Iteraciones: {iteracion_biseccion}")
    



