# Instrucciones para probar la calculadora JCDS en Ubuntu

Este documento explica como ejecutar la calculadora del lenguaje JCDS en Ubuntu.

## 1. Entrar al proyecto

Abrir una terminal y escribir:

```bash
cd ~/JCDS
```

## 2. Entrar a la carpeta de la gramatica

```bash
cd gramatica 
```
## 3. Generar nuevamente el lexer, parser y visitor

```bash
antlr4 -Dlanguage=Python3 -visitor JCDS.g4
```
## 4. Copiar los archivos generados a la carpeta codigo_fuente

```bash
cp JCDSLexer.py ../codigo_fuente/
cp JCDSParser.py ../codigo_fuente/
cp JCDSVisitor.py ../codigo_fuente/
```
## 5. Entrar a la carpeta del codigo fuente

```bash
cd ../codigo_fuente
```
