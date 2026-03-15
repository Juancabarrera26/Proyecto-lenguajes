# Introduccion

En el campo de las ciencias de la computacion, los lenguajes de programacion juegan un papel fundamental en el desarrollo de software y en la solucion de problemas dentro de diferentes areas del conocimiento. Existen lenguajes de proposito general que permiten desarrollar aplicaciones para multiples dominios, pero tambien existen lenguajes disenados para resolver problemas dentro de un contexto especifico. Estos lenguajes se conocen como lenguajes de dominio especifico o DSL (Domain Specific Language).

Un lenguaje de dominio especifico es un lenguaje de programacion disenado para facilitar la expresion de soluciones dentro de un dominio particular. A diferencia de los lenguajes de proposito general, los DSL buscan simplificar la sintaxis y ofrecer instrucciones que representen directamente las operaciones mas comunes dentro de un area especifica.

En este proyecto se propone el diseno de un lenguaje de dominio especifico llamado **JCDS**. Este lenguaje esta orientado a la realizacion de operaciones matematicas, manipulacion de matrices y ejecucion de procesos basicos relacionados con analisis de datos y aprendizaje automatico.

El lenguaje JCDS busca ofrecer una sintaxis clara y sencilla que permita representar operaciones comunes utilizadas en procesos de aprendizaje automatico, como operaciones aritmeticas, manipulacion de matrices, lectura de datos, generacion de graficas y ejecucion de algoritmos de regresion y clasificacion.

El desarrollo del lenguaje se realizara utilizando **ANTLR4** como herramienta para la generacion del analizador lexico y sintactico. A partir de la gramatica definida, ANTLR permitira generar automaticamente el lexer y el parser del lenguaje. Posteriormente, el patron de diseno **Visitor** sera utilizado para recorrer el arbol sintactico generado y ejecutar las operaciones del lenguaje mediante **Python**.

Este proyecto se desarrolla como parte del curso de Lenguajes de Programacion y tiene como objetivo aplicar los conceptos fundamentales relacionados con diseno de lenguajes, analisis lexico, analisis sintactico y ejecucion de instrucciones mediante un interprete.

En el primer corte del proyecto se presenta el diseno conceptual del lenguaje JCDS, incluyendo la definicion del lenguaje, la arquitectura general del sistema, la sintaxis inicial del lenguaje, las operaciones basicas que soportara y la estructura general del proyecto.
