import streamlit as st
import pandas as pd

@st.cache
path = 'https://github.com/Ye67890/try/blob/main/%E7%A6%8F-%E7%B6%93%E7%B7%AF%E5%BA%A6.csv'
data = pd.read_csv(path)

st.write("""
# 第一個應用程式
嘗試創建**表格**
""",
         data)
