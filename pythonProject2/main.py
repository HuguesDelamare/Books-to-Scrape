import requests
from bs4 import BeautifulSoup
import re
import csv

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
            #print(book_data)
        try:
            next_page_selector = soup.find('section').find('li', {'class': 'next'}).select('a')
            #print("Found next page")
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
            book_datas = {'product_page_url': article_url, 'upc': article_upc, 'title': article_title, 'price_including_tax': article_price_including_tax,
                          'price_excluding_tax': article_price_excluding_tax, 'number_available': article_stock, 'product_description': article_description, 'category': article_category,
                          'review_rating': article_review, 'image_url': article_picture_src_link}
            create_csv_file(article_category.replace("\n",''), book_datas)
            return book_datas

def create_csv_file(category, data):
    with open('csv_files/'+ category + '.csv', 'w', encoding='UTF8', newline='') as csv_file:
        #category = category.replace("\n", '')
        header = ['product_page_url', 'upc', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available',
                  'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(csv_file, fieldnames=header, dialect='excel')

        writer.writeheader()
        writer.writerow(data)

### Fonction pour trouver toutes les catégories présentes sur le site ###
def get_books_categories():
    main_page_url = 'http://books.toscrape.com/index.html'
    response_main_page_url = requests.get(main_page_url)
    if response_main_page_url.ok:
        soup = BeautifulSoup(response_main_page_url.text, 'html.parser')
        category_selector = soup.find('ul', {'class': 'nav nav-list'}).find('ul').select('li')
        for category in category_selector:
            #category_name = " ".join(category.a.text.split())
            #print("New category : " + category)
            category_link = "http://books.toscrape.com/" + category.a['href']
            get_books_from_category(category_link)

### DEMARAGE DU CODE ###
get_books_categories()

