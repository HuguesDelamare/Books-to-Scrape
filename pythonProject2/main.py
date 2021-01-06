import requests
from bs4 import BeautifulSoup
import re

all_book_datas = []
#Utiliser librairie python recup image
#Fonction pour faire fichier CSV
#Changer les noms des variables ( plus lisibles)


### Fonction permettant de récupèrer les urls des books d'une catégorie ###
def get_books_from_category(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup('article')
        for book in books:
            book_href = book.find('a')
            href = book_href['href']
            split = href.split('../')
            href = split[3]
            url_article = 'http://books.toscrape.com/catalogue/' + str(href)
            book_data = get_book_info(url_article)
        try:
            next_page_selector = soup.find('section').find('li', {'class': 'next'}).select('a')
            print("Found next page")
            next_page_href = next_page_selector[0]['href']
            url_split = url.rsplit("/", 1)
            next_page_url = url_split[0] + str("/" + next_page_href)
            print(" Next page : " + next_page_url)
            get_books_from_category(next_page_url)
        except:
            pass

###  Fonction permettant de récupérer les infos d'un article(book) ###
def get_book_info(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            article_url = url
            article_stock_selector = str(soup.find('table', {'class': 'table table-striped'}).select('td')[5].text)
            article_stock = re.findall(r'\d+', article_stock_selector)[0]
            article_description = soup.find('article', {'class': 'product_page'}).select('p')[3].text
            article_upc = soup.find('table', {'class': 'table table-striped'}).select('td')[0].text
            article_price_including_tax = soup.find('table', {'class': 'table table-striped'}).select('td')[
                3].text
            article_price_excluding_tax = soup.find('table', {'class': 'table table-striped'}).select('td')[
                2].text
            article_category = soup.find('ul', {'class': 'breadcrumb'}).select('li')[2].text
            article_review_selector = soup.find('div', {'class': 'col-sm-6 product_main'}).select('p')[2]['class'][1]
            if article_review_selector == "One":
                article_review = int(1)
            elif article_review_selector == "Two":
                article_review = int(2)
            elif article_review_selector == "Three":
                article_review = int(3)
            elif article_review_selector == "Four":
                article_review = int(4)
            elif article_review_selector == "Five":
                article_review = int(5)
            else:
                article_review = int(0)
            article_picture_selector = soup.find('div', {'class': 'item active'}).select('img')[0]['src']
            article_picture_split = article_picture_selector.split('../')[2]
            article_picture_src_link = 'http://books.toscrape.com/' + article_picture_split
            article_title = soup.find('div', {'class': 'col-sm-6 product_main'}).select('h1')[0].text
            book_datas = [article_url, article_upc, article_title, article_price_including_tax,
                          article_price_excluding_tax, article_stock, article_description, article_category,
                          article_review, article_picture_src_link]
            return book_datas
            #all_book_datas.append(book_datas)
    #check_result(all_book_datas)

#def find_next_page(soup, url):


### Fonction pour trouver toutes les catégories présentes sur le site ###
def get_books_categories():
    main_page_url = 'http://books.toscrape.com/index.html'
    response_main_page_url = requests.get(main_page_url)
    if response_main_page_url.ok:
        soup1 = BeautifulSoup(response_main_page_url.text, 'html.parser')
        #for category in soup1.find('ul', {'class': 'nav nav-list'}).find('ul').select('li'):
            #category_link = "http://books.toscrape.com/" + category.a['href']
        get_books_from_category('http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html')

def check_result(array):
    for result in array:
        print(result)

### DEMARAGE DU CODE ###
get_books_categories()


