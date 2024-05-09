import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
#Добавление изображений
image = Image.open("центральная азия.pnd")

st.image(image)
