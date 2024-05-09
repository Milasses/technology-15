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

st.image(image)

Prob_Mod_Sev_kaz_values = [0.0737473506983265, 0.044529239425859325, 0.07208697980276833, 0.09025550050680399]
Prob_Mod_Sev_uzb_values = [0.09872602667454446, 0.12482079148104783, 0.1033934827101725, 0.16342414956949367]
Prob_Mod_Sev_tjk_values = [0.13234311608076732, 0.11086727498562164, 0.19598527440470287, 0.23921461895440915]
Prob_Mod_Sev_kgz_values = [0.1875365079274166, 0.21059007745097164, 0.19581301002148638, 0.19449654750600165]
years = [2014, 2015, 2016, 2017]

#Функция для создания графиков 
def plot_country_graph(country, values, years):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, values, marker='o', linestyle='-')
    ax.set_title(country)
    ax.set_xticks(years)
    ax.set_yticks(np.arange(0, 0.31, 0.05))
    ax.grid(True)
    st.pyplot(fig)

st.markdown("<h1 style='text-align: center;'>←--------------------------------</h1>", unsafe_allow_html=True)
# Ввод теста
st.markdown("<div style='text-align: right;'> <h1 style='color: green; font-family: Times New Roman;'>Данная страница представляет информацию продовольственной безопасности центральной Азии</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: right; color: green; font-family: Times New Roman;'> Для того чтобы увидеть график с определенной страной нажмите на соответствующую кнопку</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>←--------------------------------</h1>", unsafe_allow_html=True)


