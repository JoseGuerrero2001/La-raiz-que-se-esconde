
#Metodo de newton raphson modificado

def newton_raphson_modificado(f, df, ddf, x0, tol, max_iter ):
    """Método Abierto: Newton-Raphson Modificado (Ideal para raíces múltiples/dobles)."""
    
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x, i + 1

        dfx = df(x)
        ddfx = ddf(x) # Requiere segunda derivada

        denominador = (dfx ** 2) - (fx * ddfx)
        if denominador == 0:
            return None, "Error: Denominador cero en Newton mejorado."

        x_nuevo = x - (fx * dfx) / denominador
        if abs(x_nuevo - x) < tol:
            return x_nuevo, i + 1
        x = x_nuevo
    return x, max_iter