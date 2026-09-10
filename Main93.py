# E50.News App in Python.
import requests;
import json;
query = input("What Type of News are you Interested in? : ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-08-10&sortBy=publishedAt&apiKey=32cddf192f26445d900d7284ba75c1c3"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news)).
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------------------")