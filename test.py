from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json

# Function to extract name and price
def extract_laptop_info(element):
    name = element.get_attribute('title')
    data_ga4 = element.get_attribute('data-ga4')
    data_ga4_json = json.loads(data_ga4)
    price = data_ga4_json['ecommerce']['value']
    return name, price

# Set up the Selenium WebDriver using WebDriverManager
driver = webdriver.Chrome()

# Load the webpage
url = 'https://darwin.md/laptopuri?page=1'
driver.get(url)

# Find all laptop elements
laptop_elements = driver.find_elements(By.CLASS_NAME, 'ga-item')

# Extract and print name and price for each laptop
for element in laptop_elements:
    name, price = extract_laptop_info(element)
    print(f"Name: {name}")
    print(f"Price: {price} MDL")
    print("-" * 30)

# Quit the WebDriver
driver.quit()
