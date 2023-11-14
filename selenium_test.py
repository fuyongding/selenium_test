from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

chrome_options = Options()
chrome_options.add_argument('start-maximized')

company_ticker = input("Enter the company ticker symbol: ").upper()
if company_ticker != '':
    driver = webdriver.Chrome(options = chrome_options)
    webpage = f"https://sg.finance.yahoo.com/quote/{company_ticker}"
    driver.get(webpage)

    #driver.implicitly_wait(2)

    try:
        stock_price_node = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.XPATH, f'//fin-streamer[@data-symbol="{company_ticker}"][@data-field="regularMarketPrice"]')) 
        )
        #stock_price_node = driver.find_element(By.XPATH, f'//fin-streamer[@data-symbol="{company_ticker}"][@data-field="regularMarketPrice"]')
        stock_price = stock_price_node.get_attribute('innerText').strip()

        currency_node = driver.find_element(By.XPATH, "//span[contains(text(), 'Currency in')]") # Find the span element that contains the text "Currency in"
        #print(currency_node.get_attribute('outerHTML'))
        currency_text = currency_node.text
        currency = currency_text.split()[-1]

        print(f'The current price of {company_ticker} is: {stock_price} {currency}')

        driver.save_screenshot(f'images/wholescreen_{company_ticker}.png') # Take a screenshot of the entire page

        canvas_element = driver.find_element(By.XPATH, '//canvas[@role="img"]') 
        canvas_element.screenshot(f'images/canvas_{company_ticker}.png') # take ss of canvas chart

        chart_link_node = driver.find_element(By.XPATH, "//li[@data-test='CHART']")
        chart_link_node.click() # Click the element

        driver.implicitly_wait(5)   

        chart_element = driver.find_element(By.XPATH, "//div[contains(@id, 'Lead-7-Chart-Proxy')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", chart_element)
        chart_element.screenshot(f'images/chart_{company_ticker}.png')
    except NoSuchElementException:
        print(f'Stock price of {company_ticker} could not be found on YAHOO finance')
    finally:
        driver.quit()
else:
    print("INPUT SOMETHING YOU DUMBASS")