# Wiki académica · Analítica financiera con Python

**Lenguajes de Programación · Ingeniería Financiera · ITM**

Esta wiki es un texto de consulta y autoaprendizaje. Complementa, pero no sustituye, los notebooks de la carpeta principal del repositorio. Su objetivo es **formular preguntas financieras, obtener datos, calcular indicadores correctamente, interpretarlos y comunicar conclusiones con límites claros**.

> Uso académico. Los resultados históricos no constituyen recomendaciones de inversión ni garantizan rendimientos futuros.

## Ruta de lectura

| Unidad | Pregunta que responde | Guía | Laboratorio |
|---|---|---|---|
| 0 | ¿Qué significa hacer analítica financiera? | [Fundamentos y método](00_fundamentos.md) | [Notebook 01](../../aprendizaje/01_fundamentos/01_fundamentos_analizador_inversiones.ipynb) |
| 1 | ¿Cómo obtener datos financieros confiables? | [Datos y calidad](01_datos_financieros.md) | [Notebook 02](../../aprendizaje/02_datos_financieros/02_tratamiento_datos_financieros.ipynb) |
| 2 | ¿Qué rentabilidad y dispersión presentan los activos? | [Análisis exploratorio](02_analisis_exploratorio.md) | [Notebook 03](../../aprendizaje/03_analisis_exploratorio/03_analisis_exploratorio_portafolio.ipynb) |
| 3 | ¿Cómo cambia el comportamiento a través del tiempo? | [Series temporales](03_series_temporales.md) | [Notebook 04](../../aprendizaje/04_series_temporales/04_series_temporales_financieras.ipynb) |
| 4 | ¿Cómo medir riesgo y diversificación? | [Riesgo y portafolios](04_riesgo_portafolios.md) | [Notebook 05](../../aprendizaje/05_riesgo_simulacion/05_riesgo_simulacion_portafolio.ipynb) |
| 5 | ¿Cómo comunicar el análisis en una aplicación? | [Proyecto y Streamlit](05_proyecto_aplicacion.md) | [Notebook 06](../../aprendizaje/06_streamlit/06_guia_streamlit.ipynb) |
| Referencias | ¿Dónde profundizar y verificar? | [Bibliografía comentada](referencias.md) | [Cuaderno integrador](../../evaluaciones/02_proyecto_analisis_portafolio/Proyecto_1_Analisis_Portafolio.ipynb) |

## Cómo estudiar cada unidad

1. **Plantear una pregunta** que pueda responderse con datos: «¿Cuál de dos activos tuvo mayor volatilidad diaria durante el mismo periodo?».
2. **Leer la explicación** y comprender las unidades de las fórmulas.
3. **Reproducir el ejemplo** numérico antes de ejecutar código.
4. **Abrir el notebook** en Colab y realizar los ejercicios con datos descargados.
5. **Interpretar**, no solo graficar: señalar periodo, frecuencia, moneda, fuente y limitaciones.
6. **Documentar** decisiones y resultados en Markdown.
7. **Guardar una copia individual** en GitHub y compartir el enlace cuando la actividad lo solicite.

## Convenciones de esta wiki

- Los rendimientos se calculan como **fracciones** (0.05 significa 5 %) salvo que se indique lo contrario.
- Las medidas anualizadas dependen de la **frecuencia** de los datos y de supuestos explícitos.
- Se distingue entre **precios ajustados y no ajustados**, entre **rendimientos simples y logarítmicos**, y entre **riesgo histórico y riesgo futuro**.
- Una correlación es una asociación estadística, no una relación causal.
- Los ejemplos son ilustrativos y no representan asesoría financiera.

## Competencia final

Al finalizar, el estudiante podrá entregar un informe reproducible de un portafolio con datos, indicadores, gráficos interpretados, limitaciones metodológicas y una aplicación Streamlit que permita explorar resultados.

[Comenzar por los fundamentos →](00_fundamentos.md)
