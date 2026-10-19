# 3 · Series temporales financieras

[← Índice](README.md) · [← Exploratorio](02_analisis_exploratorio.md) · [Riesgo →](04_riesgo_portafolios.md)

## Pregunta

**¿Cómo evoluciona el rendimiento y el riesgo de un activo a lo largo del tiempo?**

Una serie temporal ordena observaciones por fecha. En finanzas importan la frecuencia, la dependencia temporal, los cambios de régimen y las ventanas de análisis.

## Componentes de una serie

- **Tendencia**: dirección de largo plazo, cuando puede identificarse.
- **Estacionalidad**: patrón que se repite con cierta periodicidad.
- **Ciclo**: fluctuación sin periodicidad necesariamente fija.
- **Ruido**: variaciones no explicadas por los componentes anteriores.

No debe suponerse estacionalidad en una serie financiera sin evidencia. Las series de precios pueden ser no estacionarias y las propiedades de sus rendimientos pueden variar con el tiempo.

## Índice de fechas y remuestreo

```python
import pandas as pd
s = pd.Series([100, 101, 99, 104, 103, 107],
              index=pd.bdate_range("2026-01-05", periods=6))
mensual = s.resample("ME").last()
print(mensual)
```

**Atención:** `resample("ME").last()` produce el último valor disponible de cada mes, no una media de rendimientos. Para obtener retornos mensuales, primero se eligen cierres mensuales y luego se calcula `pct_change()`.

## Rezagos y medias móviles

```python
rezago = s.shift(1)
media_movil_3 = s.rolling(window=3).mean()
print(pd.DataFrame({"precio": s, "rezago": rezago,
                    "media_movil_3": media_movil_3}))
```

Una media móvil suaviza fluctuaciones, pero **introduce rezago** y puede ocultar cambios bruscos. Una ventana de 3 observaciones no equivale necesariamente a 3 días calendario.

## Volatilidad móvil

```python
r = s.pct_change()
vol_movil_3 = r.rolling(3).std(ddof=1)
print(vol_movil_3)
```

Se calcula sobre **rendimientos**, no sobre niveles de precios. La volatilidad móvil permite observar cambios en dispersión a través del tiempo, pero es sensible al tamaño de la ventana.

## Rendimiento acumulado y drawdown

```python
indice = (1 + r.fillna(0)).cumprod()
maximo_historico = indice.cummax()
drawdown = indice / maximo_historico - 1
print("Máxima caída desde pico:", drawdown.min())
```

El **drawdown** mide la caída respecto del máximo acumulado previo. No debe confundirse con volatilidad: un activo puede tener variaciones diarias moderadas y acumular una caída persistente.

## Estacionariedad y autocorrelación

Una serie (débilmente) estacionaria mantiene media y covarianzas que no dependen del momento absoluto, bajo la definición correspondiente. Para una introducción, comparar gráficos de precios y rendimientos y observar ACF; en niveles avanzados se pueden estudiar ADF y KPSS. Ninguna prueba aislada garantiza predictibilidad.

## Errores frecuentes

1. Usar datos futuros en una media móvil o entrenamiento de modelo (**look-ahead bias**).
2. Mezclar frecuencias diarias y mensuales.
3. Comparar ventanas con distinto número de observaciones.
4. Interpretar una correlación temporal como prueba causal.
5. Pronosticar precios únicamente porque una curva parece tener tendencia.

## Actividad

Para un activo, calcular rendimientos, media móvil de 20 y 50 sesiones, volatilidad móvil de 20 sesiones y drawdown. Redactar qué pregunta responde cada gráfico y qué no permite concluir.

**Laboratorio:** [Series temporales](../../04_time_series/04_series_temporales_financieras.ipynb).

**Referencias:** [pandas, series temporales](https://pandas.pydata.org/docs/user_guide/timeseries.html); [statsmodels, estacionariedad y ADF/KPSS](https://www.statsmodels.org/stable/examples/notebooks/generated/stationarity_detrending_adf_kpss.html).
