from time import sleep
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver

driver = webdriver.Chrome(
    executable_path="../webdriver/chromedriver.exe"
)
url="https://www.instagram.com/explore/tags/에버랜드"

driver.get(url)
sleep(3)
path=""
link2 = ""
soup = BeautifulSoup(driver.page_source, "html.parser")

def checkUrl():
    for tag in soup.find_all("div",{"class":"v1Nh3"}): #div중 게시물과 관련된 div 추출
        for link in tag.find_all('a'): #a tag 의 주소만 추출
            if 'href' in link.attrs: #추출된 a tag 의 주소 href만 추출
                return link.attrs['href']

count = driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']")
print(len(count))

for tap in driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']") :
    tap.click()
    #여기에서 건당 url 뽑기
    #print("1")
    #url = checkUrl()
    #print(url)
    sleep(1)
    driver.find_element_by_class_name('ckWGn').click()


#print(driver.find_element_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']"))
#print(soup)



