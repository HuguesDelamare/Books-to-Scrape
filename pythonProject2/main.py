import requests
from bs4 import BeautifulSoup
import re
import csv
import os

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
            next_page_href = next_page_selector[0]['href']
            url_split = url.rsplit("/", 1)
            next_page_url = url_split[0] + str("/" + next_page_href)
            print(" Page suivante : " + next_page_url)
            get_books_from_category(next_page_url)
        except:
            pass

###  Fonction permettant de récupérer les infos d'un article(book) via le HTML & CSS ###
def get_book_info(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            article_url = str(url)
            article_stock_selector = str(soup.find('table', {'class': 'table table-striped'}).select('td')[5].text)
            article_stock = re.findall(r'\d+', article_stock_selector)[0]
            article_description = str(soup.find('article', {'class': 'product_page'}).select('p')[3].text)
            article_upc = str(soup.find('table', {'class': 'table table-striped'}).select('td')[0].text)
            article_price_including_tax = str(soup.find('table', {'class': 'table table-striped'}).select('td')[
                3].text)
            article_price_excluding_tax = str(soup.find('table', {'class': 'table table-striped'}).select('td')[
                2].text)
            article_category = str(soup.find('ul', {'class': 'breadcrumb'}).select('li')[2].text).replace("\n", '')
            print(article_category)
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
            article_picture_src_link = str('http://books.toscrape.com/' + article_picture_split)
            article_title = str(soup.find('div', {'class': 'col-sm-6 product_main'}).select('h1')[0].text)
            get_book_picture(article_picture_src_link, article_title, article_category)
            book_datas = {'product_page_url': article_url, 'upc': article_upc, 'title': article_title, 'price_including_tax': article_price_including_tax, 'price_excluding_tax': article_price_excluding_tax, 'number_available': article_stock, 'product_description': article_description, 'category': article_category, 'review_rating': article_review, 'image_url': article_picture_src_link}
            create_csv_file(article_category, book_datas)
            return book_datas

###  Fonction pour créer le fichier csv contenant les données des différents livres ###
def create_csv_file(category, data):
    ### On tente de chercher le dossier ou deposer le fichier CSV ###
    try:
        with open('csv_files/' + category + '.csv', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            ### Si on trouve le dossier correspondant, on ajoute les données dans le fichier existant ###
            if reader:
                with open('csv_files/' + category + '.csv', 'a', encoding='UTF8', newline='') as csv_file:
                    header = ['product_page_url', 'upc', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
                    writer = csv.DictWriter(csv_file, fieldnames=header)
                    writer.writerow(data)
    ### Si on ne trouve pas le dossier pour deposer le fichier CSV ####
    except FileNotFoundError:
        ### On créée le fichier dans le dossier ###
        with open('csv_files/' + category + '.csv', 'w', encoding='UTF8', newline='') as csv_file:
            header = ['product_page_url', 'upc', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
            writer = csv.DictWriter(csv_file, fieldnames=header)
            writer.writeheader()
            writer.writerow(data)
    finally:
        print("Enregistrement des données dans fichier csv " + category)

###  Fonction pour stocker les images des différents livres dans un dossier ###
def get_book_picture(file_url, file_name, file_category):
    r = requests.get(file_url)
    picture_name = re.sub('[^A-Za-z0-9]+', '', file_name)
    try:
        os.mkdir('./books_cover_pictures')
    except Exception:
       pass
    if os.path.isdir('./books_cover_pictures/' + file_category):
        file_path = 'books_cover_pictures/'+ file_category + '/' + picture_name + '.' + file_url.split('.')[-1]
        with open(file_path, 'wb') as file:
            file.write(r.content)
    else:
        os.makedirs('./books_cover_pictures/' + file_category)
        file_path = 'books_cover_pictures/' + file_category + '/' + picture_name + '.' + file_url.split('.')[-1]
        with open(file_path, 'wb') as file:
            file.write(r.content)

### Fonction pour trouver toutes les catégories présentes sur le site ###
def get_books_categories():
    try:
        os.mkdir('./csv_files')
    except Exception as e:
        pass
    main_page_url = 'http://books.toscrape.com/index.html'
    response_main_page_url = requests.get(main_page_url)
    if response_main_page_url.ok:
        soup = BeautifulSoup(response_main_page_url.text, 'html.parser')
        category_selector = soup.find('ul', {'class': 'nav nav-list'}).find('ul').select('li')
        for category in category_selector:
            print("Catégorie suivante")
            category_link = 'http://books.toscrape.com/' + category.a['href']
            get_books_from_category(category_link)

### DEMARAGE DU CODE ###
get_books_categories()

