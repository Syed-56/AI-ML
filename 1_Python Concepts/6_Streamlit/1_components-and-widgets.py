import streamlit as st
#Basic
st.title("Hello Streamlit")
st.write("This is a simple text")

import pandas as pd
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

import numpy as np
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

#Interactive
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}")
    
age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is {age}")

options = ["Python", "Java", "C", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite programming language", options)
st.write(choice)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
#type=["csv", "xlsx", "txt"] can be used to accept multiple types of files

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)