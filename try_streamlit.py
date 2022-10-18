import streamlit as st
import pandas as pd

@st.cache
def load_data():
         data = pd.read_csv('福-經緯度.csv')
         return data

st.write("""
# 第一個應用程式
嘗試創建**表格**
""",
         data)
