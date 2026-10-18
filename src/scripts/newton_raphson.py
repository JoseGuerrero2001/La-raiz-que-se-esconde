
#Metodo de Newton-Raphson

def newton_raphson(f, df, x0, tol, max_iter):

    lista_raices = []
    lista_iteraciones = []
    lista_Fx = []


    x = x0
    for i in range(max_iter):


        fx = f(x)
        if abs(fx) < tol:
            lista_iteraciones.append(i + 1)
            lista_raices.append(round(x, 6))
            lista_Fx.append(round(f(x), 6))
            return lista_raices, lista_iteraciones , lista_Fx

        dfx = df(x)
        if dfx == 0:
            return None, "Error: Derivada = a cero."

        x_nuevo = x - (fx / dfx)

        lista_iteraciones.append(i + 1)
        lista_raices.append(round(x_nuevo, 6))
        lista_Fx.append(round(f(x_nuevo), 6))

        if abs(x_nuevo - x) < tol:
            return lista_raices, lista_iteraciones , lista_Fx
        x = x_nuevo
    return lista_raices, lista_iteraciones , lista_Fx