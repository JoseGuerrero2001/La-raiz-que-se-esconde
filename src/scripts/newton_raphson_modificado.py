
#Metodo de newton raphson modificado

def newton_raphson_modificado(f, df, ddf, x0, tol, max_iter ):
    """Método Abierto: Newton-Raphson Modificado (Ideal para raíces múltiples/dobles)."""

    lista_raices = []
    lista_iteraciones = []
    lista_Fx = []

    x = x0
    for i in range(max_iter):


        #print(f"\nIteracion {i + 1}: x = {x}, f(x) = {f(x)}")

        fx = f(x)
        if abs(fx) < tol:
            lista_iteraciones.append(i + 1)
            lista_raices.append(round(x, 6))
            lista_Fx.append(round(fx, 6))
            return lista_raices, lista_iteraciones , lista_Fx

        dfx = df(x)
        ddfx = ddf(x) # Requiere segunda derivada

        denominador = (dfx ** 2) - (fx * ddfx)
        if denominador == 0:
            return None, "Error: Denominador cero en Newton mejorado."

        x_nuevo = x - (fx * dfx) / denominador

        lista_iteraciones.append(i + 1)
        lista_raices.append(round(x_nuevo, 6))
        lista_Fx.append(round(f(x_nuevo), 6))

        if abs(x_nuevo - x) < tol:
            return lista_raices, lista_iteraciones , lista_Fx
        x = x_nuevo
    return lista_raices, lista_iteraciones , lista_Fx