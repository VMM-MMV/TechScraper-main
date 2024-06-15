from bs4 import BeautifulSoup
import requests
import time

# Base URL and starting page number
base_url = "https://www.allprices.md"
page_number = 1
total_links = 0

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
        print(link.get('href'))
    
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
