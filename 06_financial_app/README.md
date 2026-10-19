# 06 · Aplicación de analítica financiera con Streamlit

## El problema de análisis

Los notebooks permiten explorar datos y verificar fórmulas, pero una aplicación interactiva debe organizar esas operaciones en un flujo comprensible para otras personas. El usuario necesita seleccionar activos, definir un período, examinar indicadores y comprender las limitaciones de los resultados.

Este módulo integra la programación, el tratamiento de datos, el análisis exploratorio, las series temporales y las medidas de riesgo desarrolladas anteriormente. El resultado es **una aplicación que evoluciona en dos versiones**, no dos proyectos independientes.

## Guía de aprendizaje

**[06 · Construcción de una aplicación de analítica financiera](06_guia_streamlit.ipynb)**

[Abrir guía en Google Colab](https://colab.research.google.com/github/vyolete/proyecto_analitica_financiera/blob/main/06_financial_app/06_guia_streamlit.ipynb)

La guía presenta la arquitectura de Streamlit, las validaciones, la comprobación de cálculos y la progresión entre versiones. El notebook explica el código, pero **la interfaz de Streamlit se ejecuta desde una terminal**.

## Primera versión: analizador individual

**[Código fuente · app.py](app.py)**

Esta aplicación permite seleccionar un activo y un rango de fechas, consultar cierres históricos, calcular rendimiento acumulado del precio y volatilidad por observación, visualizar la trayectoria y descargar los datos. Incluye validación de fechas, manejo de errores e interpretación básica.

## Versión ampliada: portafolio comparativo

**[Código fuente · app_final.py](app_final.py)**

La ampliación permite seleccionar varios activos, asignar ponderaciones, estudiar correlaciones y calcular rendimiento acumulado, volatilidad y máximo drawdown del portafolio. Se explicita el supuesto de **reequilibrio a pesos constantes por observación** y se documentan las limitaciones.

## Cómo ejecutar desde Google Colab

**No es necesario instalar Python ni Streamlit en el computador.** Abre la [guía interactiva en Colab](https://colab.research.google.com/github/vyolete/proyecto_analitica_financiera/blob/main/06_financial_app/06_guia_streamlit.ipynb) y ejecuta sus celdas en orden. El notebook instala las bibliotecas en la sesión temporal, descarga el código del repositorio, inicia el servidor Streamlit y permite intentar abrir la interfaz mediante las funciones de acceso a puertos de Colab.

La versión inicial utiliza `app.py`; la versión ampliada utiliza `app_final.py`. Para cambiar entre ambas, sigue las instrucciones del notebook.

**Limitación:** la apertura de la interfaz depende del soporte de proxy de Colab y puede no funcionar en todas las sesiones. La aplicación no permanece publicada cuando finaliza la sesión. Conserva el código y las evidencias en GitHub; no uses el enlace temporal como única evidencia.

La ejecución local o el despliegue permanente son alternativas opcionales, **no requisitos de este recorrido**.

## Hitos de desarrollo y evidencia

| Hito | Producto | Evidencia diferenciada |
|---|---|---|
| S27 · Primera versión | Aplicación funcional de un activo | Código, ejecución, cálculos, gráfico e interpretación |
| S33 · Ampliación | Aplicación comparativa de varios activos | Indicadores de portafolio, validaciones, análisis y documentación |
| S34 · Defensa | Explicación individual de la solución | Demostración, justificación de fórmulas y modificación del código |

Estos hitos describen una progresión académica propuesta. Su equivalencia con actividades y porcentajes evaluativos del curso requiere la autorización correspondiente.

## Criterios de reproducibilidad

Se registran fuentes, parámetros de descarga y supuestos. La consulta de Yahoo Finance depende de un servicio externo; los resultados pueden cambiar. Las aplicaciones no incluyen comisiones, impuestos ni aportes o retiros. Las estadísticas históricas y los escenarios calculados **no son predicciones ni recomendaciones de inversión**.

[← Catálogo de proyectos](../README.md)
