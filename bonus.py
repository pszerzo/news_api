import streamlit as st
import requests
import os
import datetime

today = "2024-11-05" #datetime.datetime.today().strftime('%Y-%m-%d')
my_key = os.getenv("NASAAPI")
url = f"https://api.nasa.gov/planetary/apod?api_key={my_key}&date={today}"
my_request = requests.get(url)
content = my_request.json()

my_title = content["title"]
my_text = content["explanation"]
pict = content["url"]
pict_req = requests.get(pict)

with open("daily.png", "wb") as file:
    file.write(pict_req.content)

# st.set_page_config(layout="wide")
st.title(my_title)
st.image("daily.png")#, width=400)
st.write(my_text)
