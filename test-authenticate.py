from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth

# Configure Chrome webdriver with stealth options
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Initialize Chrome webdriver with configured options
driver = webdriver.Chrome(options=options)

# Apply stealth settings to mimic human behavior
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
)

# Navigate to the target website
driver.get("https://darwin.md/laptopuri?page=1")

# Print page title to verify navigation
print("Page title:", driver.title)

try:
    # Wait for the checkbox to be clickable
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Verify you are human"]/preceding-sibling::input[@type="checkbox"]'))
    )

    # Click on the checkbox
    checkbox.click()

    # Wait for the success message to appear
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'success'))
    )   

    # Print success message text
    print("Success message:", success_message.text)

except Exception as e:
    print("Exception occurred:", e)

finally:
    # Close the webdriver session
    driver.quit()
