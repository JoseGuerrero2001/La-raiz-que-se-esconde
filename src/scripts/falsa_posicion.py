
#Metodo de falsa posicion

def falsa_posicion(g , intervaloA , intervaloB , tol , max_iter):

    lista_raices = []
    lista_iteraciones = []
    lista_Fx = []


    if g(intervaloA) * g(intervaloB) >= 0:
        print("\nError: El intervalo no cumple con el teorema de Bolzano. (f(a) * f(b) >= 0).")
        return None, None, None

    for i in range(max_iter):
        c = (intervaloA+intervaloB) / 2
        lista_raices.append(round(c, 6))
        lista_iteraciones.append(i + 1)
        lista_Fx.append(round(g(c), 6))
        if abs(g(c)) < tol or (intervaloB - intervaloA) / 2 < tol:
            return lista_raices, lista_iteraciones , lista_Fx
        if g(intervaloA) * g(c) < 0:
            intervaloB = c
        else:
            intervaloA = c
    return lista_raices, lista_iteraciones , lista_Fx
