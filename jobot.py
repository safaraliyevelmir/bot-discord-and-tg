import requests
from bs4 import BeautifulSoup as bs

class JoBot:

    MAIN_URL = "https://jobot.com"
    def __init__(self):
        pass

    def return_url(self,work_name):
        return self.MAIN_URL + "/search?q=" + work_name + "&l=remote"
    
    def get_data(self,url):
        response = requests.get(url)
        soup = bs(response.content,"html.parser")
        links = soup.find_all("a","link")
        return [self.MAIN_URL+i['href'] for i in links]


jobot=JoBot()