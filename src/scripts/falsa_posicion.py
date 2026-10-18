
# Método de Falsa Posición (con historial en listas)
def falsa_posicion(f , intervaloA , intervaloB , tol , max_iter ):
    """Método Cerrado: Falsa Posición (Regula Falsi)."""
    
    lista_raices = []
    lista_iteraciones = []
    lista_Fx = []

    if f(intervaloA) * f(intervaloB) >= 0:
        lista_raices = [0]
        lista_iteraciones = [0]
        lista_Fx = [0]
        print("\nError: El intervalo no cumple con el teorema de Bolzano.")
        return lista_raices, lista_iteraciones, lista_Fx
    
    c_ant = intervaloA
    for i in range(max_iter):
        fa, fb = f(intervaloA), f(intervaloB)
        

        c = intervaloB - (fb * (intervaloA - intervaloB)) / (fa - fb)
        
        lista_iteraciones.append(i + 1)
        lista_raices.append(round(c, 6))
        lista_Fx.append(round(f(c), 6))
        

        if abs(f(c)) < tol or abs(c - c_ant) < tol:
            return lista_raices, lista_iteraciones, lista_Fx
        
        if f(intervaloA) * f(c) < 0:
            intervaloB = c
        else:
            intervaloA = c
        c_ant = c
        
    return lista_raices, lista_iteraciones, lista_Fx
