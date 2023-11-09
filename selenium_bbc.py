import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('start-maximized')
#chrome_options.add_argument('--no-sandbox') 

driver = webdriver.Chrome(options = chrome_options)
webpage = "https://www.bbc.com/news"

try:
    driver.get(webpage)
    driver.implicitly_wait(5)

    # Use the XPath to find the title of headline
    headline_element = driver.find_element(By.XPATH, "//h3[@class='gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text']")
    print(f"TOP HEADLINE: {headline_element.text}")

    print("\n-----------------------------------------------------------------------------------------------------------------\n")

    print("Current most read: ")
    for i in range(10):
        list_element = driver.find_element(By.XPATH, f"//li[@data-entityid='most-popular-read-{i+1}']")
        #print(list_element.get_attribute('outerHTML'))

        span_element = list_element.find_element(By.CSS_SELECTOR, "span.gs-c-promo-heading__title.gel-pica-bold")
        title = span_element.text
        #print(span_element.get_attribute('outerHTML'))
        print(f"{i+1}) {title}")
    
    print("\n-----------------------------------------------------------------------------------------------------------------\n")
except Exception as e:
    print(e)
finally:
    pid = driver.service.process.pid
    #os.system(f'taskkill /PID {pid} /F') # or else chrome processes will accumulate
    driver.quit()  



