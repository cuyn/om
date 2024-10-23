from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# User information
username = "tellonym_username"  # Replace with the user's Tellonym username
question = "hi baby i miss you"  # Replace with the question you want to ask

# Selenium setup
driver = webdriver.Chrome()  # Make sure to have the appropriate web driver installed

# Open Tellonym website
driver.get("https://tellonym.me/" + areiyn)

# Find the "Ask" button and click it
ask_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//button[text()="Ask"]'))
)
ask_button.click()

# Find the text area and enter the question
text_area = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
)
text_area.send_keys(question)

# Find the "Send" button and click it
send_button = driver.find_element(By.XPATH, '//button[text()="Send"]')
send_button.click()

# Close the browser
driver.quit()