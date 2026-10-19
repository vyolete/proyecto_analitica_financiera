# Programación y analítica financiera con Python

**Financial Analytics Lab** · Proyectos reproducibles de programación aplicada a las finanzas

La información financiera adquiere valor cuando es posible examinarla de manera rigurosa y convertirla en argumentos para la toma de decisiones. Para ello, no basta con producir tablas o gráficos: es necesario comprender de dónde provienen los datos, cómo se transforman, qué representa cada indicador y cuáles son los límites de las conclusiones obtenidas.

Este repositorio reúne una secuencia de proyectos de programación que aborda ese proceso con Python. El recorrido comienza con la formulación de algoritmos y el manejo de estructuras de datos; continúa con la extracción, preparación y exploración de información financiera; y culmina con el desarrollo de una aplicación interactiva que integra cálculos, visualizaciones e interpretación económica.

La programación se utiliza aquí como un instrumento de análisis. Cada proyecto propone una pregunta, presenta los conceptos necesarios para abordarla y deja evidencia del procedimiento seguido para obtener y examinar sus resultados.

## Proyectos

| Módulo | Pregunta de análisis | Contenido |
| --- | --- | --- |
| [01 · Fundamentos de programación](01_python_fundamentals/README.md) | ¿Cómo representar las reglas de una operación comercial mediante un algoritmo? | Variables, operadores, condicionales, ciclos, funciones y estructuras de datos. |
| [02 · Tratamiento de datos financieros](02_financial_data/README.md) | ¿Qué debe verificarse antes de utilizar precios históricos en un análisis? | Fuentes públicas, yfinance, pandas, limpieza y validación. |
| [03 · Análisis exploratorio](03_exploratory_analysis/README.md) | ¿Qué revelan los rendimientos sobre el comportamiento de un activo? | Estadística descriptiva, distribuciones y gráficos. |
| [04 · Series temporales financieras](04_time_series/README.md) | ¿Cómo cambia la interpretación de un activo al examinar su evolución en el tiempo? | Fechas, frecuencias, rezagos, medias móviles y volatilidad. |
| [05 · Riesgo y simulación](05_risk_and_simulation/README.md) | ¿Cómo estudiar relaciones entre activos y escenarios de resultados posibles? | Correlación, covarianza, cuantiles y simulación. |
| [06 · Aplicación de analítica financiera](06_financial_app/README.md) | ¿Cómo integrar el análisis en una herramienta que permita explorar activos e interpretar indicadores? | Streamlit, integración de datos, cálculos y visualizaciones. |

## Cómo trabajar con los proyectos

Los módulos siguen una progresión conceptual, pero cada uno conserva su propio problema de análisis. Antes de ejecutar código, conviene identificar qué pregunta se busca responder y qué datos se necesitan. Durante el desarrollo, los resultados deben contrastarse con las definiciones de los indicadores y con las funciones de las librerías utilizadas. Al finalizar, la interpretación debe señalar tanto los hallazgos como los supuestos y limitaciones del procedimiento.

Los cuadernos de trabajo se desarrollarán en Google Colab y podrán consultarse desde las carpetas correspondientes. La aplicación integradora se documentará en el último módulo.

## Herramientas

**Python · Google Colab · NumPy · pandas · yfinance · matplotlib · SciPy · Plotly · Streamlit · GitHub**

Estas herramientas cumplen funciones diferentes dentro del proceso. Python permite expresar algoritmos; pandas y NumPy facilitan el tratamiento cuantitativo; yfinance proporciona acceso a datos históricos; las librerías gráficas permiten examinar patrones; y Streamlit sirve para presentar el análisis en una interfaz interactiva.

## Reproducibilidad y alcance

Un resultado analítico debe poder revisarse y reproducirse. Por eso, cada proyecto documentará sus fuentes, transformaciones, decisiones metodológicas y procedimientos de cálculo. Los datos externos pueden actualizarse o presentar restricciones de acceso. Los resultados históricos describen comportamientos observados y no constituyen una predicción ni una recomendación de inversión.

**Estado del repositorio:** estructura y descripciones iniciales disponibles. Los notebooks, los informes y la aplicación se incorporarán progresivamente; no se presentan como trabajos terminados.

[Documentación](docs/README.md) · [Recursos visuales](assets/README.md) · [Licencia](LICENSE)


## 📚 Wiki académica de analítica financiera

Consulta la [Wiki de analítica financiera con Python](docs/wiki/README.md): fundamentos, calidad de datos, rendimientos, series temporales, riesgo, portafolios, proyecto integrador y bibliografía académica comentada. Complementa los seis notebooks del curso.
