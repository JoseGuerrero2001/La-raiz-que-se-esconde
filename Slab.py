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


if __name__ == "__main__":
    print("=== PRUEBA DE MÉTODOS NUMÉRICOS CON ELEMENTOS NATIVOS ===\n")

    #Definicion de tolerancia
    TOLERANCIA = 1e-6

