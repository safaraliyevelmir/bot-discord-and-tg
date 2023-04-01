from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


# Burada Indeedin kodları yazılıbdır
class Indeed:
    MAIN_URL = "https://www.indeed.com/jobs?q="
    
    def __init__(self):
        pass
    
    # Burada url geri qayıdır
    def return_url(self,work_name,location="Remote"):
        url = self.MAIN_URL + f"{work_name}&l={location}"
        return self.get_data(url)
    
    #get_data  dataları gətirir
    def get_data(self,url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
        driver.get(url)
        time.sleep(5)                        
        elements = driver.find_elements(By.XPATH,'/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a')
        return [i.get_attribute("href") for i in elements]

            
indeedbot = Indeed()
# print(indeedbot.get_data(indeedbot.return_url("django")))