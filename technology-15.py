import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#Добавление изображений
image = Image.open("центральная азия.jpg")
image1 = Image.open("казахстан.jpg")
image2 = Image.open("узбекистан.jpg")
image3 = Image.open("таджикистан.jpg")
image4 = Image.open("кыргызстан.jpg")
image5 = Image.open("общий график.jpg")

#Ввод текста
st.markdown("<h1 style='text-align: center; color: green; font-family: Times New Roman;'>Данная страница представляет информацию продовольственной безопасности центральной Азии</h1>", unsafe_allow_html=True)

#Добавление фона сайта
st.image(image)

# Данные для каждого региона
kaz_values = [0.0737473506983265, 0.044529239425859325, 0.07208697980276833, 0.09025550050680399]
uzb_values = [0.09872602667454446, 0.12482079148104783, 0.1033934827101725, 0.16342414956949367]
tjk_values = [0.13234311608076732, 0.11086727498562164, 0.19598527440470287, 0.23921461895440915]
kgz_values = [0.1875365079274166, 0.21059007745097164, 0.19581301002148638, 0.19449654750600165]
years = [2014, 2015, 2016, 2017]

#Функция для создания графиков 
def plot_country_graph(country, values, years):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, values, marker='o', linestyle='--')
    ax.set_title(country)
    ax.set_xticks(years)
    ax.set_yticks(np.arange(0, 0.31, 0.05))
    ax.grid(True)
    st.pyplot(fig)

# Ввод текста
st.markdown("<h1 style='text-align: center; color: green; font-family: Times New Roman; font-size: 20px; '> Для того чтобы увидеть график определенной страны нажмите на соответствующую кнопку</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 20px; '>←--------------------------------</h1>", unsafe_allow_html=True)

# Кнопки
st.sidebar.header("Выберите страну")
kaz_button = st.sidebar.button('Казахстан')
uzb_button = st.sidebar.button('Узбекистан')
tjk_button = st.sidebar.button('Таджикистан')
kgz_button = st.sidebar.button('Кыргызстан')
all_countries_button = st.sidebar.button('Общий график')
# Это нужно для того чтобы графики отображались на главной станице 
chart_placeholder = st.empty()

# Действия которые выполняю кнопки. Показывают график и изображение
if kaz_button:
    st.image(image1)
    plot_country_graph('Казахстан', kaz_values, years) 
elif uzb_button:
    st.image(image2)
    plot_country_graph('Узбекистан', uzb_values, years)
elif tjk_button:
    st.image(image3)
    plot_country_graph('Таджикистан', tjk_values, years)
elif kgz_button:
    st.image(image4)
    plot_country_graph('Кыргызстан', kgz_values, years)
elif all_countries_button:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, kaz_values, marker='o', linestyle='--', label='Казахстан')
    ax.plot(years, uzb_values, marker='o', linestyle='--', label='Узбекистан')
    ax.plot(years, kgz_values, marker='o', linestyle='--', label='Кыргызстан')
    ax.plot(years, tjk_values, marker='o', linestyle='--', label='Таджикистан')
    ax.set_title('Центральная Азия')
    ax.set_xticks(years)
    ax.set_yticks(np.arange(0, 0.3, 0.05))
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    st.image(image5)
