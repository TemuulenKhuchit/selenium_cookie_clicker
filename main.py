import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome options to start maximized
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Start Chrome maximized

# Keep Chrome browser open after program finishes
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

click_qty = 0
cookie = driver.find_element(By.ID, "cookie")
check_upgrade_timer = time.time()
game_over_timer = time.time() + 60 * 5


def check_upgrade() -> bool:
    global check_upgrade_timer
    if check_upgrade_timer <= time.time():
        check_upgrade_timer = time.time() + 5
        return True
    return False


def buy_item():
    store = driver.find_element(By.ID, "store")
    items = store.find_elements(By.CSS_SELECTOR, '[class=""]')
    if items:
        need_to_buy = items[-1]
        need_to_buy.click()


while game_over_timer > time.time():
    cookie.click()
    click_qty += 1
    if check_upgrade():
        buy_item()

cookies_second = driver.find_element(By.ID, "cps").text

print(f"Click count is: {click_qty}")
print(cookies_second)


# driver.close()
driver.quit()