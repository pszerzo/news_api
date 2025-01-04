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

# access titles
titles = []
contents = []
for article in content["articles"]:
    titles.append(article["title"])
    contents.append(article["content"])

text = titles + contents
print(text)

f.send_email(text)
