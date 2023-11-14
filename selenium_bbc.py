import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

chrome_options = Options()
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome(options = chrome_options)
webpage = "https://www.bbc.com/news"

try:
    driver.get(webpage)
    headline_element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.XPATH, "//h3[@class='gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text']")) 
    ) 

    print(f"TOP HEADLINE: {headline_element.text}")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Current most watched: ")
    most_watched_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='nw-c-most-watched gs-t-news gs-u-box-size no-touch b-pw-1280']"))
    )
    #print(most_watched_element.get_attribute('outerHTML'))

    for i in range(5):
        data_entity_id = f"most-popular-watched#{i+1}"
        video_list_element = most_watched_element.find_element(By.XPATH, f"//li[@data-entityid='{data_entity_id}']")
        #print(video_list_element.get_attribute('outerHTML'))

        video_span_element = video_list_element.find_element(By.XPATH, f".//span[@class='gs-c-promo-heading__title gel-pica-bold']")
        #print(video_span_element.get_attribute('outerHTML'))

        title = video_span_element.text
        print(f"{i+1}) {title}")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Current most read: ")
    for i in range(10):
        list_element = driver.find_element(By.XPATH, f"//li[@data-entityid='most-popular-read-{i+1}']")
        #print(list_element.get_attribute('outerHTML'))
        span_element = list_element.find_element(By.CSS_SELECTOR, "span.gs-c-promo-heading__title.gel-pica-bold")
        title = span_element.text
        #print(span_element.get_attribute('outerHTML'))
        print(f"{i+1}) {title}")
except Exception as e:
    print(e)
finally:
    pid = driver.service.process.pid
    #os.system(f'taskkill /PID {pid} /F') # or else chrome processes will accumulate
    driver.quit()  



