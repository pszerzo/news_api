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

f.send_email(titles + contents)


    # if article["title"] == "Are You Ultrarich, Rich or Merely Affluent? It Makes a Big Difference for Your Bank":
    #       print(article["content"])
    #       with open("news.txt", "w") as file:
    #             file.write(article["content"])
