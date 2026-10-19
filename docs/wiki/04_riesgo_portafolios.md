# 4 · Riesgo, diversificación y portafolios

[← Índice](README.md) · [← Series temporales](03_series_temporales.md) · [Proyecto →](05_proyecto_aplicacion.md)

## Pregunta

**¿Cómo cambia el riesgo al combinar activos con diferentes rendimientos y correlaciones?**

## Riesgo y rendimiento

La volatilidad histórica (desviación estándar de rendimientos) mide dispersión, pero no resume todos los riesgos. También importan pérdidas extremas, liquidez, riesgo de mercado, crédito, divisa y concentración.

### Covarianza y correlación

- **Covarianza**: cómo varían conjuntamente dos series de rendimientos, en sus unidades cuadráticas.
- **Correlación**: covarianza normalizada, entre -1 y 1, que describe asociación lineal.
- **Correlación baja** puede favorecer la diversificación; no elimina el riesgo ni es necesariamente estable en crisis.

## Rendimiento de portafolio

Para pesos `w_i` que suman 1 y rendimientos del mismo periodo `r_i`:

`r_p = sum(w_i * r_i)`

Ejemplo: 60 % en A con rendimiento de 4 % y 40 % en B con -2 %:

`r_p = 0.6*0.04 + 0.4*(-0.02) = 0.016 = 1.6 %`

Esta fórmula corresponde a un periodo y a los pesos efectivos de ese periodo; en series multiperiodo debe especificarse si se rebalancea la cartera.

## Riesgo de dos activos

`sigma_p^2 = w_A^2 sigma_A^2 + w_B^2 sigma_B^2 + 2 w_A w_B sigma_A sigma_B rho_AB`

El término de correlación explica por qué el riesgo total no suele ser el promedio ponderado de las volatilidades individuales.

## Cálculo con pandas y numpy

```python
import numpy as np
import pandas as pd

# Ejemplo ilustrativo: rendimientos por periodo
retornos = pd.DataFrame({
    "A": [0.02, -0.01, 0.03, 0.01, -0.02],
    "B": [-0.01, 0.02, 0.01, -0.02, 0.02]
})
pesos = np.array([0.6, 0.4])
cov = retornos.cov().to_numpy()
rend_port = retornos.to_numpy() @ pesos
vol_port = np.sqrt(pesos @ cov @ pesos)
print("Rendimiento medio:", rend_port.mean())
print("Volatilidad por periodo:", vol_port)
print("Correlación:\n", retornos.corr())
```

Las medidas del ejemplo son **muestrales** y se refieren a la misma frecuencia que los datos. No representan un pronóstico.

## Indicadores adicionales

| Indicador | Fórmula o idea | Interpretación y límite |
|---|---|---|
| Máximo drawdown | Menor valor de `valor / máximo_acumulado - 1` | Peor caída observada desde un máximo |
| Sharpe | `(rendimiento - tasa libre de riesgo) / volatilidad` | Exceso de rendimiento por unidad de volatilidad; exige frecuencias consistentes |
| VaR histórico | Cuantil inferior de la distribución de pérdidas/retornos, con nivel y horizonte definidos | Umbral estimado, **no** pérdida máxima posible |
| CVaR/ES | Pérdida media en la cola más adversa, según convención | Sensible a tamaño de muestra y supuestos |
| Beta | Sensibilidad lineal al retorno de referencia | Depende del benchmark y del periodo |

## Simulación Monte Carlo

Una simulación genera escenarios bajo un modelo y supuestos explícitos. No debe presentarse como predicción cierta. Documentar distribución elegida, estimación de parámetros, horizonte, número de simulaciones y límites (colas, cambios de régimen, correlaciones variables).

## Frontera eficiente: concepto

La teoría media-varianza estudia combinaciones que maximizan rendimiento esperado para un nivel de riesgo o minimizan riesgo para un rendimiento esperado. La frontera **depende de estimaciones**, restricciones y supuestos; pequeñas variaciones en insumos pueden cambiar fuertemente los pesos óptimos.

## Actividad

Construye un portafolio de tres activos; compara volatilidades individuales, matriz de correlación y volatilidad del portafolio. Justifica pesos y comenta por qué el comportamiento histórico no garantiza la diversificación futura.

**Laboratorio:** [Riesgo y simulación](../../aprendizaje/05_riesgo_simulacion/05_riesgo_simulacion_portafolio.ipynb).

**Referencias:** [CFA Institute, Portfolio Risk and Return I](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/portfolio-risk-return-part-1); [CFA Institute, Portfolio Risk and Return II](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/portfolio-risk-return-part-2); [SEC, Diversifying Risk](https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/diversifying-risk).
