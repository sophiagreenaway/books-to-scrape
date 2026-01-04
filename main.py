import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv

base_url = "http://books.toscrape.com"
page = requests.get(base_url)
soup = BeautifulSoup(page.content, 'html.parser')

page_url_class = soup.select_one('article', class_='product_pod')
if page_url_class:
    product_url = page_url_class.select_one('a')['href']
product_page_url = urljoin(base_url, product_url)

page = requests.get(product_page_url)
soup = BeautifulSoup(page.content, 'html.parser')

image_class = soup.select_one('article', class_='product page')
src = image_class.select_one('img')
image_relative_url = src.get('src')
image_url = urljoin(base_url, image_relative_url)

div_class = soup.find_all('div', class_='col-sm-6 product_main')
for container in div_class:
    book_title = container.find('h1')

review_rating_class = soup.select_one('[class*="star-rating"]')
review_rating = review_rating_class["class"][1]

upc = soup.find('td')

price_incl_tax_row = soup.find('th', string='Price (incl. tax)')
price_including_tax = price_incl_tax_row.find_next_sibling('td')
price_excl_tax_row = soup.find('th', string='Price (excl. tax)')
price_excluding_tax = price_excl_tax_row.find_next_sibling('td')

quantity_row = soup.find('th', string='Availability')
quantity_available = quantity_row.find_next_sibling('td')

description_class = soup.find('article', class_='product_page')
if description_class:
    product_description = soup.find_all('p', class_=False)

category_class = soup.find('ul', class_='breadcrumb')

if category_class:
    all_lis = category_class.find_all('li')
    i = 0
    for li in all_lis:
        i += 1
        if i == 3:
            category = li.get_text(strip=True)

data = []
data.append(('product_page_url', product_page_url))
data.append(('universal_product_code', image_url))
data.append(('review_rating', review_rating))
data.append(('book_title', book_title.string))
data.append(('universal_product_code', upc.string))
data.append(('price_including_tax', price_including_tax.string))
data.append(('price_excluding_tax', price_excluding_tax.string))
data.append(('quantity_available', quantity_available.string))
data.append(('product_description', product_description[0].string))
data.append(('category', category))

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for i in range(len(data)):
        row = f"{data[i]}"
        csvfile.write(row+'\n')