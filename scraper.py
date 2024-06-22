from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize an instance of the Chrome driver (browser)
driver = webdriver.Chrome()

try:
    # Visit your target site
    driver.get('https://github.com/')

    # Allow some time for the page to load
    time.sleep(3)

    # Find the "Sign up" button using XPath and click it
    signin_button = driver.find_element(By.XPATH, "//a[text()='Sign in']")
    signin_button.click()

    # Allow some time for the next page to load
    time.sleep(10)
finally:
    # Release the resources allocated by Selenium and shut down the browser
    driver.quit()
