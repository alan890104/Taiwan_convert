from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import urllib
import os
import pandas as pd
import IOT_GPS as GPS


addr_dict = {}

def loading():
    import random
    i=0
    while i<100:
        print(i,'%',end=' ')
        for j in range(i):
            print('#',end='')
        for j in range(i,100):
            print('-',end='')
        print('')
        time.sleep(random.uniform(0.02,0.07))
        os.system('cls')
        i+= random.randint(1,5)

def weather(location=None):

    if location==None:
        print('這不是在台灣喔!')
        return 0
    else:
        print('你所在的位置是 : ',location)
        location = location.split(',')
        location = location[1]+', '+location[0]

        if location not in addr_dict:
            try:
                url = 'https://weather.com/zh-TW/weather/today/l/TWXX0021:1:TW'
                options = Options()
                #options.add_argument("--headless")
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                driver = webdriver.Chrome(executable_path =r'C:\Users\alan8\test543\project\chromedriver.exe',options=options)
                driver.get(url)
                time.sleep(1)
                input_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="LocationSearch_input"]')))
                time.sleep(1)
                driver.execute_script("arguments[0].click();", input_box)
                time.sleep(1)
                input_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="LocationSearch_input"]')))
                time.sleep(1)
                input_box.send_keys(location)
                time.sleep(1)
                input_box.send_keys(Keys.ENTER)

                addr_dict[location] = driver.current_url
            except:
                pass
        else:
            try:
                url = addr_dict[location]
                options = Options()
                #options.add_argument("--headless")
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                driver = webdriver.Chrome(executable_path =r'C:\Users\alan8\test543\project\chromedriver.exe',options=options)
                driver.get(url)
            except:
                pass

        wind = driver.find_element_by_xpath('//*[@id="WxuTodayDetails-main-fd88de85-7aa1-455f-832a-eacb037c140a"]/section/div[2]/div[2]/div[2]/span')
        visible = driver.find_element_by_xpath('//*[@id="WxuTodayDetails-main-fd88de85-7aa1-455f-832a-eacb037c140a"]/section/div[2]/div[7]/div[2]/span')

        print('風速是',wind.text)
        print('能見度有',visible.text)

        w,v = wind.text,visible.text
        driver.quit()
        return float(w.split()[0]),float(v.split()[0])

        


if __name__ == '__main__':
    longitude = float(input('經度：'))
    latitude = float(input('緯度：'))
    #loading()
    weather(GPS.your_location(longitude,latitude))

    
