import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import BASE_URL

#SCRAPES PRODUCT PAGE URLS

def get_product_page_urls(category_url):
    page = requests.get(category_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    urls = []

    containers = soup.find_all(
        'li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'
    )

    for container in containers:
        a = container.find('a')
        urls.append(urljoin(category_url, a['href']))
    
    return urls

def scrape_product(product_url):
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")

    #IMAGE URL
    image = soup.select_one('article.product_page img')
    image_url = urljoin(BASE_URL, image['src'])

    #TITLE
    title = soup.find('h1').get_text(strip=True)
    
    #REVIEW RATING
    review_rating = soup.select_one('[class*="star-rating"]')["class"][1]

    #UPC
    upc = soup.find('td').get_text(strip=True)

    #PRICES
    price_incl = soup.find('th', string='Price (incl. tax)')\
        .find_next_sibling('td').get_text(strip=True)
    
    price_excl = soup.find('th', string='Price (excl. tax)')\
        .find_next_sibling('td').get_text(strip=True)

    #QUANITY AVAILABLE
    quantity = soup.find('th', string='Availability')\
        .find_next_sibling('td').get_text(strip=True)

    #PRODUCT DESCRIPTION
    description = soup.select_one('#product_description + p')
    product_description = description.get_text(strip=True) if description else None

    #CATEGORY INFORMATION
    breadcrumb = soup.find('ul', class_='breadcrumb')
    category = breadcrumb.find_all("li")[2].get_text(strip=True)
    
    return {
        "product_page_url": product_url,
        "image_url": image_url,
        "review_rating": review_rating,
        "title": title,
        "upc": upc,
        "price_including_tax": price_incl,
        "price_excluding_tax": price_excl,
        "quantity_available": quantity,
        "product_description": product_description,
        "category": category,
    }