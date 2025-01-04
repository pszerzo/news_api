import requests
import functions as f
import os

api_key = os.getenv("NEWSAPI")
url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=" \
      "7881f1a5c078402bb47b6f8e82a616d2"
# make request
myrequest = requests.get(url)

# get dictionary
content = myrequest.json()

# send articles
text = ""
for article in content["articles"]:
    text = text + "\n" + str(article["title"]) + "\n" + str(article["content"]) +"\n" *2
f.send_email(text)
