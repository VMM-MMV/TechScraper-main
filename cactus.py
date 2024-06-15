import requests
from bs4 import BeautifulSoup

# URL of the page containing the product information
url = f'https://www.cactus.md/ro/catalogue/electronice/kompyuternaya-tehnika/noutbuki/?sort_=ByView_Descending&page_=page_{}'

# Fetch the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the product container
product_div = soup.find('div', class_='catalog__pill')

if product_div:
    # Extract the name
    name_element = product_div.find('span', class_='catalog__pill__text__title')
    product_name = name_element.text.strip() if name_element else 'Name not found'

    # Extract the price
    price_element = product_div.find('div', class_='catalog__pill__controls__price')
    price = price_element.text.strip() if price_element else 'Price not found'

    # Print the results
    print(f'Product Name: {product_name}')
    print(f'Price: {price}')
else:
    print('Product not found on the page.')
