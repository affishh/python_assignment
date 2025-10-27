## Develop a simple web scraper to extract data from a website?
import requests
import bs4 as BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup.BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")
for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_ = "author").get_text()
    tags = [tag.get_text() for tag in quote.find_all("a", class_ = "tag")]

print(f"Quotes scraped from the website:, {text}")
print(f"Author: {author}")
print(f"Tags: {', '.join(tags)}")
print("-" * 80)

images = soup.find_all('img')
for image in images:
        print(f'Image: {image.get("src")}')
else:
    print(f'Failed to retrieve webpage. Status code: {response.status_code}')
