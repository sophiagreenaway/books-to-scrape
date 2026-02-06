import requests
import os
from urllib.parse import urlparse

def get_slug(product_url):
    path = urlparse(product_url).path
    return path.strip("/").split("/")[-2]

def download_images(image_url_and_slug, category):
    folder = f"images/{category}"
    os.makedirs(folder, exist_ok=True)
    
    for slug, url in image_url_and_slug.items():
        path = f"{folder}/{slug}.jpg"

        if os.path.exists(path):
            continue
        
        url = url.replace("http://", "https://", 1)

        response = requests.get(url)
        response.raise_for_status()

        with open(path, "wb") as file:
            file.write(response.content)