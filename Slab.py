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


if __name__ == "__main__":
    print("\n=== PRUEBA DE MÉTODOS NUMÉRICOS CON ELEMENTOS NATIVOS ===")

    #Definicion de tolerancia
    TOLERANCIA = 1e-6

    print("\nLa tolerancia por defecto sera 1e-6")

    iteraciones = 100

    print("\nMetodo de la biseccion con la funcion polinomica (raiz simple) ")
    raiz_biseccion, iteracion_biseccion = bisecccion(funcion_polinomica , intervaloA = 1 , intervaloB = 2 , tol = TOLERANCIA , max_iter = iteraciones)

    print(f"\nLos resultado de la con la primera funcion son -> Raíz: {raiz_biseccion:.6f} | Iteraciones: {iteracion_biseccion}")





