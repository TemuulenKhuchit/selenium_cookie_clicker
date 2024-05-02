from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

# Chrome options to start maximized
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--start-maximized")  # Start Chrome maximized

# Keep Chrome browser open after program finishes
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Find the <input> by Name
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

# Sending keyboard input to Selenium
first_name.send_keys("Temuulen")
last_name.send_keys("Khuchit")
email.send_keys("TemuulenKhuchit01@gmail.com")

# Location the "Sign Up" button. Then click on it.
submit = driver.find_element(By.CSS_SELECTOR, "button")
submit.click()

# driver.close()
# driver.quit()
