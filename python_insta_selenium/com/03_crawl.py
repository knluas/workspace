import urllib
from time import sleep
import datetime
from urllib.request import urlopen
import bs4
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="../webdriver/chromedriver.exe"
)
url="https://www.instagram.com/p/B1fsnySpBXE/"
driver.get(url) #enter 치는것
sleep(2)
html = urllib.request.urlopen(url)
pageString = driver.page_source
driver_obj = bs4.BeautifulSoup(pageString,"html.parser")

#driver_obj1 = driver_obj.find("div",{"class":"C4VMK"})
#driver_date = driver_obj1.find("time",{"class":"FH9sR Nzb55"})
driver_text = driver_obj.find("div",{"class":"C4VMK"}).find_all("a",{"class":""})
driver_date = driver_obj.find("div",{"class":"k_Q0X NnvRN"}).find("time",{"class":"_1o9PC Nzb55"})

for i in driver_text:
    print(i.text)
print(datetime.datetime.strptime(driver_date.get("datetime")[0:10], '%Y-%m-%d'))
#bs_obj = bs4.BeautifulSoup(html,"html.parser")
#driver.find_element_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']").click()
sleep(1)
#con = bs_obj.find("body",{"class":""})
#print(bs_obj)
#print(con)
#for m in con.finditer('meta',{"property":"instapp:hashtags"}):
#         print('ll found', m)
#print(con.find("meta",{"property":"instapp:hashtags"}))





#con1 = bs_obj.find("span",{"id":"react-root"})
#con2 = con1.find("section",{"class":"_9eogI E3X2T"})
#print(con1)
#print(con2)
#print(con)
#print(bs_obj)



#인스타 껍데기
#인스타 내용 Nnq7C aaa

#driver.close()