import streamlit as st
import pandas as pd
import numpy as np

# st.write("hello")
# x= st.text_input("favourite movie")
# st.write(f"your favourite movie is {x}")

titanic_data = pd.read_csv("titanic3.csv")
st.write(titanic_data)

chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])


st.bar_chart(chart_data)