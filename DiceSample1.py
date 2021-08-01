import datetime
import time
from dateutil.parser import parse
import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = 'C:\Tim_software\SeleniumDriver\chromedriver_win32\chromedriver.exe'
driver: WebDriver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.dice.com/')
driver.maximize_window()

# selecting sdet in job serach
driver.find_element_by_xpath('//*[@id="typeaheadInput"]').send_keys("SDET")
# click on search button
driver.find_element_by_xpath('//*[@id="submitSearch-button"]').click()
time.sleep(5)
# select 'Today' option
driver.find_element_by_xpath(
    '//*[@id="facets"]/dhi-accordion[2]/div[2]/div/js-single-select-filter/div/div/button[2]').click()
# Scroll to the bottom of the page
# select 100
driver.find_element_by_xpath('//*[@id="pageSize_2"]/option[4]').click()
time.sleep(5)

counter1 = len(driver.find_elements_by_css_selector(".card-title-link.bold"))
print(counter1)

#remove the next line for all the records
counter1 = 6

for i in range(0, counter1):
    driver.find_elements_by_css_selector(".card-title-link.bold").__getitem__(int(i)).click()
    time.sleep(5)
    data = driver.find_elements_by_xpath("//*[@class='container job-details']")
    for j in data:
        datas = j.text
    print("Data for record: " + str(i))
    print(datas)
    driver.execute_script("window.history.go(-1)")
    time.sleep(6)


driver.close()