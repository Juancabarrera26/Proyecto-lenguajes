# JCDS

JCDS abreviado en (Juan Camilo, Danilo, sebastian) es un lenguaje de dominio especifico (DSL) disenado para facilitar la definicion y ejecucion de operaciones matematicas, manipulacion de matrices y procesos basicos relacionados con analisis de datos, aprendizaje automatico y Deep Learning.

Este proyecto se desarrolla como parte del curso de Lenguajes de Programacion y tiene como objetivo disenar e implementar un lenguaje propio utilizando ANTLR4 y Python.

---

# Descripcion del proyecto

Un lenguaje de dominio especifico es un lenguaje de programacion disenado para resolver problemas dentro de un dominio particular. A diferencia de los lenguajes de proposito general, un DSL esta orientado a simplificar tareas especificas dentro de un area determinada.

El lenguaje JCDS esta orientado a procesos de analisis de datos y aprendizaje automatico. Su objetivo es permitir que el usuario pueda escribir instrucciones simples para realizar operaciones matematicas, manipulacion de matrices, procesamiento de datos y ejecucion de algoritmos de aprendizaje automatico.

El lenguaje sera implementado utilizando ANTLR4 para el analisis lexico y sintactico. A partir de la gramatica definida, ANTLR permitira generar automaticamente el lexer y el parser del lenguaje. Posteriormente, el patron de diseno Visitor sera utilizado para recorrer el arbol sintactico generado y ejecutar las operaciones del lenguaje mediante Python.

---

# Objetivos del proyecto

## Objetivo general

Disenar un lenguaje de dominio especifico orientado a procesos de Deep Learning que permita ejecutar operaciones matematicas, manipulacion de matrices y operaciones basicas relacionadas con analisis de datos y aprendizaje automatico.

## Objetivos especificos

- Disenar la estructura general del lenguaje JCDS.
- Definir la sintaxis del lenguaje para representar operaciones matematicas, matrices y procesamiento de datos.
- Definir la gramatica del lenguaje utilizando ANTLR4.
- Implementar el analisis lexico y sintactico del lenguaje.
- Utilizar el patron de diseno Visitor para ejecutar las instrucciones del lenguaje.
- Integrar el lenguaje con Python para ejecutar las operaciones del DSL.

Los detalles completos del diseno del lenguaje se encuentran en la carpeta `documentos`.

---

# Alcance del primer corte

En el primer corte del proyecto se presenta el diseno conceptual del lenguaje JCDS. Esta etapa se enfoca en definir la estructura del lenguaje y los componentes necesarios para su implementacion.

En esta fase se incluyen:

- definicion del lenguaje
- arquitectura general del sistema
- sintaxis inicial del lenguaje
- operaciones basicas soportadas
- estructura del proyecto
- organizacion del repositorio

La documentacion detallada de estos elementos se encuentra dentro de la carpeta `documentos`.

---

# Arquitectura general

El funcionamiento del lenguaje JCDS sigue el siguiente flujo:

Programa escrito en JCDS  
↓  
Lexer generado con ANTLR  
↓  
Parser generado con ANTLR  
↓  
Parse Tree  
↓  
Visitor Pattern  
↓  
Ejecucion en Python  
↓  
Resultados

El patron Visitor sera utilizado para recorrer el arbol sintactico generado por ANTLR y ejecutar las instrucciones definidas en el lenguaje.

Una explicacion mas detallada de esta arquitectura se encuentra en `documentos/arquitectura_del_lenguaje.md`.

---

# Operaciones del lenguaje

El lenguaje JCDS esta disenado para soportar diferentes tipos de operaciones relacionadas con matematicas, matrices y procesamiento de datos.

Entre las principales capacidades del lenguaje se incluyen:

- operaciones aritmeticas
- manipulacion de matrices
- estructuras de control
- manejo de archivos
- generacion de graficas
- modelos de regresion
- clasificacion utilizando perceptron multicapa
- algoritmos de agrupamiento
- prediccion de datos

La sintaxis completa del lenguaje y ejemplos detallados se encuentran en:

---

# Estructura del proyecto

El proyecto esta organizado en la siguiente estructura de carpetas.
```
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
```

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
