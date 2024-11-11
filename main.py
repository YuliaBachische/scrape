import requests
from bs4 import BeautifulSoup
import json

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes_data = []

for quote in soup.select('.quote'):
    text = quote.find(class_='text').get_text(strip=True)
    author = quote.find(class_='author').get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in quote.select('.tag')]
    quotes_data.append({
        'text': text,
        'author': author,
        'tags': tags
    })

with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump(quotes_data, f, ensure_ascii=False, indent=4)
