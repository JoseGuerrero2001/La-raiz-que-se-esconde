
#Metodo de punto fijo

def punto_fijo(g, x0, tol , max_iter):
    """Método Abierto: Iteración de Punto Fijo (x = g(x))."""

    lista_raices = []
    lista_iteraciones = []
    lista_Fx = []

    x = x0
    for i in range(max_iter):
        lista_iteraciones.append(i + 1)
        lista_raices.append(round(x, 6))
        lista_Fx.append(round(g(x), 6))

        x_nuevo = g(x)
        if abs(x_nuevo - x) < tol:
            return lista_raices, lista_iteraciones , lista_Fx
        x = x_nuevo
    return lista_raices, lista_iteraciones , lista_Fx