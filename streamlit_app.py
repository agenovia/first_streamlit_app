import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')

items = [
          '🥣 Omega 3 & Blueberry Oatmeal',
          '🥗 Kale, Spinach & Rocket Smoothie',
          '🐔 Hard-Boiled Free-Range Egg',
          '🥑🍞 Avocado Toast'
]
list(map(streamlit.text, items))
