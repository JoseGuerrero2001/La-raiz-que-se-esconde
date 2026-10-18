Resolución de dudas generadas durante la resolución del trabajo.

1.- ¿Qué método convergió en menos iteraciones en cada función?, ¿Por qué?

Res: En la función Polinómica (Raíz simple): Empataron Secante, Newton-Raphson y Newton-Raphson modificado, con 6 iteraciones.
En polinómica (Raíz doble): El método de la Secante convirgió en 1 iteracion.
En la función Exponencial, empataron la Secante, Newton-Raphson y Newton-Raphson Modificado con 4 iteraciones.
En trigonométrica, el método de la Secante fue superior a las demás con 4 iteraciones. 
Y en la función mixta, el método más rapido fue de la Secante con 3 iteraciones.

Las razones de estos resultados se deben a lo siguiente: 
a) En las raíces simples, los métodos abiertos como Newton-Raphson y modificado poseen convergencia cuadrática, mientras que la Secante posee convergencia superlineal. Esto permite corregir el error a una tasa mucho mayor que los métodos de Bisección o de punto fijo.
b) En raíces múltiples, la primera derivada se anula, lo que provoca que Newton-Raphson pierda su velocidad cuadrática y se degrade a lineal, y que la Secante o Punto fijo se estanquen (100 iteraciones). El Newton-Raphson modificado, en teoría, restablece la convergencia cuadrática, por eso encuentra la raíz en solo 2 iteraciones.
c) En funciones Trigonométrica y Mixta, la Secante fue la más rápida debido a la pendiente secante generada por sus puntos iniciales, lo que ofreció un paso de corrección más favorable. Por ende, en la función Mixta, Newton-Raphson Mod. no pudo concluir debido a una indeterminación por dominio (evaluado en raíz negativa)
d)Los métodos más lentos: El método de bisección muestra un comportamiento constante debido a su convergencia lineal fija de factor 1/2, a diferencia de Punto fijo y falsa posición dependieron demasiado de la derivada local, retrasando su avance.

2.- ¿Qué orden de convergencia tiene cada método y cómo se refleja en el gráfico |error| vs iteración?

Res: 


3.- ¿Qué métodos requieren un intervalo con cambio de signo y cuáles no?

Res: Los métodos que requieren el cambio de signo son: Bisección y Falsa Posición.

Mientras, los que no requieren intervalo con cambio de signo son: Punto fijo, Secante, Newton-Raphson y Newton-Raphson Mod.

4.- En la función que toca el eje x (raíz doble): ¿qué métodos fallan o no aplican y cuál se comporta mejor?, ¿Por qué?

Res: Los métodos que fallan o no aplican son el Punto Fijo y el método de Newton-Raphson. El primero es un método que falla o se estanca, alcanzando el límite desproporcionado de 100 iteraciones, sin converger adecuadamente.
El segundo, Newton-Raphson presenta un comportamiento deficiente al requerir 11 iteraciones.
Ahora bien, los que mejor se comportan son el metodo de la secante y el Newton-Raphson Modificada, al sólo requerir 1 y 2 iteraciones respectivamente. En todo caso, Newton-Raphson Modificado es el método teóricamente superior y más funcional al momento de manejar raíces múltiples.

El motivo de esto se debe a múltiples factores:

a) La raiz doble: Al tener la curva de la función una tangente al eje x, en la raiz r se cumple simultáneamente que f{r}= 0 y f'{r}=0.
b) Ralentizamiento de Punto Fijo: Al anularse la derivada de la función original, la función de iteración pierde la condición estricta de contracción, provocando que los pasos de correción sean insignificantes y el método que atrapado en un bucle de convergencia lenta.
c) Se ralentiza Newton-Raphson: Este se divide por la primera derivada. Al aproximarse a una raíz doble, la presencia de esta derivada nula degrada el orden de convergencia del método cuadrático a lineal, provocando el triple de iteraciones necesarias respecto a una raíz simple.

d) La secante requirió solo 1 iteración: En este caso, en una función con raíz doble, se resuelve por una coincidencia geométrica favorable de los puntos iniciales dados, donde la recta secante proyectó la intersección con el eje x precisamente en el vértice, la raíz que buscabamos.


5.- ¿Cómo influyen el intervalo inicial y la estimación inicial en la cantidad de iteraciones y en si el método converge?

Res: Respecto a la cantidad de iteraciones: una estimación inicial o un par de puntos bien ubicados, reducen significativamente el número de pasos en métodos abiertos (por ejemplo, la secante que se resolvió en 1 iteración).
En métodos de intervalo como Bisección, cuanto más grande sea el intervalo inicial, mayor será el número de iteraciones necesarias para reducir la tolerancia a la mitad en cada paso.

Sobre si el método converge: 
a)En métodos cerrados: La elección de un intervalo con cambio de signo garantiza la convergencia por el Teorema de Bolzano.

b)En métodos abiertos: La convergencia no está garantizada y depende estrictamente de la estimación inicial. Un punto x[0] lejano o inadecuado puede hacer que el método diverja si |g'(x)|>= 1, si la derivada se aproxima a cero f'(x) = 0, o si las iteraciones salen del dominio real de la función.

6.- ¿Qué método recomiendan según el tipo de función, considerando el compromiso entre velocidad y robustez?

Res:
Se respondera por apartados para precisar el tipo de problema, el método recomendado y el compromiso velocidad/robustez:
a) Raíz simple (con buena estimación inicial), aplicar método Secante y Newton-Raphson. Su máxima velocidad es 3 a 6 iteraciones, la secante se prefiere por no requerir derivadas.

b) Búsqueda ciega o sin estimación confiable, aplicar método de Bisección. Tiene una velocidad baja (20 iteraciones), pero posee una máxima robustez garantizada por el Teorema de Bolzano.

c) Raíz múltiple o doble conocida, aplicar método de Newton-Raphson modificado. Posee una velocidad excepcional (2 iteraciones) y alta robustez, al evitar los fallos de los métodos tradicionales.

d) Evitar por completo el método de Punto Fijo, debido a un poble desempeño, como las 100 iteraciones en raíces múltiples y mixtas, debido a una débil condición de contracción.

Conclusión final: 
_ 