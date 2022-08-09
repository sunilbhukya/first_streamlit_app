import streamlit
import pandas as pd
import snowflake.connector
from urllib.error import URLError
import requests
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

def fruitt(fc):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fc)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
streamlit.header("Frutyvice advise")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("pleae enter inf")
  else:
    bf=fruitt(fruit_choice)
# write your own comment - what does this do?
    streamlit.dataframe(bf)
except URLError as e:
  streamlit.error()

# write your own comment -what does the next line do? 
streamlit.header("This Fruit Load List Contanis:")
def load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
if streamlit.button('get fruit list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    myrows=load_list()
    streamlit.dataframe(myrows)
    
    
def insert(new):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "thanks fror adding"
    
addfruit=streamlit.text_input('what you want to ad')
if streamlit.button('adding'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    backfrom=insert(addfruit)
    streamline.text(backfrom)

       
    


 
        












