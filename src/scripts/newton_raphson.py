
#Metodo de Newton-Raphson

def newton_raphson(f, df, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x, i + 1

        dfx = df(x)
        if dfx == 0:
            return None, "Error: Derivada = a cero."

        x_nuevo = x - (fx / dfx)
        if abs(x_nuevo - x) < tol:
            return x_nuevo, i + 1
        x = x_nuevo
    return x, max_iter