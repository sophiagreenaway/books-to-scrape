import requests

def download_images(image_urls):
    for i, url in enumerate(image_urls, start=1):
        img = requests.get(url)
        with open(f"img_{i}.jpg", "wb") as img_file:
            img_file.write(img.content)