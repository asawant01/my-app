import streamlit as st
num_1 = st.slider('Choose your number', 1,100)
num_2 = st.slider('choose your second number', 1,100)
st.write('Sum of 2 numbers', num_1 + num_2)
st.write('Difference between 2 numbers', num_1 - num_2)
st.write('Product of 2 numbers', num_1*num_2)
st.write('Square of ', num_1, 'is', num_1**2)