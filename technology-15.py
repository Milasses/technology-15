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

# Ввод текста
st.markdown("<h1 style='text-align: center; color: green; font-family: Times New Roman; font-size: 20px; '> Для того чтобы увидеть график с определенной страной нажмите на соответствующую кнопку</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 20px; '>←--------------------------------</h1>", unsafe_allow_html=True)

# Function to plot the graph
def plot_graph(values, countries, years):
    plt.figure(figsize=(10, 6))

    for i, values_country in enumerate(values):
        plt.plot(years, values_country, marker='o', linestyle='-', label=countries[i])

    plt.title('Probability of Moderate and Severe Financial Distress')
    plt.xlabel('Year')
    plt.ylabel('Probability')
    plt.xticks(years)
    plt.grid(True)
    plt.legend()

    # Display the graph
    st.pyplot()

# Defining the page
page = st.sidebar.radio('Select Page', ['Home', 'Kazakhstan', 'Tajikistan', 'Kyrgyzstan', 'Uzbekistan', 'Central Asia'])

# Displaying the graph based on the selected page
if page == 'Kazakhstan':
    plot_graph([F_ad_Prob_Mod_Sev_kaz_values], ['Kazakhstan'], years)
elif page == 'Tajikistan':
    plot_graph([F_ad_Prob_Mod_Sev_tjk_values], ['Tajikistan'], years)
elif page == 'Kyrgyzstan':
    plot_graph([F_ad_Prob_Mod_Sev_kgz_values], ['Kyrgyzstan'], years)
elif page == 'Uzbekistan':
    plot_graph([F_ad_Prob_Mod_Sev_uzb_values], ['Uzbekistan'], years)
elif page == 'Central Asia':
    plot_graph([F_ad_Prob_Mod_Sev_kaz_values, F_ad_Prob_Mod_Sev_uzb_values, F_ad_Prob_Mod_Sev_tjk_values, F_ad_Prob_Mod_Sev_kgz_values], ['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'Kyrgyzstan'], years)
