import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            writer.writerow([text, author])

    print("Data scraped successfully and saved into quotes.csv")

except requests.exceptions.RequestException:
    print("Failed to fetch website data")
