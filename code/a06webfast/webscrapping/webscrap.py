#pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'http://quotes.toscrape.com/'

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the quotes (they are inside <span> elements with the class "text")
    quotes = soup.find_all('span', class_='text')
    
    # Loop through all the quotes and print them
    for quote in quotes:
        print(quote.get_text())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
