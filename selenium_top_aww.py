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
webpage = "https://www.reddit.com/r/aww/top"
#webpage = "https://www.reddit.com/r/singapore/top/"
#webpage = "https://www.reddit.com/r/news/top/"

try:
    driver.get(webpage)
    #driver.implicitly_wait(100)

    top_post = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.XPATH, "/html/body/shreddit-app/div/div[1]/div[2]/main/div[2]/shreddit-post[1]/a")) 
    ) 
 
    #top_post = driver.find_element(By.XPATH, "/html/body/shreddit-app/div/div[1]/div[2]/main/div[2]/shreddit-post[1]/a")
    top_post.screenshot(f'images/top_post.png')
except Exception as e:
    print(e)
finally:
    driver.quit()  



