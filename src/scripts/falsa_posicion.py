
# Método de Falsa Posición (con historial en listas)
def falsa_posicion(f, a, b, tol=1e-6, max_iter=100):
    """Método Cerrado: Falsa Posición (Regula Falsi)."""
    
    lista_raices = []
    lista_iteraciones = []
    lista_Fx = []

    if f(a) * f(b) >= 0:
        print("\nError: El intervalo no cumple con el teorema de Bolzano.")
        return None, None, None
    
    c_ant = a
    for i in range(max_iter):
        fa, fb = f(a), f(b)
        

        c = b - (fb * (a - b)) / (fa - fb)
        
        lista_iteraciones.append(i + 1)
        lista_raices.append(round(c, 6))
        lista_Fx.append(round(f(c), 6))
        

        if abs(f(c)) < tol or abs(c - c_ant) < tol:
            return lista_raices, lista_iteraciones, lista_Fx
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c_ant = c
        
    return lista_raices, lista_iteraciones, lista_Fx
