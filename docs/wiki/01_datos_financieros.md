# 1 · Obtención y calidad de datos financieros

[← Índice](README.md) · [← Fundamentos](00_fundamentos.md) · [Análisis exploratorio →](02_analisis_exploratorio.md)

## Pregunta de análisis

**¿Qué datos necesitamos para comparar el comportamiento de varios activos sin producir conclusiones engañosas?**

## Estructura de una serie financiera

Un registro típico incluye fecha, apertura, máximo, mínimo, cierre y volumen (OHLCV). La fecha puede representar una sesión bursátil y no todos los días del calendario. El cierre no necesariamente incorpora dividendos o desdoblamientos; cuando el proveedor ofrece series ajustadas, es indispensable identificar qué ajustes aplica.

La frecuencia (diaria, semanal, mensual), zona horaria, calendario bursátil, moneda y tratamiento de dividendos deben documentarse.

## Descargar datos con yfinance

```python
%pip -q install yfinance pandas
import yfinance as yf
import pandas as pd

ticker = yf.Ticker("MSFT")
datos = ticker.history(period="1y", auto_adjust=True)
print(datos.head())
print(datos.info())
```

**Interpretación del código**: `Ticker` identifica el instrumento; `history` solicita un intervalo histórico; `auto_adjust=True` solicita precios ajustados según la lógica del proveedor. Antes de comparar activos, verificar que existan registros y que la cobertura sea suficiente.

> La disponibilidad, licencia y estructura de los datos pueden cambiar. Yahoo Finance no es una fuente de datos auditada para todas las aplicaciones y `yfinance` es una biblioteca de terceros.

## Lista de verificación de calidad

```python
if datos.empty:
    raise ValueError("No hay datos para el activo y periodo solicitado")

print("Duplicados de fecha:", datos.index.duplicated().sum())
print("Nulos por columna:\n", datos.isna().sum())
print("Rango:", datos.index.min(), datos.index.max())
print("Tipos:\n", datos.dtypes)
```

### Errores frecuentes

- Combinar monedas sin conversión.
- Comparar activos con periodos distintos.
- Rellenar nulos sin justificarlo (puede fabricar rendimientos).
- Ignorar dividendos o splits al interpretar retornos.
- Confundir días no bursátiles con datos perdidos.
- Suponer que todos los proveedores usan idénticos ajustes.

## Selección y preparación

```python
precios = datos["Close"].dropna().sort_index()
rendimientos = precios.pct_change().dropna()
```

`pct_change()` devuelve una **variación relativa**. Por ejemplo, 0.025 equivale a 2.5 %, no a 0.025 %. El primer resultado suele ser `NaN` porque no existe una observación anterior.

## Preguntas de reflexión

1. ¿Qué cambia al utilizar precios sin ajustar?
2. ¿Por qué el volumen no se interpreta igual que el precio?
3. ¿Cómo documentarías un periodo en el que un activo no cotizó?

**Laboratorio:** [Tratamiento de datos financieros](../../02_financial_data/02_tratamiento_datos_financieros.ipynb).

**Fuentes:** [yfinance](https://ranaroussi.github.io/yfinance/); [pandas, cambio relativo](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html).
