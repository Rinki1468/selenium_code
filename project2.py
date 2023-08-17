from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from pandas import ExcelWriter
from openpyxl import Workbook
import pymongo


driver=webdriver.Firefox(service=FirefoxService("C:/Users/firedriver/geckodriver.exe"))
urls=("https://www.insiderbiz.in/company-list/?page={}")
#driver.get(urls)

data=[]
#driver.get(urls)

    #col=WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
#col1=driver.find_elements(By.XPATH,'//*[@class="table"]/tbody/tr/td[1]')
#col2=driver.find_elements(By.XPATH,'//*[@class="table"]/tbody/tr/td[2]')
#col3=driver.find_elements(By.XPATH,'//*[@class="table"]/tbody/tr/td[3]')
#col4=driver.find_elements(By.XPATH,'//*[@class="table"]/tbody/tr/td[4]')

all_data=[]
for page in range(1,11):
    print('page',page)
    url=urls.format(page)
    r=driver.get(url)
    col1=driver.find_elements(By.XPATH,'//*[@class="table"]/tbody/tr/td[1]')
    col2=driver.find_elements(By.XPATH,'//*[@class="table"]/tbody/tr/td[2]')
    col3=driver.find_elements(By.XPATH,'//*[@class="table"]/tbody/tr/td[3]')
    col4=driver.find_elements(By.XPATH,'//*[@class="table"]/tbody/tr/td[4]')
    for i in range(len(col2)):
        data={'cin':col1[i].text,
            'company':col2[i].text,
            'ROC':col3[i].text,
            'address':col4[i].text}
        all_data.append(data)
        print(all_data)
#df=pd.DataFrame(all_data)
#df.to_excel('project_final_assinment.xlsx',index=False)    


client=pymongo.MongoClient("mongodb://localhost:27017")
print(client)
db=client['first_selenium']
collection=db['project_assingment_final']
collection.insert_many(all_data)    
    