
#Metodo de punto fijo

def punto_fijo(g, x0, tol , max_iter):
    """Método Abierto: Iteración de Punto Fijo (x = g(x))."""
    x = x0
    for i in range(max_iter):
        x_nuevo = g(x)
        if abs(x_nuevo - x) < tol:
            return x_nuevo, i + 1
        x = x_nuevo
    return x, max_iter