# 02 · Tratamiento de datos financieros

## El problema de análisis

En el primer módulo representamos inversiones con precios hipotéticos. Para avanzar hacia el estudio de los mercados necesitamos obtener observaciones históricas, comprender su estructura y comprobar que sean adecuadas para los cálculos que realizaremos. Un conjunto de precios descargado no constituye, por sí mismo, una base analítica confiable.

## Qué se aprende

Este módulo introduce la extracción, exploración, validación y transformación de información financiera. Mediante `yfinance` consultamos precios históricos; con `pandas` reconocemos la estructura de los DataFrames, examinamos índices y tipos de datos, identificamos observaciones faltantes y documentamos decisiones de preparación. Posteriormente calculamos rendimientos simples y alineamos las fechas de distintos activos para construir una base comparable.

El propósito es comprender **qué significa cada dato, cómo se obtuvo y qué operaciones permiten utilizarlo responsablemente**, en lugar de limitarse a ejecutar instrucciones.

## Cuaderno de trabajo

**[02 · Tratamiento de datos financieros con Python](02_tratamiento_datos_financieros.ipynb)**

[Abrir en Google Colab](https://colab.research.google.com/github/vyolete/proyecto_analitica_financiera/blob/main/02_financial_data/02_tratamiento_datos_financieros.ipynb)

El cuaderno incluye explicaciones conceptuales, ejemplos con datos históricos, comprobaciones de calidad, visualizaciones y prácticas individuales. La consulta depende de la disponibilidad de la fuente externa.

## Producto esperado

Un notebook reproducible que documente la consulta y preparación de tres activos, compruebe al menos un rendimiento, justifique sus transformaciones y exporte archivos de precios y rendimientos para continuar el análisis exploratorio.

**Estado:** cuaderno disponible; materiales complementarios en preparación.

[← Catálogo de proyectos](../README.md)
