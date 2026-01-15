# Análisis Estadístico Multivariante - ACB (1983-2023)

Este proyecto realiza un análisis estadístico exhaustivo sobre un dataset histórico de la liga ACB de baloncesto, abarcando desde la temporada 1983-1984 hasta la 2022-2023.

## Descripción

El objetivo es aplicar técnicas de análisis multivariante para extraer conocimiento sobre la evolución de los jugadores y el juego. Se exploran dimensiones como rendimiento, perfiles físicos y eficiencia.

## Tecnologías Utilizadas

- **R & RMarkdown**: Lenguaje principal para el análisis y generación de informes.
- **Tidyverse (dplyr, ggplot2)**: Manipulación de datos y visualización.
- **Técnicas Estadísticas**:
  - **PCA (Análisis de Componentes Principales)**: Para reducir dimensionalidad y detectar arquetipos de jugadores (ej. anotadores vs. defensores).
  - **Clustering (K-means y Jerárquico)**: Agrupación de jugadores por similitud estadística.
  - **Análisis Discriminante (LDA)**: Clasificación de jugadores en posiciones (Base, Alero, Pívot, etc.).
  - **Regresión Lineal Múltiple**: Predicción de la valoración del jugador basada en estadísticas de juego.

## Estructura del Proyecto

- `src/`: Código fuente en RMarkdown (`.Rmd`).
- `data/`: Datasets utilizados (histórico y temporada 22-23).
- `figures/`: Gráficos generados durante el análisis.
