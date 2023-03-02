import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class Remote:
    
    MAIN_URL = "https://remote.co/remote-jobs/search/?search_keywords="

    
    def __init__(self):
        pass
    
    def return_url(self,work_name):
        return self.MAIN_URL + "+".join(work_name.split(" "))
    
    def get_data(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(10)
        links = driver.find_elements(By.CLASS_NAME,"stretched-link")
        return [i.get_attribute("href") for i in links]
        
remotebot = Remote()
# print(remotebot.get_data(remotebot.return_url("django")))