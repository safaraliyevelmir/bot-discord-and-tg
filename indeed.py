from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Firefox()
#https://www.indeed.com/jobs?q=django&l=Remote&start=0
class Indeed:
    MAIN_URL = "https://www.indeed.com/jobs?q="
    
    def __init__(self):
        pass
    
    def return_url(self,work_name,location="Remote"):
        url = self.MAIN_URL + f"{work_name}&l={location}"
        self.get_data(url)
    
    def get_data(self,url):
        driver = webdriver.Firefox()
        driver.get(url)
        time.sleep(5)
        elements = driver.find_element(By.XPATH,'//*[@id="job_abbae8e96a294a15"]')
        print(elements.get_attribute("href"))
        # return [i.get_attribute("href") for i in elements]

            
indeedbot = Indeed()
indeedbot.return_url("django")
# indeedbot.get_data(url)