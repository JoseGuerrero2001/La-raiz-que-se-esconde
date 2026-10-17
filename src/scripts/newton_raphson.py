
#Metodo de Newton-Raphson

def newton_raphson(f, df, x0, tol, max_iter):

    lista_raices = []
    lista_iteraciones = []
    lista_Fx = []


    x = x0
    for i in range(max_iter):

        lista_iteraciones.append(i + 1)
        lista_raices.append(round(x, 6))
        lista_Fx.append(round(f(x), 6))

        fx = f(x)
        if abs(fx) < tol:
            return lista_raices, lista_iteraciones , lista_Fx

        dfx = df(x)
        if dfx == 0:
            return None, "Error: Derivada = a cero."

        x_nuevo = x - (fx / dfx)
        if abs(x_nuevo - x) < tol:
            return x_nuevo, i + 1
        x = x_nuevo
    return x, max_iter