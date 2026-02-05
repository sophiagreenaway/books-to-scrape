import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import BASE_URL

def get_categories():
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, "html.parser")

    categories = []

    nav = soup.find('ul', class_="nav nav-list")
    links = nav.find_all('a')

    #GET ALL CATEGORY NAMES AND URLS
    for a in links:
        name = a.get_text(strip=True)
        if name != "Books":
            url = urljoin(BASE_URL, a['href'])
            categories.append((name, url))
            
    return categories

#SCRAPES URL FOR NEXT PAGE IN CATEGORY

def paginate(category_url):
    current_url = category_url

    while True:
        page = requests.get(current_url)
        soup = BeautifulSoup(page.content, "html.parser")
        
        yield soup
        
        next_link = soup.select_one('li.next a')
        if not next_link:
            break
    
        current_url = urljoin(current_url, next_link['href'])