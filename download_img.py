import requests

url = "https://kiszamolo.hu/wp-content/uploads/2024/12/Kepernyokep-2024-12-25-180825.png"
response = requests.get(url)
# print(response.text)
with open("image.png", "wb") as file:
    file.write(response.content)