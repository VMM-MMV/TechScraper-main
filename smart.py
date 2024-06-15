from requests_html import HTMLSession
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.smart.md/laptopuri?offset=120'

# Create an HTML session
session = HTMLSession()

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

else:
    print(f"Failed to retrieve page: {url}")

# Close the session
session.close()
