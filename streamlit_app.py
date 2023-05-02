import streamlit as st

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
