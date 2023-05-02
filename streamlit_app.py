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
my_fruit_list.set_index("Fruit", drop=True, inplace=True)

# put  pick list
fruits_selected = st.multiselect("Pick some fruits:", my_fruit_list.index.tolist(), my_fruit_list.index.tolist()[:2])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# display the table on the page
st.dataframe(fruits_to_show)
