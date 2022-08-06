import streamlit
import pandas as pd
streamlit.title('My parents New Healthy Dinner')
streamlit.header('breakfast menu')
streamlit.text('🥣 omega 3 & bluberry oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index), ['Avocado' , 'Strawberries'])


#fruits_selected=streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index), ['Avocado' , 'Strawberries'])
#fruits_to_show=my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(fruits_to_show)
