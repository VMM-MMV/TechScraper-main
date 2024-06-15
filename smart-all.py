from requests_html import HTMLSession
from bs4 import BeautifulSoup
import time

# Base URL of the webpage to scrape
base_url = 'https://www.smart.md/laptopuri?'

# Create an HTML session
session = HTMLSession()

offset = 0
while True:
    # Construct the URL with the current offset
    url = f'{base_url}offset={offset}'
    
    # Fetch the HTML content
    response = session.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Render the JavaScript and wait for the page to fully render
        response.html.render()

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.html.html, 'html.parser')

        # Find all product items on the page
        product_items = soup.find_all('div', class_='search-item')

        # If no more product items found, break the loop
        if not product_items:
            print(f"No more products found. Exiting loop.")
            break

        # Iterate over each product item
        for item in product_items:
            # Find product name
            name_element = item.find('h4')
            product_name = name_element.text.strip() if name_element else 'N/A'

            # Find product price
            price_element = item.find('span', class_='regular')
            product_price = price_element.text.strip() if price_element else 'N/A'

            # Print or store the data as needed
            print(f"Product: {product_name}")
            print(f"Price: {product_price}\n")

        # Increment offset for the next page
        offset += 40
        time.sleep(2)
        print('---' * 40)

    else:
        print(f"Failed to retrieve page: {url}")
        break

# Close the session
session.close()
