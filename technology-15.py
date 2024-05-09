import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
#Добавление изображений
background_image = "искендерькульtourister.ru.jpg"

# Устанавливаем фоновое изображение
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url("{background_image}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
