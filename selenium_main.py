###                                                             ###
###     MOST OF THE DATA HAVE BEEN DELETED FOR AUTHENTICITY     ###
###                                                             ###

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options


firefox_options = Options()
firefox_service = FirefoxService('geckodriver.exe') 
driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

cookies = [
    {}
    ]

url = ""
driver.get(url)


for cookie in cookies:
    driver.add_cookie(cookie)

driver.get(url)
time.sleep(20)  

rows = driver.find_elements(By.CSS_SELECTOR, '.ds-dex-table') 

data = []
print(f"Found {len(rows)} rows.")
for row in rows:
    for index in range(2,102):
        try:
            pair_name = row.find_element(By.CSS_SELECTOR, f'a.ds-dex-table-row:nth-child({index}) > div:nth-child(1) > span:nth-child(4)').text  
            price = row.find_element(By.CSS_SELECTOR, f'a.ds-dex-table-row:nth-child({index}) > div:nth-child(2)').text  
            volume_24h = row.find_element(By.CSS_SELECTOR, f'a.ds-dex-table-row:nth-child({index}) > div:nth-child(3)').text  
        
            data.append({
                'Pair': pair_name,
                'Price': price,
                '24h Volume': volume_24h
            })
        except Exception as e:
            print(f"Error scraping row: {e}")

html = driver.page_source

with open("page_source.html", "w", encoding="utf-8") as file:
    file.write(html)

print("HTML page source saved to 'page_source.html'.")

df = pd.DataFrame(data)

print(df)
df.to_csv('data.csv', index=False)

driver.quit()

print("Scraping completed and data saved to data.csv.")

