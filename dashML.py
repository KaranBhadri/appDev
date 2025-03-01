import streamlit as st
import pandas as pd

st.title('🏆 XPLAINABLE MODEL')
st.info("This app will create an explainable model output")

with st.expander('**DATA**'):
  st.write('**input data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
  
  st.write('**X**')
  X = df.drop('species', axis=1)
  X

  st.write('**Y**')
  Y = df.species
  Y

with st.expander('**VISUALIZATIONS**'):
  st.write('**By Island**')
  st.scatter_plot(data=df, x='bill_depth_mm', y='body_mass_g', color='island')
  st.write('**By Species**')
  st.scatter_plot(data=df, x='bill_depth_mm', y='body_mass_g', color='species')

