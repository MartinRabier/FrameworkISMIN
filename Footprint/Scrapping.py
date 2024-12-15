
import requests
from bs4 import BeautifulSoup

def html_site():
    print("This function will scrape the HTML content of a website.")
    print("\nScraping is the process of automatically collecting information from websites. \n The HTML content of the website will be displayed, that content may be very long.\n Please note that some websites may have restrictions on scraping.")
    print(" \n Please enter the URL of the website you want to scrape. Example: https://www.example.com")
    url = input("Enter the URL to scrape: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
