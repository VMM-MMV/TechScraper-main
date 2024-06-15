from bs4 import BeautifulSoup
import requests

# URL of the page
base_url = "https://www.allprices.md"
url = base_url + '/ro/produse/calculatoare/laptop-uri?page=1'

# Send a GET request to fetch the page content
response = requests.get(url)
html_content = response.content

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the specific <a> tag based on the class or other identifying attributes
# In this case, we're looking for the <a> tag with class="thumbnail"
thumbnail_link = soup.find('a', class_='thumbnail')

# Extract the href attribute if the <a> tag is found
if thumbnail_link:
    laptop_url = thumbnail_link.get('href')
    print("Link found:", base_url + laptop_url)
else:
    print("Link not found")

