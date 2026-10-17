
#Metodo de biceccion

def bisecccion(f , intervaloA , intervaloB , tol , max_iter ):

    lista_raices = []
    lista_iteraciones = []
    lista_Fx = []



    if f(intervaloA) * f(intervaloB) >= 0:
        return None, "Error: El intervalo no cumple con el teorema de Bolzano. (f(a) * f(b) >= 0)."

    for i in range(max_iter):
        lista_iteraciones.append(i + 1)
        c = (intervaloA + intervaloB) / 2
        lista_raices.append(round(c, 6))
        lista_Fx.append(round(f(c), 6))
        #print(f"\nIteracion {i + 1}:")
        #print(f"\nValor de c: {c:.6f}")
        # Con abs obtenemos el valor absolutio del resultado de evaluar el punto medio "c" en la funcion
        if abs(f(c)) < tol or (intervaloB - intervaloA) / 2 < tol:
            
            return lista_raices, lista_iteraciones
        if f(intervaloA) * f(c) < 0:
            intervaloB = c
        else:
            intervaloA = c
    return lista_raices, lista_iteraciones
