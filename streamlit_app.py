import streamlit as st
import pandas as pd

st.title('My Parents New Healthy Diner')

st.header('Breakfast Favorites')

items = [
          '🥣 Omega 3 & Blueberry Oatmeal',
          '🥗 Kale, Spinach & Rocket Smoothie',
          '🐔 Hard-Boiled Free-Range Egg',
          '🥑🍞 Avocado Toast'
]
list(map(st.text, items))

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# put  pick list
st.multiselect("Pick some fruits:", my_fruit_list.index.tolist())
# display the table on the page
st.dataframe(my_fruit_list)
