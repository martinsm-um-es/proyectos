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

Los archivos principales incluidos en esta entrega son:

- **`main.ipynb`**: Cuaderno Jupyter que contiene todo el flujo de trabajo documentado, con las celdas ejecutadas mostrando los resultados del análisis y procesamiento.
- **`BM25.py`**: Script de Python con la implementación de la clase y métodos para la vectorización utilizando el algoritmo BM25.
- **`datos_proyecto.zip`**: Dataset comprimido que contiene los datos en crudo recopilados de Reddit en formato JSON.
- **`output_proyecto.zip`**: Archivo comprimido con todas las salidas y documentos generados por el sistema (también en JSON).

## Notas Adicionales

*   Este repositorio contiene los archivos esenciales requeridos para la entrega.
*   No se incluyen archivos auxiliares no solicitados.
*   Debido a limitaciones de tamaño, no se incluyen los pesos del modelo con fine-tuning ni el tokenizador utilizado en fases avanzadas del proyecto.
