import requests
import bs4

page = requests.get('https://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(page.text, "lxml")

authors = soup.select('.author')
authors_set = set()
for author in authors:
    authors_set.add(author.text)

for author in sorted(authors_set):
    print(author)
print()

quotes = soup.select('.quote')
print(type(quotes))