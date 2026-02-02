from categories import get_categories
from products import get_product_page_urls, scrape_product
from exporter import export_to_csv
from images import download_images

def clean_filename(name):
    return name.lower().replace(" ", "_")

def main():
    category_urls = get_categories()

    for category_name, category_url in category_urls:

        product_urls = get_product_page_urls(category_url)

        products = []
        images = []

        for url in product_urls:
            product = scrape_product(url)
            products.append(product)
            images.append(product["image_url"])

        export_to_csv(f"{clean_filename(category_name)}.csv", products)

        download_images(images)


if __name__ == "__main__":
    main()