# Proyecto de Procesamiento del Lenguaje Natural (PLNE) - Análisis de Reddit

Este proyecto realiza una compilación y análisis de un corpus de datos extraído de Reddit como parte de la asignatura de Procesamiento del Lenguaje Natural (PLNE) en el grado de Ciencia e Ingeniería de Datos (GCID) de la Universidad de Murcia.

## Descripción

El objetivo del proyecto es aplicar técnicas de recuperación y procesamiento de texto sobre datos reales. El trabajo documentado abarca desde la recolección de datos de distintos subreddits hasta la implementación de modelos de vectorización y búsqueda como BM25.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Jupyter Notebook**: Para la documentación y ejecución interactiva del código.
- **BM25**: Implementación propia del algoritmo de ranking probabilístico para recuperación de información.
- **JSON**: Formato estándar para el almacenamiento de los datos recopilados y procesados.

## Estructura del Repositorio

El proyecto se organiza en la carpeta `proyecto_plne/` con la siguiente estructura:

- **src/**: Contiene el código fuente.
  - `main.ipynb`: Cuaderno principal con el análisis y ejecución.
  - `BM25.py`: Módulo de implementación del algoritmo BM25.
- **data/**: Contiene los conjuntos de datos y salidas.
  - `datos_proyecto.zip`: Datos crudos en JSON.
  - `output_proyecto.zip`: Resultados generados.
- **proyecto_plne.pdf**: Versión en PDF del cuaderno para facilitar su lectura.
- **README.md**: Información general del proyecto.

## Notas Adicionales

*   Este repositorio contiene los archivos esenciales requeridos para la entrega.
*   No se incluyen archivos auxiliares no solicitados.
*   Debido a limitaciones de tamaño, no se incluyen los pesos del modelo con fine-tuning ni el tokenizador utilizado en fases avanzadas del proyecto.
