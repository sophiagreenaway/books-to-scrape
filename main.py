from categories import get_categories, paginate
from products import get_product_page_urls, scrape_product
from exporter import export_to_csv
from images import download_images, get_slug

def clean_filename(name):
    return name.lower().replace(" ", "_")

def main():
    category_urls = get_categories()

    for category_name, category_url in category_urls:
        product_urls = []

        for soup in paginate(category_url):
            page_urls = get_product_page_urls(category_url, soup)
            product_urls.extend(page_urls)

        products = []
        images = {}
        for product_url in product_urls:
            slug = get_slug(product_url)
            product = scrape_product(product_url)
            products.append(product)
            images[slug] = product["image_url"]

        clean_category_name = clean_filename(category_name)
        export_to_csv(f"{clean_category_name}.csv", products)

        download_images(images, clean_category_name)

if __name__ == "__main__":
    main()