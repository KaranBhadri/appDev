import streamlit as st
import pandas as pd

st.title('🏆 XPLAINABLE MODEL')
st.write("Hello World")

with st.expander('**DATA**'):
  st.write('**input data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

