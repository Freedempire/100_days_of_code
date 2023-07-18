# import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# it seems that no need for setting path
# chrome_driver_path = 'D:\\Study\\Programming\\Chromedriver\\chromedriver'
# os.environ['PATH'] += ';' + chrome_driver_path
# print(os.environ['PATH'])

driver = webdriver.Chrome()
driver.get('https://www.python.org/')
times = [time.get_attribute('datetime').split('T')[0] for time in driver.find_elements(By.CSS_SELECTOR, '.event-widget .shrubbery .menu time')]
event_names = [event_name.text for event_name in driver.find_elements(By.CSS_SELECTOR, '.event-widget .shrubbery .menu a')]
events = {}
for index in range(len(times)):
    # events.update({index: {'time': times[index], 'event name': event_names[index]}})
    events[index] = {'time': times[index], 'event name': event_names[index]}

print(events)