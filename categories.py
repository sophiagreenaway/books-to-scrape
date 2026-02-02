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