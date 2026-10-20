
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

# Título do aplicativo
st.header("Dashboard de anúncios de veículos")

st.write(
    "Explore os dados dos anúncios de venda de veículos "
    "usando os gráficos interativos abaixo."
)

# Botão para criar um histograma
hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Distribuição da quilometragem dos veículos")

    fig = px.histogram(
        car_data,
        x="odometer",
        title="Distribuição da quilometragem dos veículos",
        labels={"odometer": "Quilometragem"}
    )

    st.plotly_chart(fig, use_container_width=True)

# Botão para criar um gráfico de dispersão
scatter_button = st.button("Criar gráfico de dispersão")

if scatter_button:
    st.write("Relação entre preço e ano do veículo")

    fig = px.scatter(
        car_data,
        x="model_year",
        y="price",
        title="Preço dos veículos por ano do modelo",
        labels={
            "model_year": "Ano do modelo",
            "price": "Preço (US$)"
        }
    )

    st.plotly_chart(fig, use_container_width=True)
