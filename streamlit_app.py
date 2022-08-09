import streamlit
import pandas as pd
#123
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

import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("This Fruit Load List Contanis:")
df=streamlit.dataframe(my_data_row)
title = streamlit.text_input('Which fruit you want to add', 'jackfruit')
streamlit.write('Thanks for adding', title)
df.loc[len(df.index)] = ['jackfruit'] 

data=['jackfruit']
df2 = pd.DataFrame(data)
df1=df.append(df2)
stream.dataframe(df1)
