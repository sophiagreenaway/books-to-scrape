# books-to-scrape

Books-to-Scrape is a Python application that scrapes book pricing and product metadata from the Books to Scrape website. The scraper exports structured data to CSV files and downloads the corresponding book cover images for local storage.

# Features
- Scrapes book data across multiple paginated category pages
- Extracts pricing, availability, and product metadata
- Normalizes and validates URLs
- Downloads and stores images locally
- Outputs clean, structured CSV files
- Skips duplicate records to avoid redundancy

# Setup Instructions

## Requirements
- Python 3
- Requests
- BeautifulSoup
- CSV (Python standard library)

## Usage
Running the script will:

1. Fetch category pages
2. Paginate through results
3. Scrape individual product details
4. Save book data to a CSV file
5. Download and store cover images in nested directories

## Setup
1. Clone the repo
    - git clone https://github.com/sophiagreenaway/books-to-scrape
2. Create and activate your Virtual Environment
    - python -m venv venv venv\Scripts\activate or venv/bin/activate for macOS
3. Install dependencies from requirements.txt
    - pip install -r requirements.txt

## Future Plans
Testing for edge cases
Databasing (SQLite)

## Disclaimer
This project is for educational purposes only.