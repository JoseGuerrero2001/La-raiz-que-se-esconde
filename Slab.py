# Trabajo de Computacion numerica 
# Autores : Ricardo Yañez Vega, Jose Guerrero

# Importamos modulo estandar "math"
import math

#funcion de valores personalizado
def entrada(la_entrada, default):
    if la_entrada == "":
        valor = default
    else:
        valor = int(la_entrada)
    return valor






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
    print("=== PRUEBA DE MÉTODOS NUMÉRICOS CON ELEMENTOS NATIVOS ===\n")

    #Definicion de tolerancia
    TOLERANCIA = 1e-6

    print("\nLa tolerancia por defecto sera 1e-6")

    default_iteraciones = 100
    entrada_iteraciones = input("\nIngrese num de iteraciones personalizada (opcional, por defecto sera 100) ")

    valor_interaciones = entrada(entrada_iteraciones, default_iteraciones)

    default_ExtremoA = 1.0
    default_ExtremoB = 2.0
    entrada_ExtremoA = input("\nIngrese num de extremo A personalizado (por defecto 1)")
    entrada_ExtremoB = input("\nIngrese num de extremo B personalizado (por defecto 2)")

    valor_ExtremoA = entrada(entrada_ExtremoA , default_ExtremoA )
    valor_ExtremoB = entrada(entrada_ExtremoB , default_ExtremoB )




 

    raiz_biseccion, iteracion_biseccion = bisecccion(funcion_polinomica , valor_ExtremoA , valor_ExtremoB , valor_interaciones)



