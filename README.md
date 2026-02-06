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

## Create your Virtual Environment
From the project root directory:

### Windows
- cd C:\Users\YourName\..\books-to-scrape
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- python main.py

### macOS
- cd ../books-to-scrape
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python main.py

## Future Plans
Testing for edge cases
Unit tests
Error handling (try/catch)
Databasing (SQLite)

## Disclaimer
This project is for educational purposes only.