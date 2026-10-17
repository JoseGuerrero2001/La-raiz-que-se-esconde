
#Metodo de la secante

def secante(f, x0, x1, tol, max_iter):
    for i in range(max_iter):
        fx0, fx1 = f(x0), f(x1)
        if fx1 - fx0 == 0:
            return None, "Error: Division por cero en el metodo de la sec."
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x2 - x1) < tol or abs(f(x2)) < tol:
            return x2, i + 1
        x0, x1 = x1, x2
    return x1, max_iter