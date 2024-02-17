import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu

@st.cache_data
#load data csv 
@st.cache
def load_data():
    # Proses memuat data
    return pd.read_csv('day.csv')

def load_data():
    # Proses memuat data
    return pd.read_csv('hour.csv')

df = load_data()

# Tampilkan DataFrame
st.dataframe(df)
