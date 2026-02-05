import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import BASE_URL

#SCRAPES PRODUCT PAGE URLS

def get_product_page_urls(category_url, soup):
    urls = []

    for a in soup.select("article.product_pod h3 a"):
        relative_url = a["href"]
        full_url = urljoin(category_url, relative_url)
        urls.append(full_url)

    return urls

def scrape_product(product_url):
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")

    #IMAGE URL
    # image = soup.select_one('article.product_page img')
    image = soup.select_one('div.item.active img')
    image_url = urljoin(BASE_URL, image['src'])
    # else:
    #     image_url = None

    #TITLE
    title = soup.find('h1').get_text(strip=True)
    
    #REVIEW RATING
    review_rating = soup.select_one('[class*="star-rating"]')["class"][1]

    #TABLE VALUES
    def get_table_value(soup, label):
        th = soup.find("th", string=label)
        return th.find_next_sibling("td").get_text(strip=True) if th else None

    price_incl = get_table_value(soup, "Price (incl. tax)")
    price_excl = get_table_value(soup, "Price (excl. tax)")
    quantity = get_table_value(soup, "Availability")
    upc = get_table_value(soup, "UPC")


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