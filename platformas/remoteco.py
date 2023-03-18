import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class Remote:
    
    MAIN_URL = "https://remote.co/remote-jobs/search/?search_keywords="

    
    def __init__(self):
        pass
    
    def return_url(self,work_name):
        return self.get_data(self.MAIN_URL + work_name)
    
    def get_data(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(2)
        links = driver.find_elements(By.CLASS_NAME,"stretched-link")
        return [i.get_attribute("href") for i in links]
        
remotebot = Remote()
# print(remotebot.get_data(remotebot.return_url("django")))