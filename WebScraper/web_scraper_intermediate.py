# web_scraper_intermediate.py
import requests
from bs4 import BeautifulSoup
import csv

base_url = "http://quotes.toscrape.com/page/{}/"
quotes_list = []

for page in range(1, 6):  # Scrape first 5 pages
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        quotes_list.append([text, author])

# Save to CSV
with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])
    writer.writerows(quotes_list)

print("Scraped quotes saved to 'quotes.csv'")
