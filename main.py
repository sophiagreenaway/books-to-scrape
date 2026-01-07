import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv

# WEBSITE HOMEPAGE
base_url = "http://books.toscrape.com"
page = requests.get(base_url)
soup = BeautifulSoup(page.content, 'html.parser')

#SCRAPE CATEGORY PAGE URLS AND STORE THEM IN A LIST
category_url_list = []
nav_list = soup.find('ul', class_="nav nav-list")
categories = nav_list.find_all('a')
for a in categories:
    if a.get_text(strip=True) != "Books":
        relative_category_url = a['href']
        category_url = urljoin(base_url, relative_category_url)
        category_url_list.append(category_url)

def scrape_all_categories(category_urls: list):
    file_id = 0
    
    for category_url in category_urls:
        #CSV FILE NAME FOR PRODUCT
        file_id += 1
        image_url_list = []

        #NAVIGATE TO CATEGORY PAGE AND SCRAPE THE PRODUCT PAGE URLS
        page = requests.get(category_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # SCRAPE THE AFOREMENTIONED URLS AND STORE THEM IN A LIST
        product_page_url_list = []

        li_class = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
        for container in li_class:
            a = container.find('a')
            page_url = a['href']
            url = urljoin(category_url, page_url)
            product_page_url_list.append(url)

        #GO TO EACH PRODUCT PAGE WITHIN CATEGORY AND SCRAPE THE DATA
        def scrape_all_pages(product_page_urls: list):
            data = []
            for my_url in product_page_urls:

                #GO TO PRODUCT PAGE
                page = requests.get(my_url)
                soup = BeautifulSoup(page.content, 'html.parser')

                #IMAGE URL
                image_class = soup.select_one('article', class_='product page')
                src = image_class.select_one('img')
                image_relative_url = src.get('src')
                image_url = urljoin(base_url, image_relative_url)
                image_url_list.append(image_url)

                #TITLE
                div_class = soup.find_all('div', class_='col-sm-6 product_main')
                for container in div_class:
                    book_title = container.find('h1')
                
                #REVIEW RATING
                review_rating_class = soup.select_one('[class*="star-rating"]')
                review_rating = review_rating_class["class"][1]

                #UPC
                upc = soup.find('td')

                #PRICES
                price_incl_tax_row = soup.find('th', string='Price (incl. tax)')
                price_including_tax = price_incl_tax_row.find_next_sibling('td')
                price_excl_tax_row = soup.find('th', string='Price (excl. tax)')
                price_excluding_tax = price_excl_tax_row.find_next_sibling('td')

                #QUANITY AVAILABLE
                quantity_row = soup.find('th', string='Availability')
                quantity_available = quantity_row.find_next_sibling('td')

                #PRODUCT DESCRIPTION
                description = soup.select_one('#product_description + p')
                product_description = description.get_text(strip=True) if description else None

                #CATEGORY INFORMATION
                category_class = soup.find('ul', class_='breadcrumb')

                if category_class:
                    all_lis = category_class.find_all('li')
                    i = 0
                    for li in all_lis:
                        i += 1
                        if i == 3:
                            category = li.get_text(strip=True)
                
                #APPEND DATA TO A LIST
                data.append(('product_page_url', my_url))
                data.append(('image_url', image_url))
                data.append(('review_rating', review_rating))
                data.append(('book_title', book_title.string))
                data.append(('universal_product_code', upc.string))
                data.append(('price_including_tax', price_including_tax.string))
                data.append(('price_excluding_tax', price_excluding_tax.string))
                data.append(('quantity_available', quantity_available.string))
                data.append(('product_description', product_description))
                data.append(('category', category))
                data.append(' ')

            #EXPORT DATA TO CSV FILE
            filename_csv = f'output_file_{file_id}.csv'
            with open(filename_csv, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                for item in data:
                    writer.writerow(item)
        scrape_all_pages(product_page_url_list)
        
        #EXPORT IMAGES
        image_id = 0
        for image_url in image_url_list:
            image_id += 1
            filename_jpg = f'img_{image_id}.jpg'
            image = requests.get(image_url)
            with open(filename_jpg, 'wb') as f:
                f.write(image.content)
        
scrape_all_categories(category_url_list)