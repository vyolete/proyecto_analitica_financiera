# 0 · Fundamentos de analítica financiera

[← Índice](README.md) · [Siguiente: datos financieros →](01_datos_financieros.md)

## Propósito

Aprender a transformar una pregunta financiera en un procedimiento verificable. La analítica financiera integra **conceptos financieros, estadística, programación y juicio crítico**.

### Ejemplo conductor

Un analista debe estudiar tres activos y responder: **¿cómo se comportaron su rentabilidad y riesgo durante el último año disponible?** Antes de calcular, debe fijar universo, fechas, moneda, fuente, frecuencia y reglas para datos faltantes.

## Proceso analítico

1. **Problema**: delimitar decisión y pregunta.
2. **Datos**: identificar proveedor, cobertura, periodicidad, ajustes y calidad.
3. **Preparación**: revisar índice temporal, duplicados, nulos y tipos.
4. **Cálculo**: estimar indicadores mediante fórmulas documentadas.
5. **Visualización**: elegir un gráfico coherente con la pregunta.
6. **Interpretación**: responder con evidencia y reconocer limitaciones.
7. **Comunicación**: informe o aplicación reproducible.

### Diferencia entre dato, indicador e interpretación

- **Dato**: cierre de una acción en una fecha.
- **Indicador**: rendimiento diario calculado con dos precios.
- **Interpretación**: «el activo cayó 2 % entre estas dos sesiones»; no implica que caerá mañana.

## Python como herramienta

| Recurso | Para qué sirve |
|---|---|
| Variables y operadores | Expresar tasas, capital, costos y fórmulas |
| Condicionales | Aplicar reglas y validar entradas |
| Listas y diccionarios | Organizar activos y parámetros |
| pandas | Trabajar con tablas e índices de fechas |
| numpy | Operaciones numéricas y simulación |
| matplotlib | Visualización de resultados |
| yfinance | Consultar datos de mercado con restricciones de cobertura |
| Streamlit | Convertir un análisis en una interfaz exploratoria |

## Ejemplo reproducible sin conexión

```python
capital = 1_000_000
tasa = 0.08
valor_final = capital * (1 + tasa)
ganancia = valor_final - capital
print(f"Valor final: {valor_final:,.0f}")
print(f"Ganancia: {ganancia:,.0f}")
```

**Interpretación**: una tasa del 8 % para un único periodo incrementa el capital inicial en 80 000 unidades monetarias. El ejemplo no incorpora inflación, impuestos ni costos.

## Conceptos financieros imprescindibles

- **Acción**: participación patrimonial en una compañía.
- **Bono**: instrumento de deuda con condiciones de pago.
- **ETF**: fondo cotizado que mantiene una cartera según su mandato.
- **Precio**: valor observado por unidad del activo.
- **Rendimiento**: variación relativa del valor durante un periodo, con la definición de precio adecuada.
- **Riesgo**: posibilidad de que el resultado difiera del esperado; no se reduce a una sola medida.
- **Portafolio**: combinación de activos y sus pesos.

## Comprobación

1. ¿Por qué un precio de 300 no significa mayor rentabilidad que un precio de 50?
2. ¿Qué información falta si un informe solo dice «volatilidad de 2 %»?
3. ¿Qué decisión metodológica cambia si se mezclan precios en USD y COP?

**Laboratorio:** [Fundamentos de Python](../../aprendizaje/01_fundamentos/01_fundamentos_analizador_inversiones.ipynb).

**Referencia conceptual:** [CFA Institute, Investment Foundations](https://www.cfainstitute.org/programs/investment-foundations-certificate).
