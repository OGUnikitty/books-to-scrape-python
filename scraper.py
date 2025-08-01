import requests
from bs4 import BeautifulSoup

# Book definition
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

# Database container
database = []

def getBookDetail(container):
    books = container.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('div', class_='product_price').find('p', class_='price_color').text.strip()
        
        # Create a new Book object and add it to the database list
        database.append(Book(
            title=title,
            price=price
        ))

def getEveryPage():
    # Since number of pages could have been dynamic, a calculation for number of paginations would be included
    # But for now I know that there are 50

    for page_number in range(1, 51):  # This will loop from 1 to 50
        url = f"http://books.toscrape.com/catalogue/page-{page_number}.html"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # Main page content
        main_container = soup.find('div', class_='col-sm-8 col-md-9')
        getBookDetail(main_container)

getEveryPage()
print(len(database)) # This should print 1000