import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="FinanceLab | ITM", page_icon="📈", layout="wide", initial_sidebar_state="expanded")
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
html,body,[class*="css"],[data-testid="stApp"]{font-family:'DM Sans',sans-serif}
h1,h2,h3{font-family:'Space Grotesk',sans-serif!important;letter-spacing:-.035em}
[data-testid="stApp"]{background:radial-gradient(ellipse at 80% 0%,#14243a 0%,#09111e 45%,#070d17 100%);color:#e9f0fa}
[data-testid="stSidebar"]{background:#0c1728;border-right:1px solid #24334b}
[data-testid="stMetric"]{background:linear-gradient(145deg,#14253a,#0d1a2b);padding:18px 20px;border:1px solid #263951;border-radius:16px}
[data-testid="stMetricLabel"]{color:#a9bad1}
[data-testid="stMetricValue"]{color:#eaf5ff}
div[data-testid="stTabs"] button{font-weight:600}
.hero{padding:28px 32px;background:linear-gradient(115deg,#172d48,#101c30);border:1px solid #284563;border-radius:22px;margin-bottom:22px}
.eyebrow{color:#67e8f9;font-size:12px;font-weight:700;letter-spacing:.18em}
.hero h1{font-size:2.6rem;margin:10px 0;color:#f3f8ff}
.hero p{color:#a9bdd5;margin:0}
.insight{padding:14px 18px;border-left:3px solid #5eead4;background:#102337;border-radius:9px;color:#c5d7e9;margin-top:12px}
</style>""",unsafe_allow_html=True)

UNIVERSE={"Apple":"AAPL","Microsoft":"MSFT","NVIDIA":"NVDA","Alphabet":"GOOGL","Amazon":"AMZN","JPMorgan":"JPM","Visa":"V","Berkshire Hathaway":"BRK-B","S&P 500 ETF":"SPY","Nasdaq 100 ETF":"QQQ","Gold ETF":"GLD"}
st.sidebar.markdown("### ◈ FINANCELAB")
st.sidebar.caption("ITM · S23 · Demostración docente")
st.sidebar.divider()
names=st.sidebar.multiselect("Activos del portafolio",list(UNIVERSE),default=["Apple","Microsoft","JPMorgan"],max_selections=6)
period=st.sidebar.selectbox("Horizonte histórico",["3mo","6mo","1y","2y","5y"],index=2,format_func=lambda p:{"3mo":"3 meses","6mo":"6 meses","1y":"1 año","2y":"2 años","5y":"5 años"}[p])
capital=st.sidebar.number_input("Inversión inicial (USD)",min_value=100.0,value=10000.0,step=1000.0)
rf=st.sidebar.slider("Tasa libre de riesgo anual (%)",0.0,15.0,4.0,0.5)/100
st.sidebar.caption("Fuente: Yahoo Finance · Precios históricos ajustados cuando están disponibles")
if not names:
    st.info("Selecciona al menos un activo en el panel lateral."); st.stop()
tickers=[UNIVERSE[n] for n in names]
st.sidebar.markdown("#### Pesos del portafolio")
st.sidebar.caption("Modifica la asignación relativa. Se normaliza automáticamente a 100 %.")
raw={t:st.sidebar.number_input(t,min_value=0.0,max_value=100.0,value=round(100/len(tickers),1),step=5.0,key="w_"+t) for t in tickers}
total=sum(raw.values())
if total<=0:
    st.warning("Asigna un peso positivo al menos a un activo."); st.stop()
weights=pd.Series({t:v/total for t,v in raw.items()})
st.sidebar.caption("Distribución efectiva: "+", ".join(f"{t} {v:.1%}" for t,v in weights.items()))

@st.cache_data(ttl=1800,show_spinner=False)
def load_prices(symbols,period):
    frame=yf.download(list(symbols),period=period,auto_adjust=True,progress=False,threads=False)
    if frame.empty: return pd.DataFrame()
    if isinstance(frame.columns,pd.MultiIndex):
        close=frame["Close"]
    else:
        close=frame[["Close"]].rename(columns={"Close":symbols[0]})
    if isinstance(close,pd.Series):close=close.to_frame(name=symbols[0])
    return close.sort_index().apply(pd.to_numeric,errors="coerce")

st.markdown('<div class="hero"><span class="eyebrow">FINANCELAB / LABORATORIO DE ANALÍTICA FINANCIERA</span><h1>Observatorio de Portafolios</h1><p>Explora activos, compara riesgos y analiza decisiones de inversión con Python · Streamlit · Yahoo Finance</p></div>',unsafe_allow_html=True)
with st.spinner("Consultando precios históricos..."):
    try: prices=load_prices(tuple(tickers),period)
    except Exception as e:
        st.error("No se pudieron consultar los datos de mercado. Reintenta en unos minutos.")
        st.caption(str(e));st.stop()
missing=[t for t in tickers if t not in prices.columns or prices[t].dropna().empty]
if missing:
    st.warning("No hay datos suficientes para: "+", ".join(missing))
    prices=prices.drop(columns=missing,errors="ignore")
if prices.empty:st.error("Sin datos disponibles para los activos elegidos.");st.stop()
prices=prices.ffill().dropna()
if len(prices)<35:
    st.warning("Se requieren al menos 35 observaciones conjuntas para calcular los indicadores.");st.stop()
weights=weights.reindex(prices.columns).fillna(0)
if weights.sum()==0:st.error("Los activos con datos no tienen pesos positivos.");st.stop()
weights=weights/weights.sum()
rets=prices.pct_change().dropna()
port=rets.dot(weights)
wealth=(1+port).cumprod()
growth=wealth.iloc[-1]-1
vol=port.std(ddof=1)*np.sqrt(252)
sharpe=(port.mean()*252-rf)/vol if vol>0 else np.nan
drawdown=wealth/wealth.cummax()-1
maxdd=drawdown.min()
cols=st.columns(4)
for c,(label,val,helptext) in zip(cols,[("Rentabilidad acumulada",f"{growth:+.2%}","Portafolio con pesos constantes y rebalanceo diario"),("Volatilidad anualizada",f"{vol:.2%}","Desviación diaria × raíz de 252"),("Sharpe anualizado",f"{sharpe:.2f}" if np.isfinite(sharpe) else "N/D","Rentabilidad media anualizada menos tasa libre de riesgo, sobre volatilidad"),("Máximo drawdown",f"{maxdd:.2%}","Mayor caída desde un máximo histórico")]):
    c.metric(label,val,help=helptext)
st.caption(f"Ventana observada: {prices.index.min():%d/%m/%Y} — {prices.index.max():%d/%m/%Y} · {len(prices)} precios comunes · {len(rets)} rendimientos diarios")
tab1,tab2,tab3=st.tabs(["◈ Portafolio","◈ Riesgo cuantitativo","◈ Estadística"])
def chart(fig):
    fig.update_layout(template="plotly_dark",paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",font=dict(color="#cbd5e1"),margin=dict(l=10,r=10,t=40,b=10),hovermode="x unified")
    st.plotly_chart(fig,use_container_width=True)
with tab1:
    st.subheader("Evolución comparativa")
    normalized=prices.div(prices.iloc[0]).mul(100)
    fig=px.line(normalized,title="Índice base 100 · Comparación de activos",labels={"value":"Índice (inicio = 100)","index":"Fecha","variable":"Activo"})
    chart(fig)
    left,right=st.columns([1.7,1])
    with left:
        fig=go.Figure()
        fig.add_trace(go.Scatter(x=wealth.index,y=wealth*capital,fill="tozeroy",name="Portafolio",line=dict(color="#5eead4",width=3)))
        fig.update_layout(title="Valor histórico de la inversión (USD)",yaxis_title="USD")
        chart(fig)
    with right:
        fig=px.pie(values=weights.values,names=weights.index,hole=.64,title="Asignación del portafolio",color_discrete_sequence=px.colors.qualitative.Set2)
        chart(fig)
    st.markdown('<div class="insight">Lectura financiera: los precios normalizados permiten comparar activos con precios nominales distintos. La curva de inversión representa un portafolio teórico con rebalanceo diario a pesos constantes, sin costos ni impuestos.</div>',unsafe_allow_html=True)
with tab2:
    st.subheader("Riesgo y comportamiento temporal")
    left,right=st.columns(2)
    with left:
        fig=px.line(drawdown.mul(100),title="Drawdown del portafolio",labels={"value":"Caída desde máximo (%)","index":"Fecha"})
        chart(fig)
    with right:
        rolling=port.rolling(30).std()*np.sqrt(252)*100
        fig=px.line(rolling,title="Volatilidad móvil de 30 sesiones",labels={"value":"Volatilidad anualizada (%)","index":"Fecha"})
        chart(fig)
    summary=pd.DataFrame({"Rendimiento anualizado (%)":rets.mean()*252*100,"Volatilidad anualizada (%)":rets.std()*np.sqrt(252)*100})
    fig=px.scatter(summary,x="Volatilidad anualizada (%)",y="Rendimiento anualizado (%)",text=summary.index,size=[20]*len(summary),title="Mapa riesgo–rendimiento")
    fig.update_traces(textposition="top center");chart(fig)
    st.markdown('<div class="insight">El drawdown cuantifica pérdidas desde máximos previos; la volatilidad mide dispersión, no pérdidas garantizadas. El rendimiento histórico no predice el futuro.</div>',unsafe_allow_html=True)
with tab3:
    st.subheader("Estadística descriptiva")
    table=pd.DataFrame({"Media diaria (%)":rets.mean()*100,"Mediana diaria (%)":rets.median()*100,"Desv. estándar diaria (%)":rets.std()*100,"Mínimo diario (%)":rets.min()*100,"Máximo diario (%)":rets.max()*100,"Sesiones":rets.count()})
    st.dataframe(table.style.format({k:"{:.3f}" for k in table.columns if k!="Sesiones"}),use_container_width=True)
    a,b=st.columns(2)
    with a:
        fig=px.histogram(x=port*100,nbins=40,title="Distribución de rendimientos diarios del portafolio",labels={"x":"Rendimiento diario (%)","y":"Frecuencia"})
        chart(fig)
    with b:
        corr=rets.corr()
        fig=px.imshow(corr,text_auto=".2f",zmin=-1,zmax=1,color_continuous_scale="RdBu_r",title="Correlación entre activos")
        chart(fig)
    st.markdown('<div class="insight">Una correlación cercana a +1 indica movimientos lineales similares; cercana a −1, movimientos opuestos. No implica causalidad y puede cambiar con el tiempo.</div>',unsafe_allow_html=True)
st.divider()
st.subheader("Datos y reproducibilidad")
with st.expander("Consultar precios y descargar resultados"):
    st.dataframe(prices.tail(30),use_container_width=True)
    st.download_button("Descargar precios (CSV)",prices.to_csv().encode("utf-8"),"financelab_precios.csv","text/csv")
    st.download_button("Descargar rendimientos (CSV)",rets.to_csv().encode("utf-8"),"financelab_rendimientos.csv","text/csv")
st.caption("Demo educativa · Indicadores calculados sobre precios diarios históricos · Sin recomendaciones de inversión · Las series pueden variar según disponibilidad de Yahoo Finance.")
