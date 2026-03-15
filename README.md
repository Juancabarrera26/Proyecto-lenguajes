# JCDS

JCDS (Juan Camilo, Danilo, Sebastian) es un lenguaje de dominio especifico (DSL) disenado para facilitar la definicion y ejecucion de operaciones matematicas, manipulacion de matrices y procesos relacionados con Deep Learning.

Este proyecto hace parte del curso de Lenguajes de Programacion y tiene como objetivo disenar e implementar un lenguaje propio utilizando ANTLR4 y Python.

---

# Objetivos del proyecto

## Objetivo general

Disenar e implementar un lenguaje de dominio especifico capaz de ejecutar operaciones matematicas, manipulacion de matrices y operaciones relacionadas con analisis de datos y procesos basicos de aprendizaje automatico.

## Objetivos especificos

- Disenar la sintaxis del lenguaje JCDS.
- Implementar un analizador lexico y sintactico utilizando ANTLR4.
- Desarrollar un interprete del lenguaje utilizando Python.
- Permitir operaciones matematicas y matriciales.
- Permitir operaciones de procesamiento de datos.
- Integrar algoritmos basicos de aprendizaje automatico.
- Implementar el patron de diseno Visitor para la ejecucion del lenguaje.

---

# Descripcion del lenguaje

Un lenguaje de dominio especifico es un lenguaje disenado para resolver un problema particular dentro de un dominio especifico.

El lenguaje JCDS esta orientado a facilitar tareas relacionadas con analisis de datos, operaciones matematicas, manipulacion de matrices y procesos de aprendizaje automatico mediante una sintaxis sencilla y clara.

El lenguaje toma inspiracion en diferentes lenguajes de programacion como:

- Python
- C
- Java
- Haskell

y busca combinar simplicidad con capacidad para realizar operaciones avanzadas relacionadas con Deep Learning.

---

# Primer corte

En el primer corte del proyecto se presenta el diseno del lenguaje JCDS incluyendo:

- definicion del lenguaje
- objetivos del proyecto
- arquitectura del sistema
- sintaxis inicial del lenguaje
- definicion de operaciones basicas
- estructura del proyecto
- organizacion del repositorio

En esta etapa se desarrolla el diseno conceptual del lenguaje antes de implementar completamente su interprete.

---

# Operaciones soportadas

El lenguaje JCDS permitira realizar diferentes tipos de operaciones.

## Operaciones aritmeticas

El lenguaje permitira realizar operaciones matematicas como:

- suma
- resta
- multiplicacion
- division
- modulo
- potencias
- funciones trigonometricas

Ejemplo de sintaxis posible:
```
a = 5 + 3
b = a * 2
c = sin(45)
```


## Operaciones con matrices

- suma de matrices
- resta de matrices
- multiplicacion de matrices
- matriz inversa
- matriz transpuesta

Ejemplo conceptual:
```
matrix A = [[1,2],[3,4]]
matrix B = [[5,6],[7,8]]

C = A + B
D = transpose(A)
```


## Control de flujo

El lenguaje soportara estructuras de control basicas.

- condicionales
- ciclos for
- ciclos while

Ejemplo conceptual:
```
if a > b {
print(a)
}

for i in range(0,10) {
print(i)
}
```

## Manejo de archivos

El lenguaje permitira leer y escribir archivos de texto.

Ejemplo conceptual:
```
data = read("datos.txt")
write("salida.txt", data)
```


## Procesamiento de datos

El lenguaje incluira funciones basicas relacionadas con aprendizaje automatico.

- regresion lineal
- regresion logistica
- clasificacion usando perceptron multicapa
- algoritmos de agrupamiento
- prediccion usando redes neuronales

Ejemplo conceptual:
```
model = linear_regression(data)
predict(model, new_data)
```

---

# Estructura del proyecto

El proyecto esta organizado en la siguiente estructura de carpetas.

JCDS
├── documentos
│ ├── introduccion.md
│ ├── objetivos.md
│ ├── arquitectura_del_lenguaje.md
│ ├── sintaxis_del_lenguaje.md
│ └── plan_de_desarrollo.md
│
├── gramatica
│ └── JCDS.g4
│
├── ejemplos
│ ├── operaciones_basicas.jcds
│ ├── matrices.jcds
│ ├── regresion.jcds
│ └── clasificador.jcds
│
├── codigo_fuente
│ ├── main.py
│ ├── interprete.py
│ └── visitor.py
│
└── requisitos.txt


## documentos

Contiene la documentacion del diseno del lenguaje, incluyendo objetivos, arquitectura, sintaxis y plan de desarrollo del proyecto.

## gramatica

Contiene la definicion de la gramatica del lenguaje JCDS utilizando ANTLR4.

## ejemplos

Incluye ejemplos de programas escritos utilizando la sintaxis del lenguaje JCDS.

## codigo_fuente

Contiene la implementacion del interprete del lenguaje utilizando Python.

## requisitos.txt

Archivo que define las dependencias necesarias para ejecutar el proyecto.

---

# Tecnologias utilizadas

El desarrollo del lenguaje JCDS utiliza las siguientes tecnologias:

- ANTLR4
- Python
- NumPy
- Matplotlib
- Scikit-learn
- Linux (Ubuntu)
