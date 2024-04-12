import requests
import bs4

page = requests.get('https://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(page.text, "lxml")

# Get all the authors' names on the first page
authors = soup.select('.author')
authors_set = set()
for author in authors:
    authors_set.add(author.text)

for author in sorted(authors_set):
    print(author)
print()

# Get all the quotes on the first page
quotes = soup.select('.quote .text')
for quote in quotes:
    print(quote.text)
print()

# Get the top tags from the right side
tags = soup.select('.tag-item .tag')
for tag in tags:
    print(tag.text)

# Get all the unique authors from all pages
webpage = 'https://quotes.toscrape.com/page/{}/'
page = 1
authors_set = set()
while True:
    content = requests.get(webpage.format(page))
    if 'No quotes found!' in content.text:
        break
    soup = bs4.BeautifulSoup(content.text, "lxml")
    authors = soup.select('.author')
    for author in authors:
        authors_set.add(author.text)
    page+=1

for author in sorted(authors_set):
    print(author)