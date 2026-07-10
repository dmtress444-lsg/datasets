import streamlit as st
import pandas as pd
st.title("hello world web")
st.write("hellow world streamlit")
dataframe= pd.read_csv ("https://raw.githubusercontent.com/dmtress444-lsg/datasets/refs/heads/main/titanic.csv")
st.dataframe(dataframe) 
