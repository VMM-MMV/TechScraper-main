from bs4 import BeautifulSoup
import requests
import time
import json

base_url = "https://www.allprices.md"
page_number = 1
total_links = 0

def get_smallest_price_and_shop(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table containing the product prices
    product_table = soup.find('table', id='product-prices-list')

    # Find all table rows within the product prices table
    product_rows = product_table.find_all('tr')

    # Loop through each row and extract the shop name and price
    price_mdl = float('inf')
    shop_name = ""
    for row in product_rows:
        try:
            temp_price = row.find('div', class_='price price-mdl').find('span', class_='value').text
            if int(temp_price) <= price_mdl:
                shop_name = row.find('td', class_='col-shop bold').find('a').text
                price_mdl = temp_price
        except:
            pass

    # time.sleep(1)
    return shop_name, price_mdl

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

    time.sleep(1)
    return specs

all_results = []
try:
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
            name = clean_link.replace("/ro/produse/calculatoare/laptop-uri/", "").replace("-", " ")
            shop, price = get_smallest_price_and_shop(f"{base_url}/{clean_link}/preturi")
            specs = get_pc_specs(f"{base_url}/{clean_link}/specificatii")
            result = {"name": name, "price": price, 'additional_specs': specs, "store_name": shop}
            print(page_number, result)
            all_results.append(result)

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
        # time.sleep(1)
except Exception as e:
    print(e)
    with open(f'results_all_{page_number}.json', 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=4)
    all_results = []

print(f"Total links found: {total_links}")
if len(all_results) != 0:
    with open(f'results_all_{page_number}.json', 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=4)