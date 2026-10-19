# 5 · Proyecto integrador y aplicación financiera

[← Índice](README.md) · [← Riesgo](04_riesgo_portafolios.md) · [Bibliografía →](referencias.md)

## Caso integrador

**Rol:** analista financiero que prepara un informe reproducible sobre un portafolio de activos cotizados.

**Pregunta:** ¿qué combinación de activos permite describir de manera razonada la relación histórica entre rendimiento, riesgo y diversificación, dentro de un periodo y supuestos explícitos?

## Producto 1 · Informe analítico en Colab

1. **Pregunta y alcance**: activos, tickers, fechas, moneda, frecuencia.
2. **Datos**: proveedor, ajustes, controles de calidad y observaciones descartadas.
3. **Cálculos**: rendimientos, estadísticas, acumulados, correlación y volatilidad.
4. **Series temporales**: medias móviles, volatilidad móvil y drawdown.
5. **Portafolio**: pesos justificados, rendimiento y riesgo históricos.
6. **Interpretación**: responder la pregunta con números y gráficos.
7. **Limitaciones**: sesgos de selección, costos, ajustes, cambios de régimen y datos faltantes.
8. **Reproducibilidad**: celdas ejecutables, versiones de bibliotecas y enlace individual de GitHub.

[Cuaderno integrador de nivelación](../../evaluaciones/02_proyecto_analisis_portafolio/Proyecto_1_Analisis_Portafolio.ipynb).

## Producto 2 · Aplicación Streamlit

La app debe permitir seleccionar activos y fechas, consultar o cargar datos, revisar advertencias y mostrar métricas y gráficos. Separar las funciones de obtención, cálculo y visualización cuando sea posible.

Ejemplo mínimo:

```python
import streamlit as st

st.title("Analítica de portafolios")
activo = st.selectbox("Selecciona un activo", ["AAPL", "MSFT", "JPM"])
st.write("Activo elegido:", activo)
st.info("Ejemplo de interfaz; aún no descarga ni valida datos.")
```

Para iniciar localmente: `streamlit run app.py`. En Colab puede editarse el archivo, pero ejecutar y publicar una aplicación requiere un entorno compatible y configuración adicional.

## Rúbrica formativa sugerida (100 puntos)

| Criterio | Puntos |
|---|---:|
| Definición del problema y alcance | 10 |
| Calidad, trazabilidad y preparación de datos | 20 |
| Cálculos correctos y comprobaciones | 25 |
| Gráficos e interpretación financiera | 20 |
| Reproducibilidad y organización del código | 15 |
| Limitaciones y conclusiones | 10 |

La rúbrica es **orientativa**, no sustituye las ponderaciones institucionales ni las aprobaciones docentes de EduApp.

## Sustentación individual

Pedir al estudiante explicar una fórmula, justificar una transformación, interpretar un gráfico y realizar una modificación pequeña del código. La demostración permite verificar comprensión y autoría, no solo que el programa ejecuta.

## Errores que invalidan conclusiones

- Seleccionar activos solo por los que «ganaron» después de observar el periodo.
- Usar datos futuros en una decisión histórica.
- Comparar rendimientos de frecuencias diferentes.
- Omitir monedas y dividendos.
- Presentar correlación como causalidad.
- Prometer rentabilidad futura basándose en una simulación.

**Laboratorio:** [Guía de Streamlit](../../aprendizaje/06_streamlit/06_guia_streamlit.ipynb) · [Código inicial](../../aprendizaje/06_streamlit/app_ejemplo.py) · [Código final](../../aprendizaje/06_streamlit/app_final_ejemplo.py).

**Documentación:** [Streamlit](https://docs.streamlit.io/); [pandas](https://pandas.pydata.org/docs/).
