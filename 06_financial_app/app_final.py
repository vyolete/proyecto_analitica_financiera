"""Financial Analytics Lab | Versión ampliada para análisis comparativo (S33)."""
from datetime import date, timedelta

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Financial Analytics Lab | Portafolio", page_icon="📊", layout="wide")
st.title("Financial Analytics Lab")
st.caption("Análisis comparativo de activos y portafolios · Versión ampliada")
st.write("Explora rendimientos, volatilidad, correlaciones y caídas históricas. No es una herramienta predictiva.")

UNIVERSO = {"Microsoft": "MSFT", "Apple": "AAPL", "JPMorgan": "JPM",
            "NVIDIA": "NVDA", "ETF S&P 500": "SPY", "ETF Nasdaq 100": "QQQ"}
seleccion = st.sidebar.multiselect("Activos (2 a 4)", list(UNIVERSO), default=["Microsoft", "Apple", "JPMorgan"])
fin = st.sidebar.date_input("Fecha final (incluida)", date.today())
inicio = st.sidebar.date_input("Fecha inicial", fin - timedelta(days=730))
if not 2 <= len(seleccion) <= 4:
    st.info("Selecciona entre dos y cuatro activos.")
    st.stop()
if inicio >= fin:
    st.error("La fecha inicial debe ser anterior a la final.")
    st.stop()

tickers = [UNIVERSO[x] for x in seleccion]
st.sidebar.markdown("### Ponderaciones")
pesos_ingresados = [st.sidebar.number_input(f"Peso de {ticker} (%)", min_value=0.0,
                  max_value=100.0, value=round(100 / len(tickers), 2),
                  step=1.0, key=f"peso_{ticker}") for ticker in tickers]
suma = sum(pesos_ingresados)
if not np.isclose(suma, 100, atol=0.02):
    st.sidebar.error(f"Los pesos deben sumar 100 %. Suma actual: {suma:.2f} %")
    st.stop()
pesos = pd.Series(np.array(pesos_ingresados) / suma, index=tickers)

@st.cache_data(ttl=3600, show_spinner=False)
def descargar(simbolo: str, inicio_iso: str, fin_exclusivo_iso: str) -> pd.Series:
    tabla = yf.download(simbolo, start=inicio_iso, end=fin_exclusivo_iso,
                        auto_adjust=True, progress=False, multi_level_index=False)
    if tabla.empty or "Close" not in tabla.columns:
        raise ValueError(f"No se obtuvieron precios para {simbolo}")
    cierre = pd.to_numeric(tabla["Close"], errors="coerce").dropna()
    cierre = cierre.loc[cierre > 0].sort_index()
    cierre = cierre.loc[~cierre.index.duplicated(keep="first")]
    return cierre.rename(simbolo)

try:
    series = [descargar(t, str(inicio), str(fin + timedelta(days=1))) for t in tickers]
    precios = pd.concat(series, axis=1, join="inner").dropna()
except Exception as exc:
    st.error("No se pudieron obtener los datos. Verifica la conexión y los activos.")
    st.caption(f"Detalle técnico: {type(exc).__name__}")
    st.stop()
if len(precios) < 30:
    st.warning("Se necesitan al menos 30 precios alineados para este análisis.")
    st.stop()

retornos = precios.pct_change(fill_method=None).dropna(how="any")
retornos_port = retornos.dot(pesos)  # Supone reequilibrio a pesos constantes por observación
indice_port = pd.concat([pd.Series([1.0]), 1 + retornos_port], ignore_index=True).cumprod()
valor_port = indice_port.iloc[1:]
valor_port.index = retornos.index
acumulado_port = valor_port.iloc[-1] - 1
vol_port = retornos_port.std(ddof=1)
drawdown_port = valor_port.div(valor_port.cummax().clip(lower=1.0)).sub(1)
# Incluye el capital inicial 1 en el máximo de referencia.
maximo_acumulado = np.maximum.accumulate(np.r_[1.0, valor_port.to_numpy()])[1:]
drawdown_port = pd.Series(valor_port.to_numpy() / maximo_acumulado - 1, index=retornos.index)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Rendimiento acumulado del portafolio", f"{acumulado_port:.2%}")
m2.metric("Volatilidad por observación", f"{vol_port:.2%}")
m3.metric("Máximo drawdown", f"{drawdown_port.min():.2%}")
m4.metric("Observaciones comunes", str(len(precios)))

tab1, tab2, tab3 = st.tabs(["Evolución", "Riesgo y relaciones", "Datos y método"])
with tab1:
    st.subheader("Evolución comparada · base 100")
    normalizados = precios.div(precios.iloc[0]).mul(100)
    fig, ax = plt.subplots(figsize=(10, 4))
    for t in tickers:
        ax.plot(normalizados.index, normalizados[t], label=t)
    ax.set(xlabel="Fecha", ylabel="Índice (inicio = 100)")
    ax.legend()
    ax.grid(alpha=0.25)
    st.pyplot(fig)
    plt.close(fig)

    st.subheader("Valor relativo del portafolio · inicio = 100")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(valor_port.index, valor_port * 100, label="Portafolio")
    ax.axhline(100, linewidth=1)
    ax.set(xlabel="Fecha", ylabel="Valor índice")
    ax.grid(alpha=0.25)
    st.pyplot(fig)
    plt.close(fig)
    st.write("El resultado representa una estrategia hipotética reequilibrada a los pesos seleccionados en cada observación.")

with tab2:
    st.subheader("Correlaciones de rendimientos")
    corr = retornos.corr()
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(tickers)), tickers)
    ax.set_yticks(range(len(tickers)), tickers)
    for i in range(len(tickers)):
        for j in range(len(tickers)):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center")
    fig.colorbar(im, ax=ax)
    st.pyplot(fig)
    plt.close(fig)
    st.caption("Correlación no implica causalidad ni garantiza diversificación futura.")

    st.subheader("Caída del portafolio desde máximos")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(drawdown_port.index, drawdown_port * 100)
    ax.axhline(0, linewidth=1)
    ax.set(xlabel="Fecha", ylabel="Drawdown (%)")
    ax.grid(alpha=0.25)
    st.pyplot(fig)
    plt.close(fig)

    cov = retornos.cov()
    vol_matriz = np.sqrt(float(pesos.to_numpy() @ cov.to_numpy() @ pesos.to_numpy()))
    assert np.isclose(vol_port, vol_matriz)
    st.write(f"Volatilidad verificada con matriz de covarianzas: **{vol_matriz:.2%} por observación**.")

with tab3:
    st.write("**Fuente:** Yahoo Finance vía yfinance. Cierres ajustados según auto_adjust=True.")
    st.write("**Período:**", str(precios.index.min().date()), "a", str(precios.index.max().date()))
    st.write("**Pesos:**", {k: f"{v:.1%}" for k, v in pesos.items()})
    st.write("**Tratamiento:** precios positivos, sin faltantes, fechas comunes, rendimientos simples.")
    st.write("**Supuestos:** pesos reequilibrados en cada observación; sin comisiones, impuestos, dividendos adicionales ni aportes/retiros.")
    st.write("**Limitaciones:** la información histórica no predice resultados futuros; la correlación y la volatilidad pueden cambiar.")
    st.dataframe(precios, use_container_width=True)
    st.download_button("Descargar precios CSV", precios.to_csv(index_label="Fecha"),
                       "precios_portafolio.csv", mime="text/csv")
    st.download_button("Descargar rendimientos CSV", retornos.to_csv(index_label="Fecha"),
                       "rendimientos_portafolio.csv", mime="text/csv")

st.caption("Proyecto académico de análisis financiero. No constituye asesoría ni recomendación de inversión.")
