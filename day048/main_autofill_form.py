from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element(By.NAME, 'fName')
last_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
submit_button = driver.find_element(By.TAG_NAME, 'button')

first_name.send_keys('tony')
last_name.send_keys('chi')
email.send_keys('tony@gmail.com')
# submit_button.send_keys(Keys.ENTER)
submit_button.click()