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

            product_name = re.sub(r'\s*\((?!\d{4}\)).*?\)', '', product_name).replace("Laptop", "").strip()

            # Extract the price
            price_element = product_div.find('div', class_='catalog__pill__controls__price')
            price = price_element.text.strip() if price_element else 'Price not found'

            print(f'Product Name: {product_name}')
            print(f'Price: {price}')
            print('---')

        page_number += 1
        time.sleep(1)
    else:
        # No more products found, terminate the loop
        all_products_found = False

print('Finished scraping all products.')

Apple MacBook Air 15" MQKU3 (2023) (M2, 8GB, 256GB) Starlight
Price: 27 739lei
---
Product Name: Laptop Apple MacBook Air 15" MQKX3 (2023) (M2, 8GB, 512GB) Midnight
Price: 29 525lei
---
Product Name: Laptop Apple MacBook Air 15" MQKW3 (2023) (M2, 8GB, 256GB) Midnight
Price: 28 304lei
---
Product Name: Laptop Apple MacBook Pro 16" MRW43 2023 (M3 Pro, 18Gb, 512Gb) Silver
Price: 58 496lei
---
Product Name: Laptop Apple MacBook Pro 16" MRW63 2023 (M3 Pro, 36Gb, 512Gb) Silver
Price: 73 592lei
---
Product Name: Laptop Apple MacBook Pro 16" MRW13 2023 (M3 Pro, 18Gb, 512Gb) Space Black
Price: 57 719lei
---
Product Name: Laptop Apple MacBook Pro 16" MRW23 2023 (M3 Pro, 36Gb, 512Gb) Space Black
Price: 73 592lei
---
Product Name: Laptop Apple MacBook Pro 14" MRX33 2023 (M3 Pro, 18Gb, 512Gb) Space Black
Price: 46 619lei
---
Product Name: Laptop Apple MacBook Pro 14" MRX43 2023 (M3 Pro, 18Gb, 1Tb) Space Black
Price: 53 279lei
---
Product Name: Laptop Apple MacBook Pro 14" MRX63 2023 (M3 Pro, 18Gb, 512Gb) Silver
Price: 46 619lei
---
Product Name: Laptop Apple MacBook Pro 14" MRX73 2023 (M3 Pro, 18Gb, 1Tb) Silver
Price: 54 389lei
---
Product Name: Laptop Apple MacBook Pro 14" MRX53 2023 (M3 Max, 36Gb, 1Tb) Space Black
Price: 80 696lei
---
Product Nam