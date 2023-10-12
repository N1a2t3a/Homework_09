import requests
from bs4 import BeautifulSoup
import json

base_url = "http://quotes.toscrape.com"
quotes_url = "/page/1/"
quotes_data = []

while quotes_url:
    page = requests.get(f"{base_url}{quotes_url}")
    soup = BeautifulSoup(page.content, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    for q, a in zip(quotes, authors):
        quote_text = q.get_text()
        author_name = a.get_text()
        tags = [tag.get_text() for tag in a.find_next_sibling("div").find_all("a", class_="tag")]
        quotes_data.append({
            "quote": quote_text,
            "author": author_name,
            "tags": tags
        })

    next_page = soup.find("li", class_="next")
    if next_page:
        quotes_url = next_page.find("a")["href"]
    else:
        quotes_url = None

with open("quotes.json", "w") as quotes_file:
    json.dump(quotes_data, quotes_file, indent=2)
