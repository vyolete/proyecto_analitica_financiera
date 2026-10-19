"""Financial Analytics Lab | Primera versión de la aplicación (S27)."""
from datetime import date, timedelta

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Financial Analytics Lab", page_icon="📈", layout="wide")
st.title("Financial Analytics Lab")
st.caption("Analizador de inversiones · Versión inicial")
st.write(
    "Consulta precios históricos de un activo, calcula indicadores y examina "
    "su evolución. Los resultados son descriptivos, no predicciones."
)

ACTIVOS = {"Microsoft": "MSFT", "Apple": "AAPL", "JPMorgan": "JPM", "NVIDIA": "NVDA"}
nombre = st.sidebar.selectbox("Selecciona un activo", list(ACTIVOS))
ticker = ACTIVOS[nombre]
fin = st.sidebar.date_input("Fecha final (incluida)", date.today())
inicio = st.sidebar.date_input("Fecha inicial", fin - timedelta(days=365))

if inicio >= fin:
    st.error("La fecha inicial debe ser anterior a la fecha final.")
    st.stop()


@st.cache_data(ttl=3600, show_spinner=False)
def consultar_precios(simbolo: str, fecha_inicial: str, fecha_final_exclusiva: str) -> pd.DataFrame:
    """Descarga cierres ajustados; el límite final de yfinance es exclusivo."""
    tabla = yf.download(
        simbolo, start=fecha_inicial, end=fecha_final_exclusiva,
        auto_adjust=True, progress=False, multi_level_index=False
    )
    if tabla.empty or "Close" not in tabla.columns:
        return pd.DataFrame()
    precios = tabla[["Close"]].copy()
    precios = precios.sort_index()
    precios = precios.loc[~precios.index.duplicated(keep="first")]
    precios["Close"] = pd.to_numeric(precios["Close"], errors="coerce")
    return precios.dropna().loc[lambda x: x["Close"] > 0]


try:
    precios = consultar_precios(ticker, str(inicio), str(fin + timedelta(days=1)))
except Exception as exc:
    st.error("No se pudo consultar la fuente. Comprueba internet y vuelve a intentar.")
    st.caption(f"Detalle técnico: {type(exc).__name__}")
    st.stop()

if len(precios) < 2:
    st.warning("No hay suficientes observaciones válidas en el período.")
    st.stop()

rendimientos = precios["Close"].pct_change(fill_method=None).dropna()
rendimiento_acumulado = precios["Close"].iloc[-1] / precios["Close"].iloc[0] - 1
volatilidad = rendimientos.std(ddof=1) if len(rendimientos) > 1 else float("nan")

a, b, c = st.columns(3)
a.metric("Precio final (USD)", f"${precios['Close'].iloc[-1]:,.2f}")
b.metric("Variación acumulada del precio", f"{rendimiento_acumulado:.2%}")
c.metric(
    "Volatilidad por observación",
    f"{volatilidad:.2%}" if pd.notna(volatilidad) else "Muestra insuficiente",
)

st.subheader(f"Evolución histórica · {ticker}")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(precios.index, precios["Close"])
ax.set(xlabel="Fecha", ylabel="USD por acción")
ax.grid(alpha=0.25)
st.pyplot(fig)
plt.close(fig)

st.subheader("Interpretación")
if rendimiento_acumulado > 0:
    st.write("El precio de cierre final es superior al inicial en el período consultado.")
elif rendimiento_acumulado < 0:
    st.write("El precio de cierre final es inferior al inicial en el período consultado.")
else:
    st.write("El precio de cierre final coincide con el inicial en el período consultado.")
st.write(
    "La volatilidad es la desviación estándar muestral de los rendimientos "
    "entre observaciones; una cifra mayor describe más dispersión histórica. "
    "No representa por sí sola la probabilidad de pérdida futura."
)
st.caption(
    "Fuente: Yahoo Finance vía yfinance. Precios de cierre ajustados según "
    "auto_adjust=True. No incluye comisiones, impuestos ni flujos adicionales. "
    "La consulta depende de un servicio externo y no constituye asesoría financiera."
)
with st.expander("Ver datos y descargar"):
    st.dataframe(precios, use_container_width=True)
    st.download_button(
        "Descargar cierres CSV",
        data=precios.to_csv(index_label="Fecha"),
        file_name=f"{ticker}_cierres.csv",
        mime="text/csv",
    )
