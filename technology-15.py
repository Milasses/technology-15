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
regions = ['Казахстан', 'Кыргызстан', 'Таджикистан', 'Узбекистан']
kaz_values = [0.0737473506983265, 0.044529239425859325, 0.07208697980276833, 0.09025550050680399]
uzb_values = [0.09872602667454446, 0.12482079148104783, 0.1033934827101725, 0.16342414956949367]
tjk_values = [0.13234311608076732, 0.11086727498562164, 0.19598527440470287, 0.23921461895440915]
kgz_values = [0.1875365079274166, 0.21059007745097164, 0.19581301002148638, 0.19449654750600165]
years = [2014, 2015, 2016, 2017]

# Ввод текста
st.markdown("<h1 style='text-align: center; color: green; font-family: Times New Roman; font-size: 20px; '> Для того чтобы увидеть график с определенной страной нажмите на соответствующую кнопку</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 20px; '>←--------------------------------</h1>", unsafe_allow_html=True)

# Отображение графика в зависимости от выбранного региона
if selected_region == 'Казахстан':
    st.header('График для выбранного региона: Казахстан')
    st.line_chart(dict(zip(years, kaz_values)))
elif selected_region == 'Кыргызстан':
    st.header('График для выбранного региона: Кыргызстан')
    st.line_chart(dict(zip(years, kgz_values)))
elif selected_region == 'Таджикистан':
    st.header('График для выбранного региона: Таджикистан')
    st.line_chart(dict(zip(years, tjk_values)))
elif selected_region == 'Узбекистан':
    st.header('График для выбранного региона: Узбекистан')
    st.line_chart(dict(zip(years, uzb_values)))

# Отображение графика для всех стран
all_countries_chart = st.line_chart({
    'Казахстан': kaz_values,
    'Кыргызстан': kgz_values,
    'Таджикистан': tjk_values,
    'Узбекистан': uzb_values
})

