import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(
    page_title="Nigeria Economic Pulse",
    page_icon="NG",
    layout="wide"

)

st.title("NG Nigeria Economic Pulse Dashboard")
st.markdown("*Live economic indicators - Exchange Rate, Inflation & GDP*")
st.markdown("-----")

conn = sqlite3.connect("nigeria_economy.db")

exchange_rate = pd.read_sql("SELECT * FROM exchange_rate", conn)
inflation = pd.read_sql("SELECT * FROM inflation", conn)
gdp = pd.read_sql("SELECT * FROM gdp", conn)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="USD/NGN Exchange Rate",
        value= f"₦{exchange_rate['rate'].iloc[0]:,.2f}"
    )

with col2:
    latest_inflation = inflation.sort_values("year").iloc[-1]
    st.metric(
        label= "Latest Inflation Rate",
        value =f"{latest_inflation['inflation_rate']}%",
        delta=f"Year: {latest_inflation['year']}"

    )

with col3:
    latest_gdp = gdp.sort_values("year").iloc[-1]
    st.metric(
        label="Latest GDP (USD)",
        value = f"${latest_gdp['gdp_usd']:,.0f}",
        delta=f"{latest_gdp['year']}"
    )

st.markdown("---")

st.subheader("Nigeria Inflation Rate Over Time")
fig1 = px.line(
    inflation,
    x = "year",
    y ="inflation_rate",
    title = "Nigeria Inflation Rate (%)",
    markers= True,
    color_discrete_sequence = ["#2E75B6"]

)

fig1.update_layout(
    xaxis_title ="Year",
    yaxis_title = "Inflation Rate(%)",
    hovermode = "x unified"
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("Nigeria GDP Over Time")
fig2 = px.bar(
    gdp,
    x = "year",
    y = "gdp_usd",
    title = "Nigeria GDP (USD)",
    color_discrete_sequence=["#1B3A68"]
)

fig2.update_layout(
    xaxis_title = "Year",
    yaxis_title = "GDP (USD)",
    hovermode = "x unified"
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.subheader("Raw Data Tables")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Inflation Data**")
    st.dataframe(inflation, use_container_width=True)

with col2:
    st.markdown("**GDP Data**")
    st.dataframe(gdp, use_container_width=True)

st.markdown("---")
st.caption("Data sourced from ExchangeRate API & World Bank API | Built by Ediomo Etesin")