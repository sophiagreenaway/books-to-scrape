# books-to-scrape

This project is a Python application that scrapes book pricing and product data from the *Books to Scrape* website and writes the results to CSV files and saves the book covers as JPGs.

# Setup Instructions

# Requirements
- Python 3.9 or higher
- pip

# Create your Virtual Environment

From the project root directory, run:

(WINDOWS)
1. 
    cd C:\Users\YourName\..\books-to-scrape
2. 
    python -m venv venv 
3. 
    venv\Scripts\activate
4. 
    pip install requests
    pip install bs4
    pip install urljoin
5. 
    venv\Scripts\activate
6. 
    pip install -r requirements.txt
7. 
    python main.py

(macOS)
1. 
    cd ../books-to-scrape
2. 
    python3 -m venv venv 
3. 
    source venv/bin/activate
4. 
    pip install -r requirements.txt
5. 
    python main.py