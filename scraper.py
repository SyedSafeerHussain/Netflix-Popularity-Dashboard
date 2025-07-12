from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os
import requests
from bs4 import BeautifulSoup
from utils.helpers import save_to_csv

# Create data directory if doesn't exist
"""
DATA_DIR=os.path.join(os.path.dirname(os.path.dirname(__file__)),'data')
os.makedirs(DATA_DIR,exist_ok=True)"""

driver=webdriver.Chrome()

url="https://www.netflix.com/tudum/top10/most-popular/"
driver.get(url)
time.sleep(2)

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='list-start']/div"))
)
"""def scrape(file_name):
    board=driver.find_element(By.XPATH,"//*[@id='appMountPoint']/div/div/div[1]/div/div[2]/section[4]/div/div[2]/table/tbody[1]")
    rows=board.find_elements(By.XPATH,"./tr")
    with open(file_name,'w')as file:
        writer=csv.writer(file)
        writer.writerow(['Name','Views','Run_Time','Hours_Viewed'])
        for row in rows:
            try:
                name=row.find_element(By.XPATH,"./td/button").text
            except:
                name='N/A'
            try:
                views=row.find_element(By.XPATH,"./td[2]").text
            except:
                views='N/A'
            try:
                run_time=row.find_element(By.XPATH,"./td[3]").text
            except:
                run_time='N/A'
            try:
                Hours_Viewed=row.find_element(By.XPATH,"./td[4]").text
            except:
                Hours_Viewed='N/A'
            writer.writerow([name,views,run_time,Hours_Viewed])
            

"""
def scrape(file_name):
    data=[]
    board=driver.find_element(By.XPATH,"//*[@id='appMountPoint']/div/div/div[1]/div/div[2]/section[4]/div/div[2]/table/tbody[1]")
    rows=board.find_elements(By.XPATH,"./tr")
    for row in rows:
        try:
            name=row.find_element(By.XPATH,"./td/button").text
        except:
            name='N/A'
        try:
            views=row.find_element(By.XPATH,"./td[2]").text
        except:
            views='N/A'
        try:
            run_time=row.find_element(By.XPATH,"./td[3]").text
        except:
            run_time='N/A'
        try:
            Hours_Viewed=row.find_element(By.XPATH,"./td[4]").text
        except:
            Hours_Viewed='N/A'
        data.append({
            'name':name,
            'views':views,
            'run_time':run_time,
            'hours_viewed':Hours_Viewed
        })
    try:
        save_to_csv(data,file_name)
        print(f"✅ Scraping complete and saved to data/{file_name}")
    except Exception as e:
        print("❌ Failed to save CSV: %s", str(e))
def open_dropdown():
    try:
        key=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@id=':r8:']"))
    )
        key.click()
        time.sleep(2)
        print("drop_down opened")
    except Exception as e:
        print(f"lora {str(e)}")

def category1():
    try:
        option=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@id=':ra:-1']"))
    )
        option.click()
        print("Selected option")
    except Exception as e:
        print("not selected")



def category2():
    try:
        option=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@id=':ra:-2']"))
    )
        option.click()
        print("Selected option")
    except Exception as e:
        print("not selected")




def category3():
    try:
        option=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@id=':ra:-3']"))
    )
        option.click()
        print("Selected option")
    except Exception as e:
        print("not selected")



scrape('english_movies.csv')

open_dropdown()
category1()
scrape('non_english_movies.csv')
open_dropdown()
category2()
scrape('english_series.csv')
open_dropdown()
category3()
scrape('non_english_series.csv')

driver.quit()






























        