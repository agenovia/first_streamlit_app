import streamlit
import pandas
import requests
import snowflake.connector

st = streamlit
pd = pandas

st.title("My Mom's New Healthy Diner")

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


st.header("FruityVice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice.strip().lower()}")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


# add a fruit to the fruit_load_list table
add_fruit = streamlit.text_input('What fruit would you like to add?')
add_fruit = add_fruit.strip().lower()
if len(add_fruit) > 0:
          my_cur.execute(f"INSERT INTO fruit_load_list VALUES ('{add_fruit}')")
          streamlit.write("Thanks for adding ", add_fruit)
