import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/cookieclicker/')
timeout =60

# https://stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python
try:
    element_present = expected_conditions.presence_of_element_located((By.ID, 'langSelect-EN'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print('Timed out waiting for page to load.')

time.sleep(1)
lang_select_button_en = driver.find_element(By.ID, 'langSelect-EN')
lang_select_button_en.click()

try:
    element_present = expected_conditions.presence_of_element_located((By.ID, 'upgrades'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print('Timed out waiting for page to load.')

big_cookie = driver.find_element(By.ID, 'bigCookie')
# cursor = driver.find_element(By.ID, 'product0')
# grandma = driver.find_element(By.ID, 'product1')
# farm = driver.find_element(By.ID, 'product2')
# mine = driver.find_element(By.ID, 'product3')
# factory = driver.find_element(By.ID, 'product4')
# bank = driver.find_element(By.ID, 'product5')
# temple = driver.find_element(By.ID, 'product6')
# wizard_tower = driver.find_element(By.ID, 'product7')
# shipment = driver.find_element(By.ID, 'product8')
# alchemy_lab = driver.find_element(By.ID, 'product9')
# portal = driver.find_element(By.ID, 'product10')
# time_machine = driver.find_element(By.ID, 'product11')
# antim_condenser = driver.find_element(By.ID, 'product12')
# prism = driver.find_element(By.ID, 'product13')
# chancemaker = driver.find_element(By.ID, 'product14')
# fractal_engine = driver.find_element(By.ID, 'product15')
# javascript_console = driver.find_element(By.ID, 'product16')
# idleverse = driver.find_element(By.ID, 'product17')
# cortex_baker = driver.find_element(By.ID, 'product18')
# you = driver.find_element(By.ID, 'product19')


start_time = time.time()
running_time = start_time
timer = start_time
time_interval = 10
while running_time - start_time < 60 * 5:
    big_cookie.click()
    if running_time - timer >= time_interval:
        timer = running_time
        # try to click upgrade and products
        # upgrades = driver.find_elements(By.CSS_SELECTOR, '.crate.upgrade.enabled')
        # # store all the ids, because ids won't change, while elements can change
        # upgrade_ids = [upgrade.get_attribute('id') for upgrade in upgrades]
        # for upgrade_id in upgrade_ids[::-1]:
        #     while True:
        #         # use id to find the element, because it will change after clicking
        #         upgrade = driver.find_element(By.ID, upgrade_id)
        #         if not 'enabled' in upgrade.get_attribute('class'):
        #             break
        #         else:
        #             upgrade.click()
        products = driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')
        product_ids = [product.get_attribute('id') for product in products]
        for product_id in product_ids[::-1]:
            while True:
                product = driver.find_element(By.ID, product_id)
                if not 'enabled' in product.get_attribute('class'):
                    break
                else:
                    product.click()
    running_time = time.time()

        
