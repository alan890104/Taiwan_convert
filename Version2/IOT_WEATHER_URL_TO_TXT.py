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

def weather(location=None):

    read_txt_name = 'dict.txt'
    write_txt_name = 'url_dictionary.txt'

    f = open(read_txt_name,"r")
    g = open(write_txt_name,'w')

    for location in f.readlines():
        if '臺中市' in location: 
            location.replace('臺中市','臺中縣')
        print('location : ',location)

        if location==None:
            print('None')
        else:

            
                try:
                    url = 'https://weather.com/zh-TW/weather/today/l/TWXX0021:1:TW'
                    options = Options()
                    options.add_argument("--headless")
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
                    time.sleep(2)
                    input_box.send_keys(Keys.ENTER)
                    time.sleep(1)
                    g.write(location+' '+str(driver.current_url)+'\n')
                    print(driver.current_url)
                    time.sleep(1)
                    driver.quit()
                except:
                    pass
        
        


if __name__ == '__main__':
    weather()

    
