# 2 · Análisis exploratorio de activos financieros

[← Índice](README.md) · [← Datos](01_datos_financieros.md) · [Series temporales →](03_series_temporales.md)

## Objetivo

Describir y comparar **rentabilidad, variabilidad, distribución y asociación** de activos antes de formular conclusiones.

## 1. Rendimiento simple

Para precios comparables `P_t` y `P_(t-1)`:

`r_t = (P_t / P_(t-1)) - 1`

Si el precio pasa de 100 a 105, el rendimiento es 0.05 = **5 %**. Si pasa de 105 a 100, el rendimiento es aproximadamente **-4.76 %**; subir y bajar cinco unidades no genera porcentajes simétricos.

```python
import pandas as pd
precios = pd.Series([100, 105, 102], name="Precio")
r = precios.pct_change()
print(r)
```

## 2. Rendimiento acumulado

`R = producto(1 + r_t) - 1 = P_final / P_inicial - 1`, si los precios y ajustes son consistentes y no hay flujos externos.

No se suman rendimientos simples de varios periodos para obtener el rendimiento compuesto exacto.

```python
acumulado = (1 + r.dropna()).prod() - 1
print(f"Acumulado: {acumulado:.2%}")
```

## 3. Medidas descriptivas

| Indicador | Qué informa | Precaución |
|---|---|---|
| Media | Promedio histórico por periodo | No garantiza rentabilidad futura |
| Mediana | Rendimiento central | No mide extremos |
| Desviación estándar | Dispersión respecto a la media | Trata alzas y caídas como variaciones |
| Mínimo y máximo | Extremos observados | Dependen de la ventana |
| Cuantiles | Posición en la distribución | No describen eventos fuera de muestra |
| Correlación | Asociación lineal entre rendimientos | No demuestra causalidad |

```python
print("Media:", r.mean())
print("Mediana:", r.median())
print("Volatilidad muestral:", r.std(ddof=1))
print("Cuantiles:\n", r.quantile([0.05, 0.5, 0.95]))
```

### Anualización orientativa

Para datos diarios bursátiles se usa a menudo una convención de **252 sesiones por año**:

- Media anualizada aritmética aproximada: `media_diaria * 252`.
- Volatilidad anualizada aproximada: `desv_diaria * sqrt(252)`.

Estas expresiones son **aproximaciones** sujetas a supuestos de frecuencia, dependencia y estabilidad; no equivalen a un rendimiento anual realizado ni garantizan que la volatilidad escale exactamente con la raíz del tiempo.

## 4. Visualizaciones y preguntas

- **Serie de precios**: ¿cómo cambió el nivel del activo?
- **Precios normalizados a base 100**: ¿cómo se comparan las trayectorias desde un mismo punto de partida?
- **Histograma de rendimientos**: ¿qué valores fueron frecuentes y cuáles extremos?
- **Diagrama de dispersión**: ¿qué asociación presentan dos activos?
- **Boxplot**: ¿cómo se comparan medianas, dispersión y valores atípicos?

```python
import matplotlib.pyplot as plt
r.dropna().hist(bins=15)
plt.title("Distribución de rendimientos por periodo")
plt.xlabel("Rendimiento (fracción)")
plt.ylabel("Frecuencia")
plt.show()
```

## Guía para interpretar un gráfico

Escribir siempre: **qué se representa, periodo y frecuencia, patrón principal, dato cuantitativo que lo respalda, posible explicación (si existe evidencia) y limitación**.

Evitar: «el activo es el mejor» solo porque tiene la media más alta; podría presentar mayor dispersión o pérdidas extremas.

## Actividad

Selecciona dos activos con la misma moneda y periodo. Calcula media, mediana, desviación estándar y rendimiento acumulado. Crea tres gráficos y redacta una comparación en máximo 200 palabras.

**Laboratorio:** [Análisis exploratorio](../../aprendizaje/03_analisis_exploratorio/03_analisis_exploratorio_portafolio.ipynb).

**Referencias:** [CFA Institute, Portfolio Risk and Return I](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/portfolio-risk-return-part-1); [pandas](https://pandas.pydata.org/docs/user_guide/index.html).
