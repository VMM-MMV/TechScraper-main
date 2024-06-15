import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://darwin.md/laptopuri?page=1"

# Make a request to the webpage
response = requests.get(url)

# Parse the webpage content
soup = BeautifulSoup(response.content, "html.parser")
# Find all product items based on the structure provided
# products = soup.find_all("a", class_="d-block mb-2 ga-item")
products = soup.find_all("a")

print(products)
# Extract names and prices
product_list = []
for product in products:
    name = product.get("title")
    price_data = product.get("data-ga4")
    price = price_data.split('"price":')[1].split(",")[0] if price_data else "N/A"
    product_list.append((name, price))

print(product_list)
