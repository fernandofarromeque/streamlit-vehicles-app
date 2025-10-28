import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis interactivo de anuncios de autos 🚗')

hist_button = st.button('Mostrar histograma del odómetro')
if hist_button:
    st.write('Creando histograma del kilometraje...')
    fig = px.histogram(car_data, x="odometer", nbins=30)
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Mostrar gráfico de dispersión: precio vs kilometraje')
if scatter_button:
    st.write('Creando gráfico de dispersión...')
    fig = px.scatter(car_data, x="odometer", y="price", color="type")
    st.plotly_chart(fig, use_container_width=True)