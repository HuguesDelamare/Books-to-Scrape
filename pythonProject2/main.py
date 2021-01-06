import requests
from bs4 import BeautifulSoup
import re


def get_books_infos_from_category(url):
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            books = soup('article')
            get_books_infos(books)

def get_books_infos(books):
    all_book_datas = []
    for book in books:
        book_href = book.find('a')
        href = book_href['href']
        split = href.split('../')
        href = split[3]
        url_article = 'http://books.toscrape.com/catalogue/' + str(href)
        response2 = requests.get(url_article)
        if response2.ok:
            soup2 = BeautifulSoup(response2.text, 'html.parser')
            article_url = url_article
            article_stock_selector = str(soup2.find('table', {'class': 'table table-striped'}).select('td')[5].text)
            article_stock = re.findall(r'\d+', article_stock_selector)[0]
            article_description = soup2.find('article', {'class': 'product_page'}).select('p')[3].text
            article_upc = soup2.find('table', {'class': 'table table-striped'}).select('td')[0].text
            article_price_including_tax = soup2.find('table', {'class': 'table table-striped'}).select('td')[
                3].text
            article_price_excluding_tax = soup2.find('table', {'class': 'table table-striped'}).select('td')[
                2].text
            article_category = soup2.find('ul', {'class': 'breadcrumb'}).select('li')[2].text
            article_review_selector = soup2.find('div', {'class': 'col-sm-6 product_main'}).select('p')[2]['class'][1]
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
            article_picture_selector = soup2.find('div', {'class': 'item active'}).find('img')
            article_picture = article_picture_selector['src']
            article_title = soup2.find('div', {'class': 'col-sm-6 product_main'}).select('h1')[0].text
            article_image = "image.png"
            book_datas = [article_url, article_upc, article_title, article_price_including_tax,
                          article_price_excluding_tax, article_stock, article_description, article_category,
                          article_review, article_image]
            all_book_datas.append(book_datas)
    check_result(all_book_datas)

def find_next_page(soup, url):
    next_page_selector = soup.find('section').find('li', {'class': 'next'}).select('a')
    if next_page_selector == " " or next_page_selector is None:
        print("No next page found")
        return
    else:
        next_page_href = next_page_selector[0]['href']
        url_split = url.rsplit("/", 1)
        next_page_url = url_split[0] + str("/" + next_page_href)
        return next_page_url

### Fonction pour trouver toutes les catégories présentes sur le site   ###
def get_books_categories():
    #print('get_books_categories called')
    main_page_url = 'http://books.toscrape.com/index.html'
    response_main_page_url = requests.get(main_page_url)
    if response_main_page_url.ok:
        soup1 = BeautifulSoup(response_main_page_url.text, 'html.parser')
        #for category in soup1.find('ul', {'class': 'nav nav-list'}).find('ul').select('li'):
            #category_link = "http://books.toscrape.com/" + category.a['href']
        get_books_infos_from_category('http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html')

def check_result(array):
    for result in array:
        print(result[2])
        print(result[8])

### DEMARAGE DU CODE ###
get_books_categories()


