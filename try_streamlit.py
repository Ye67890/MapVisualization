import streamlit as st
import pandas as pd

@st.cache
path = '福-經緯度.csv'
data = pd.read_csv(path)

st.write("""
# 第一個應用程式
嘗試創建**表格**
""",
         data)
