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

def bisecccion(f , a , b , tol , max_iter):
    if f(a) * f(b) >= 0:
        return None, "Error: El intervalo no cumple con el teorema de Bolzano. (f(a) * f(b) >= 0)."

    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c, i + 1
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, max_iter


if __name__ == "__main__":
    print("=== PRUEBA DE MÉTODOS NUMÉRICOS CON ELEMENTOS NATIVOS ===\n")

    #Definicion de tolerancia
    TOLERANCIA = 1e-6

    print("\nLa tolerancia por defecto sera 1e-6")

    ITERACIONES: 100
    ITERACIONES = int(input("\nIngrese num de iteraciones personalizada (opcional, por defecto sera 100) "))

    ExA = 1.0
    ExB = 2.0
    ExA = float(input("\nIngrese num de extremo A personalizado (por defecto 1)"))
    ExB = float(input("\nIngrese num de extremo B personalizado (por defecto 2)"))




