from bs4 import BeautifulSoup
import requests
import time

base_url = "https://www.allprices.md"
page_number = 1
total_links = 0

def get_shops_and_price(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table containing the product prices
    product_table = soup.find('table', id='product-prices-list')

    # Find all table rows within the product prices table
    product_rows = product_table.find_all('tr')

    shops = {}
    # Loop through each row and extract the shop name and price
    for row in product_rows:
        try:
            shop_name = row.find('td', class_='col-shop bold').find('a').text
            price_mdl = row.find('div', class_='price price-mdl').find('span', class_='value').text
            shops[shop_name] = price_mdl
        except:
            pass

    time.sleep(1)
    return shops

def get_pc_specs(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    specs = {}

    # Loop through each property group
    for group in soup.select('.property-group'):
        group_title = group.select_one('.group-title').text.strip()
        specs[group_title] = {}
        
        # Loop through each property in the group
        for item in group.select('.properties-list li'):
            title = item.select_one('.title').text.strip().strip(':')
            value = item.select_one('.value').text.strip()
            specs[group_title][title] = value

    # Print the extracted specs
    for category, properties in specs.items():
        print(f"{category}:")
        for title, value in properties.items():
            print(f"  {title}: {value}")

    time.sleep(1)
    return specs

while True:
    # Construct URL for the current page
    url = f"{base_url}/ro/produse/calculatoare/laptop-uri?page={page_number}"
    
    # Send a GET request to fetch the page content
    response = requests.get(url)
    html_content = response.content
    
    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all <a> tags on the page
    links = soup.find_all('a', class_='thumbnail')
    for link in links:
        clean_link = link.get('href')
        shops = get_shops_and_price(f"{base_url}/{clean_link}/preturi")
        specs = get_pc_specs(f"{base_url}/{clean_link}/specificatii")
        print(specs)
        print(shops)

    # Check if there are any links on the page
    if len(links) == 0 or total_links == 100:
        print(f"No more links found on page {page_number - 1}. Exiting.")
        break
    
    # Count the number of links found on this page
    page_links_count = len(links)
    print(f"Found {page_links_count} links on page {page_number}")
    
    # Increment the total link counter
    total_links += page_links_count
    
    # Prepare for the next page
    page_number += 1
    print("-" * 100)
    time.sleep(1)

print(f"Total links found: {total_links}")
