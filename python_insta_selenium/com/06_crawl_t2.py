from time import sleep
from bs4 import BeautifulSoup
from urllib.request import urlopen
import bs4
import selenium.webdriver as webdriver
import urllib
import datetime
import pandas as pd

driver = webdriver.Chrome(
    executable_path="../webdriver/chromedriver.exe"
)
url="https://www.instagram.com/explore/tags/예술강사"

driver.get(url)
sleep(2)
soup = BeautifulSoup(driver.page_source, "html.parser")
num = 0 #for문 반복값
urlList = []    #url 추가
result = []     #결과값 리스트
for tag in soup.find_all("div",{"class":"v1Nh3"}): #div중 게시물과 관련된 div 추출
    for link in tag.find_all('a'): #a tag 의 주소만 추출
        if 'href' in link.attrs: #추출된 a tag 의 주소 href만 추출
            urlList.append(link.attrs['href'])

for cnt in range(len(driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']"))):
#for cnt in range(3):
    driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']")[num].click()
    #url 추가
    #print(urlList[num])
    ###################
    url = "https://www.instagram.com"+urlList[num]
    #driver.get(url)  # enter 치는것
    sleep(2)
    html = urllib.request.urlopen(url)
    pageString = driver.page_source
    driver_obj = bs4.BeautifulSoup(pageString, "html.parser")
    driver_text = driver_obj.find("div", {"class": "C4VMK"}).find_all("a", {"class": ""})
    driver_date = driver_obj.find("div", {"class": "k_Q0X NnvRN"}).find("time", {"class": "_1o9PC Nzb55"})
    wmcymd = datetime.datetime.strptime(driver_date.get("datetime")[0:10], '%Y-%m-%d')

    for i in driver_text:
        #word.append(i.text)   #최종 해쉬태그 리스트로 append
        #date.append(wmcymd)
        if(i != ""):
            result.append([i.text.strip(' '),wmcymd])
    #result.append(temp) #2단 배열을 만들기위함
    #print(result)
    ########################
    num+=1
    sleep(1)
    driver.find_element_by_class_name('ckWGn').click()

data = pd.DataFrame(result)
data.to_csv('해쉬태그.csv', encoding='utf-8')