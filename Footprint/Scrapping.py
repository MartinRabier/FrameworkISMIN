
import requests
from bs4 import BeautifulSoup

def html_site():
    url = input("Enter the URL to scrape: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
