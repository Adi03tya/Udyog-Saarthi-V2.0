import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = r"F:\new project\Udyog-Saarthi-Version-2.0\myproject\udyogSaarthi\templates\home.html"

with open(url, "r", encoding="utf-8") as file:
    html_content = file.read()
# Send a GET request to the webpage
# response = requests.get(url)

# Create a BeautifulSoup object with the webpage content
soup = BeautifulSoup(html_content, "html.parser")

# Use BeautifulSoup methods to extract data from the webpage
# ...

# Example: Print the title of the webpage
# title = soup.title.string
# print("Title:", title)
print(soup.get_text())
