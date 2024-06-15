import requests
from bs4 import BeautifulSoup
import time

base_url = 'https://www.cactus.md/ro/catalogue/electronice/kompyuternaya-tehnika/noutbuki/?sort_=ByView_Descending&page_=page_{}'

page_number = 1
all_products_found = True

while all_products_found:
    # Construct the URL for the current page
    url = base_url.format(page_number)

    # Fetch the HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all product containers on the current page
    product_divs = soup.find_all('div', class_='catalog__pill')

    if len(product_divs) > 0:
        # Process each product found on the page
        for product_div in product_divs:
            # Extract the name
            name_element = product_div.find('span', class_='catalog__pill__text__title')
            product_name = name_element.text.strip() if name_element else 'Name not found'

            # Extract the price
            price_element = product_div.find('div', class_='catalog__pill__controls__price')
            price = price_element.text.strip() if price_element else 'Price not found'

            print(f'Product Name: {product_name}')
            print(f'Price: {price}')
            print('---')

        page_number += 1
        time.sleep(2)
    else:
        # No more products found, terminate the loop
        all_products_found = False

print('Finished scraping all products.')