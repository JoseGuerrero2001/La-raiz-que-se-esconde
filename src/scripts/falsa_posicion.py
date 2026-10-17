
#Metodo de falsa posicion

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