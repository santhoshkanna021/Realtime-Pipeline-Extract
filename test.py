import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://quotes.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span" ,class_="text")
author = soup.find_all("small" ,class_="author")

data = []

for q, a in zip(quotes, author):
    data.append({
        "quote": q.text,
        "author": a.text
    })

df = pd.DataFrame(data)

df.to_csv("data/raw_data.csv", index=False)

print("Data will be convert into an csv file")
