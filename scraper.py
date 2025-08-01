import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/index.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

