from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# driver = webdriver.Firefox()
#https://www.indeed.com/jobs?q=django&l=Remote&start=0
class Indeed:
    MAIN_URL = "https://www.indeed.com/jobs?q="
    
    def __init__(self):
        pass
    
    def return_url(self,work_name,location="Remote"):
        url = self.MAIN_URL + f"{work_name}&l={location}"
        return self.get_data(url)

    def get_data(self,url):
        driver_options = webdriver.ChromeOptions()
        driver_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        driver_options.add_argument("--headless")
        driver_options.add_argument("--disable-dev-shm-usage")
        driver_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=driver_options)

        driver.get(url)
        time.sleep(5)                        
        elements = driver.find_elements(By.XPATH,'/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a')
        return [i.get_attribute("href") for i in elements]

            
indeedbot = Indeed()
# print(indeedbot.get_data(indeedbot.return_url("django")))