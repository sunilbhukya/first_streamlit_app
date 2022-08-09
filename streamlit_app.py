import streamlit
import pandas as pd
import snowflake.connector
streamlit.title('My parents New Healthy Dinner')
streamlit.header('breakfast menu')
streamlit.text('🥣 omega 3 & bluberry oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
selected=streamlit.multiselect('pick some fruits:',list(my_fruit_list.index),['Avocado','Strawberries'])
view=my_fruit_list.loc[selected]
streamlit.dataframe(view)

