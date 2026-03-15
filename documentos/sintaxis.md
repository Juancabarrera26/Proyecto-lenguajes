# Sintaxis del lenguaje JCDS

## Introduccion

La sintaxis de un lenguaje de programacion define el conjunto de reglas que permiten escribir instrucciones validas dentro del lenguaje. En el caso de JCDS, la sintaxis fue disenada con el objetivo de ser clara, sencilla y orientada a procesos de analisis de datos, aprendizaje automatico y Deep Learning.

El lenguaje JCDS toma inspiracion de lenguajes como Python, C, Java y Haskell, buscando una sintaxis que combine legibilidad, estructura y facilidad de uso. Su diseno permite representar operaciones matematicas, manipulacion de matrices, control de flujo y funciones relacionadas con procesamiento de datos y modelos de aprendizaje.

En esta etapa del proyecto se presenta una propuesta inicial de la sintaxis del lenguaje, la cual servira como base para la definicion de la gramatica en ANTLR y para la futura implementacion del interprete en Python.

---

## Principios de diseno de la sintaxis

La sintaxis de JCDS fue definida con base en los siguientes principios:

- claridad en la escritura de instrucciones
- facilidad de lectura
- cercania con notaciones conocidas en otros lenguajes
- representacion directa de operaciones del dominio
- posibilidad de extension en futuras etapas del proyecto

---

## Estructura general del lenguaje

Un programa en JCDS estara compuesto por una secuencia de instrucciones. Cada instruccion representara una operacion valida dentro del lenguaje, como asignaciones, operaciones matematicas, operaciones con matrices, estructuras de control o funciones del dominio.

Ejemplo general:

```txt
a = 5 + 3
b = a * 2
print(b)
```
