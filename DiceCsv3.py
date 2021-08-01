import datetime
import time
import pandas as pd
from selenium import webdriver
from datetime import datetime

start_time = time.time()
#current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(dt_string)

#Headless Browser
chrome_option = webdriver.ChromeOptions()
chrome_option.headless = True
DRIVER_PATH = '/Users/shivapriya/chromedriver/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=chrome_option)

driver.get('https://www.dice.com/')
#driver.maximize_window()
driver.set_window_size(1440, 900)
# selecting sdet in job serach
driver.find_element_by_xpath('//*[@id="typeaheadInput"]').send_keys("SDET")

# click on search button
driver.find_element_by_xpath('//*[@id="submitSearch-button"]').click()
time.sleep(5)

# select 'Today' option
driver.find_element_by_xpath(
    '//*[@class="btn-group-vertical w-100 ng-star-inserted"]/button[2]').click()

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(5)
# select 100
select_values = driver.find_element_by_xpath('//*[@id="pageSize_2"]/option[4]').click()
time.sleep(5)


thisdict = {}
t = 0

def getdata(counter1):
    global t
    global dt_string
    for i in range(0, counter1-1):
        driver.find_elements_by_css_selector(".card-title-link.bold").__getitem__(int(i)).click()
        driver.implicitly_wait(5)
        d1 = driver.find_element_by_xpath("//*[@id='jt']").text
        d2 = driver.find_elements_by_css_selector(".iconsiblings").__getitem__(1).text
        d3 = driver.find_element_by_css_selector(".employer.hiringOrganization").text
        d3 = d3.replace(',', '')
        d4 = driver.find_element_by_css_selector(".location").text
        d5 = driver.find_element_by_xpath("//*[@class='company-header-info']//div[contains(text(),'ago')]").text
        d6 = driver.find_element_by_id("jobdescSec").text
        d7 = driver.find_element_by_xpath("//*[@class='company-header-info']//div[contains(text(),'Position')]").text
        d7 = d7.replace('Position id:','')
        d8 = driver.find_element_by_xpath("//*[@name='jobsUrl']").get_attribute("content")
        d9 = dt_string
        print("Job Title:",d1)
        print("Company name:", i,d3)

        thisdict[t] = {"Job Category": d2,
                       "Searched Job Title": "SDET",
                       "Searched Job Location": d4,
                       "Job Portal": "Dice",
                       "Job Date Posted": d5,
                       "Job Title": d1,
                       "Job Company Name": d3,
                       "Job Location": d4,
                       "Job Link": d8,
                       "Job Description": d6,
                       "Position id": d7,
                       "Date Time Scrapped": d9
                       }

        driver.execute_script("window.history.go(-1)")
        driver.implicitly_wait(5)
        t = t + 1

number_of_pages = driver.find_element_by_xpath("//a[contains(text(),'»')]/preceding::a[1]").text
print(number_of_pages)

# for 1st page
counter1 = len(driver.find_elements_by_css_selector(".card-title-link.bold"))
print("Page1: ")
print(counter1)
#counter1 = 2
getdata(counter1)
print("Done page")

# for 2nd page onwards
for j in range(1, int(number_of_pages)):
    print("Page: ")
    print(int(j + 1))
    driver.find_element_by_xpath("//a[contains(text(),'»')]").click()
    time.sleep(5)
    counter1 = len(driver.find_elements_by_css_selector(".card-title-link.bold"))
    print(counter1)
    #counter1 = 2
    getdata(counter1)
    print("Done page")

df = pd.DataFrame.from_dict(thisdict, orient="index", columns=['Job Title','Job Category','Job Company Name',
                                                             'Job Location','Job Date Posted','Job Description',
                                                             'Position id','Job Link','Date Time Scrapped'])

print(df)
df.to_csv("DiceCsv3_test6.csv", index=False)
# driver.close()
end_time = time.time()
print(end_time - start_time)
