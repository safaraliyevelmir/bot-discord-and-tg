from bs4 import BeautifulSoup as bs
import requests



class DjinniBot:
    MAIN_URL = "https://djinni.co"
    
    def __init__(self):
        pass

    def job_features(self,work_name,experience=None,salary=None):
        url = DjinniBot.MAIN_URL + "/jobs/?keywords="+work_name
        if salary:
            url += f"&salary={salary}"
        
        if experience:
            url += f"&exp_level={experience}y"
        
        return self.find_job(url+'&page=')
        
    def find_job(self,url):
        
        count=1
        # response = requests.get(url+str(count))
        # soup = bs(response.content,"html.parser")
        # pag = soup.find_all("a",class_='page-link')
        # number = [i.text for i in pag][-2]
        # print(number)
        # while count<=int(number):       
        response = requests.get(url+str(count))

        soup = bs(response.content,"html.parser")
        # pag = soup.find_all("a",class_='page-link')
        jobs = soup.find_all('a',class_='profile')
        job = [self.MAIN_URL + i['href'] for i in jobs ][:5]
        # count+=1
        return job
djinni = DjinniBot()
