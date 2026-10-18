
#Metodo de la secante

def secante(f, x0, x1, tol, max_iter):

    lista_raices = []
    lista_iteraciones = []
    lista_Fx = []


    for i in range(max_iter):

        lista_iteraciones.append(i + 1)

        fx0, fx1 = f(x0), f(x1)
        if fx1 - fx0 == 0:
            return None, "Error: Division por cero en el metodo de la sec."
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        lista_raices.append(round(x2, 6))
        lista_Fx.append(round(f(x2), 6))

        print(f"\nIteracion {i + 1}: x = {x2}, f(x) = {f(x2)}")

        if abs(x2 - x1) < tol or abs(f(x2)) < tol:
            return lista_raices, lista_iteraciones , lista_Fx
        x0, x1 = x1, x2
    return lista_raices, lista_iteraciones , lista_Fx