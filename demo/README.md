# FinanceLab · Observatorio de Portafolios

Demostración docente de la **S23 — Streamlit / Taller 6**, Ingeniería Financiera ITM.

## Qué permite hacer
- Elegir hasta seis activos y horizonte de 3 meses a 5 años.
- Modificar pesos, capital inicial y tasa libre de riesgo.
- Comparar precios normalizados y valor histórico de la inversión.
- Analizar rentabilidad, volatilidad, Sharpe, drawdown y correlaciones.
- Consultar y exportar precios y rendimientos.

## Ejecutar

```bash
pip install -r demo/requirements.txt
streamlit run demo/app.py
```

Si se ejecuta desde esta carpeta: `streamlit run app.py`.

## Publicar
En Streamlit Community Cloud selecciona el repositorio `vyolete/proyecto_analitica_financiera`, rama `main`, archivo principal `demo/app.py`.

## Notas metodológicas
Se usan precios históricos descargados de Yahoo Finance con `auto_adjust=True`. Los rendimientos diarios se calculan con `pct_change()`; la cartera se modela con pesos constantes y rebalanceo diario. La volatilidad se anualiza con √252; Sharpe usa media diaria × 252 y tasa libre de riesgo anual configurable. No se incluyen costos, impuestos ni deslizamientos. La fuente puede imponer límites o presentar interrupciones. Material educativo, no asesoría financiera.
