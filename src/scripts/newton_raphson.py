
#Metodo de Newton-Raphson

def newton_raphson(f, df, x0, tol, max_iter):

    lista_raices = []
    lista_iteraciones = []
    lista_Fx = []


    x = x0
    for i in range(max_iter):

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a7725f4a3ccfecb2522521fe72a23fdcc1d49b91
        if x < 0:
            print(f"Error: El valor de x ({x}) salió del dominio válido (x < 0).")
            return None, None, None



<<<<<<< HEAD
=======
>>>>>>> main
=======
>>>>>>> a7725f4a3ccfecb2522521fe72a23fdcc1d49b91

        fx = f(x)
        if abs(fx) < tol:
            lista_iteraciones.append(i + 1)
            lista_raices.append(round(x, 6))
            lista_Fx.append(round(f(x), 6))
            return lista_raices, lista_iteraciones , lista_Fx

        dfx = df(x)
        if dfx == 0:
            print("Error: Derivada = a cero.")
            return None, None, None

        x_nuevo = x - (fx / dfx)
<<<<<<< HEAD
<<<<<<< HEAD
        
=======

>>>>>>> main
=======
        
>>>>>>> a7725f4a3ccfecb2522521fe72a23fdcc1d49b91
        lista_iteraciones.append(i + 1)
        lista_raices.append(round(x_nuevo, 6))
        lista_Fx.append(round(f(x_nuevo), 6))

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> main
=======

>>>>>>> a7725f4a3ccfecb2522521fe72a23fdcc1d49b91
        if abs(x_nuevo - x) < tol:
            return lista_raices, lista_iteraciones , lista_Fx
        x = x_nuevo
    return lista_raices, lista_iteraciones , lista_Fx