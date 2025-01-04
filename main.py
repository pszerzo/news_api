import datetime as datetime
import requests
import functions as f
import os
from datetime import datetime

search = "data science" #input("add it: ")
language = "en"
top = 50
date = datetime.today().strftime('%Y-%mm-%dd')

api_key = os.getenv("NEWSAPI")
url = f"https://newsapi.org/v2/everything?q={search}&from={date}" \
      f"&language={language}&sortBy=publishedAt&apiKey={api_key}"
# make request
myrequest = requests.get(url)

# get dictionary
content = myrequest.json()

# send articles
text = ""
for article in content["articles"][:10]:
    if article["title"] is not None:
        text = f"Subject: Today's {search} news" + "\n" \
               + text \
               + article["title"] + "\n" \
               + article["content"] + "\n" \
               + article["url"] + "\n" * 2
f.send_email(text)
