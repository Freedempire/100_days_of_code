
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

google_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfMqCZAej0LU8gEITHZDKlMZBHp0rmFBMqk9mJ2N21fg62eGw/viewform?usp=sf_link'
zillow_url = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.43509511621416%2C%22east%22%3A-122.25313405664384%2C%22south%22%3A37.74192852027262%2C%22north%22%3A37.88351126976244%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A588263%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
timeout = 60

driver = webdriver.Chrome()
driver.get(zillow_url)

try:
    element_present = expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, '#grid-search-results ul'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutError:
    print('Timed out waiting for page to load.')

result_list_per_page = driver.find_elements(By.CSS_SELECTOR, '#grid-search-results ul li')
print(len(result_list_per_page))
for item in result_list_per_page:
    if item.get_attribute('data-test'):
        continue
    address = item.find_element(By.TAG_NAME, 'address').text
    print(address)

