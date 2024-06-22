from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = "riyamondaluser@gmail.com"
password = "1234riya@1234"
url = "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%3Fhl%3Den-GB&ec=GAlA8wE&hl=en-GB&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S-1643654106%3A1717439668924910&ddm=0"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

# Wait for the username field and enter the username
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "identifierId"))
).send_keys(username)

# Click on the 'Next' button
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "identifierNext"))
).click()

# Wait for the password field and enter the password
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "Passwd"))
).send_keys(password)

# Click on the 'Next' button
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "passwordNext"))
).click()

print("Login is successful")
