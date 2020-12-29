import requests
from bs4 import BeautifulSoup
import re

links = []

#Boucle pour parcourir les
for i in range(1, 4):
    url = 'http://books.toscrape.com/catalogue/category/books/fantasy_19/page-' + str(i) + '.html'
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup('article')

        for article in articles:
            a = article.find('a')
            href = a['href']
            split = href.split('../')
            href = split[3]
            url_article = 'http://books.toscrape.com/catalogue/' + str(href)
            response2 = requests.get(url_article)
            if response2.ok:
                soup2 = BeautifulSoup(response2.text, 'html.parser')
                article_link = url_article
                article_stock_selector = str(soup2.find('table', {'class': 'table table-striped'}).select('td')[5].text)
                article_stock = re.findall(r'\d+', article_stock_selector)[0]
                article_description = soup2.find('article', {'class': 'product_page'}).select('p')[3].text
                article_upc = soup2.find('table', {'class': 'table table-striped'}).select('td')[0].text
                article_price_including_tax = soup2.find('table', {'class': 'table table-striped'}).select('td')[3].text
                article_price_excluding_tax = soup2.find('table', {'class': 'table table-striped'}).select('td')[2].text
                article_category = soup2.find('ul', {'class': 'breadcrumb'}).select('li')[2].text
                article_review = ""
                article_picture_selector = soup2.find('div', {'class': 'item active'}).find('img')
                article_picture = article_picture_selector['src']
                article_title = soup2.find('div', {'class': 'col-sm-6 product_main'}).select('h1')[0].text
                print(article_stock)
