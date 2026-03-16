
# Arquitectura del lenguaje JCDS

## Introduccion

La arquitectura de un lenguaje de programacion define la estructura y los componentes que participan en el proceso de interpretacion y ejecucion de un programa escrito en dicho lenguaje. En el caso del lenguaje JCDS, la arquitectura fue disenada siguiendo los principios clasicos utilizados en la construccion de compiladores e interpretes.

El objetivo de esta arquitectura es permitir que un programa escrito en el lenguaje JCDS pueda ser procesado, analizado y ejecutado utilizando herramientas modernas de analisis lexico y sintactico. Para lograr esto, el proyecto utiliza ANTLR4 para generar automaticamente el lexer y el parser del lenguaje, y Python para ejecutar las operaciones definidas en el DSL.

La arquitectura del sistema permite separar claramente las diferentes etapas del procesamiento del lenguaje, lo que facilita su implementacion, mantenimiento y extension en futuras etapas del proyecto.

---

# Flujo general del sistema

El procesamiento de un programa escrito en JCDS sigue una serie de etapas que transforman el codigo fuente en instrucciones ejecutables.

El flujo general del sistema es el siguiente:

Programa escrito en JCDS  
↓  
Analisis lexico (Lexer)  
↓  
Analisis sintactico (Parser)  
↓  
Construccion del Parse Tree  
↓  
Recorrido del arbol mediante Visitor  
↓  
Ejecucion de operaciones en Python  
↓  
Resultados

Cada una de estas etapas cumple una funcion especifica dentro del proceso de ejecucion del lenguaje.

---

# Programa fuente

El programa fuente es el archivo escrito por el usuario utilizando la sintaxis definida por el lenguaje JCDS.

Estos archivos utilizan la extension `.jcds` y contienen las instrucciones que describen las operaciones que el lenguaje debe ejecutar.

Ejemplo de programa fuente:
```
matrix A = [[1,2],[3,4]]
matrix B = [[5,6],[7,8]]

C = A + B
print(C)

data = read("datos.txt")

model = linear_regression(data)
result = predict(model, data)

print(result)
```

Este archivo sera el punto de entrada para el procesamiento del lenguaje.

---

# Analisis lexico

El analisis lexico es la primera etapa del procesamiento del programa. En esta etapa se encarga de leer el codigo fuente y dividirlo en unidades basicas llamadas tokens.

Un token representa un elemento del lenguaje, como:

- identificadores
- numeros
- operadores
- palabras reservadas
- simbolos especiales

ANTLR4 genera automaticamente el lexer a partir de la gramatica definida en el archivo `JCDS.g4`.

El lexer se encarga de transformar el texto del programa en una secuencia de tokens que luego sera procesada por el parser.

---

# Analisis sintactico

La segunda etapa del procesamiento es el analisis sintactico. En esta fase se verifica que la secuencia de tokens generada por el lexer cumpla con las reglas de la gramatica del lenguaje.

El parser analiza la estructura del programa y determina si las instrucciones estan escritas correctamente segun las reglas del lenguaje.

ANTLR4 genera automaticamente el parser a partir de la gramatica definida. Este parser es responsable de construir una representacion estructurada del programa conocida como arbol sintactico o parse tree.

---

# Parse Tree

El parse tree es una representacion jerarquica del programa fuente. Este arbol refleja la estructura sintactica del programa segun las reglas definidas en la gramatica del lenguaje.

Cada nodo del arbol representa una construccion del lenguaje, como una expresion, una asignacion, una operacion aritmetica o una estructura de control.

El parse tree permite analizar la estructura del programa de forma organizada y facilita la ejecucion de las instrucciones mediante recorridos del arbol.

---

# Patron Visitor

Para ejecutar las instrucciones del lenguaje, el proyecto utiliza el patron de diseno Visitor.

El patron Visitor permite recorrer el parse tree generado por ANTLR y ejecutar acciones especificas en cada tipo de nodo del arbol.

Por ejemplo, cuando el Visitor encuentra:

- una operacion aritmetica, ejecuta el calculo correspondiente
- una operacion con matrices, realiza la operacion utilizando librerias de Python
- una instruccion condicional, evalua la condicion
- una funcion del dominio, ejecuta la logica correspondiente

Este patron permite separar claramente la estructura del lenguaje de la logica de ejecucion.

---

# Ejecucion en Python

La ejecucion de las operaciones del lenguaje se realiza utilizando Python. Python se encarga de realizar los calculos, manipulacion de matrices, generacion de graficas y ejecucion de algoritmos de aprendizaje automatico.

Para esto se utilizaran diferentes librerias especializadas, entre ellas:

- NumPy para operaciones con matrices
- Matplotlib para generacion de graficas
- Scikit-learn para algoritmos de regresion y clasificacion

Python recibe las instrucciones interpretadas por el Visitor y ejecuta las operaciones correspondientes.

---

# Componentes del sistema

La arquitectura del proyecto se organiza en diferentes componentes dentro del repositorio.

## Documentacion

La carpeta `documentos` contiene la documentacion relacionada con el diseno del lenguaje.

## Gramatica

La carpeta `gramatica` contiene el archivo `JCDS.g4` donde se define la gramatica del lenguaje.

## Ejemplos

La carpeta `ejemplos` contiene programas escritos en el lenguaje JCDS que sirven como ejemplos de uso del lenguaje.

## Codigo fuente

La carpeta `codigo_fuente` contiene la implementacion del interprete del lenguaje utilizando Python y el patron Visitor.

---

# Integracion de componentes

Los componentes del sistema trabajan de forma integrada para permitir la ejecucion del lenguaje.

1. El usuario escribe un programa en JCDS.
2. El lexer generado por ANTLR analiza el codigo fuente y produce tokens.
3. El parser analiza los tokens y construye el parse tree.
4. El Visitor recorre el arbol sintactico.
5. Python ejecuta las operaciones correspondientes.
6. El sistema produce los resultados del programa.

---

# Conclusion

La arquitectura del lenguaje JCDS fue disenada siguiendo los principios clasicos de construccion de interpretes y compiladores. La separacion de etapas entre analisis lexico, analisis sintactico y ejecucion permite construir un sistema modular y extensible.

El uso de ANTLR4 facilita la generacion automatica del lexer y el parser, mientras que el patron Visitor permite implementar de forma clara la logica de ejecucion del lenguaje. Python se encarga de realizar las operaciones necesarias para el dominio del lenguaje, incluyendo calculos matematicos, manipulacion de matrices y algoritmos de aprendizaje automatico.

Esta arquitectura constituye la base para la implementacion completa del lenguaje JCDS en las siguientes etapas del proyecto.

