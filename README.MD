# Laboratorio 2: La raíz que se esconde — Computación Numérica

Repositorio desarrollado para la Universidad Católica del Maule (UCM) 

**Autores:** Ricardo Yáñez Vega, Jose Guerrero


## 📁 Descripción del Proyecto
Este proyecto implementa y compara **seis métodos numéricos de búsqueda de raíces** aplicados sobre distintas funciones matemáticas (polinómicas con raíz simple y doble, exponenciales, trigonométricas y mixtas). El sistema evalúa la convergencia de cada método bajo un ambiente controlado con una tolerancia de $1e-6$, exportando automáticamente los resultados tabulares a archivos `.CSV` y generando gráficos comparativos en formato PNG.

## Estructura del Repositorio
```
evaluacion2-busqueda-raices/
│
├── src/                              # Carpeta contenedora de los scripts de Python
│   ├── 1-Main.py                     # Script principal de ejecución y orquestación
│   ├── funciones.py                  # Definición de funciones, derivadas y funciones g(x)
│   ├── biseccion.py                  # Implementación del método de Bisección
│   ├── falsa_posicion.py             # Implementación del método de Falsa Posición
│   ├── punto_fijo.py                 # Implementación del método de Punto Fijo
│   ├── secante.py                    # Implementación del método de la Secante
│   ├── newton_raphson.py             # Implementación de Newton-Raphson estándar
│   └── newton_raphson_modificado.py  # Newton-Raphson para raíces dobles/múltiples
│
├── data/                # Archivos CSV generados automáticamente con los datos (X, F(x), Iteraciones)
├── assets/              # Gráficos PNG de convergencia generados por Matplotlib
├── requirements.txt     # Dependencias y librerías necesarias del proyecto
└── README.md            # Documentación principal del proyecto

```
## ⚙️ Requisitos y Configuración del Entorno
El proyecto requiere Python 3.x instalado en el sistema. Las librerías obligatorias utilizadas son numpy y matplotlib

1.Clonar el repositorio

BASH
```
git clone <url-del-repositorio>
cd evaluacion2-busqueda-raices

```
3.Instalar las dependencias

BASH
```
pip install -r requirements.txt

```
## ▶️ ¿Cómo ejecutar el proyecto?

1.Dirígete a la carpeta donde se encuentran los scripts de código fuente (src/):

BASH
```
cd src
```

2.Ejecuta el archivo principal:

BASH
```
python 1-Main.py
```

Al finalizar la ejecución, el script se encargará automáticamente de:
* Calcular las raíces para cada método y función bajo el ambiente controlado.
* Guardar los registros iterativos en la carpeta data/ en formato .csv.
* Generar y exportar los gráficos comparativos de convergencia en la carpeta assets/ en formato .png

## 📊 Métodos Implementados

1. Bisección (Método cerrado basado en el teorema de Bolzano).
2. Falsa Posición / Regula Falsi (Método cerrado con interpolación lineal).
3. Punto Fijo (Método abierto basado en la iteración $x = g(x)$).
4. Secante (Método abierto sin requerir derivadas analíticas).
5. Newton-Raphson (Método abierto de convergencia cuadrática).
6. Newton-Raphson Modificado (Optimizado para el análisis de raíces dobles / tangencia al eje).


