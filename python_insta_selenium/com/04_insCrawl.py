from time import sleep
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver


#url = "https://www.instagram.com/explore/tags/jmt/"

#options = webdriver.ChromeOptions()
#options.headless = True
#options.add_argument('disable-gpu')
#driver = webdriver.Chrome(
#    executable_path="../webdriver/chromedriver.exe", chrome_options=options
#)
driver = webdriver.Chrome(
    executable_path="../webdriver/chromedriver.exe"
)
url="https://www.instagram.com/explore/tags/댕댕이"

driver.get(url)
sleep(3)
#for num in range(1, 22 + 1):
#path = driver.find_element_by_class_name('v1Nh3')
#pathText = path.find("a").text
#print(pathText)
#for num in range(1, 1 + 1):
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#sleep(1)
soup = BeautifulSoup(driver.page_source, "html.parser")
#for tag in soup.find_all("div",{"class":"v1Nh3"}): #div중 게시물과 관련된 div 추출
#    for link in tag.find_all('a'): #a tag 의 주소만 추출
#        if 'href' in link.attrs: #추출된 a tag 의 주소 href만 추출
#            print(link.attrs['href'])
#            path = link.attrs['href']

#print(driver.find_element_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']"))

#sourcecode_elem = driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']")
#print(sourcecode_elem.__sizeof__())
#sourcecode_elem.click()

for tap in driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']") :
    tap.click()
#driver.find_element_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']").click()
    sleep(1)

#print(soup.find("div",{"class" : "eo2As"}))


    driver.find_element_by_class_name('ckWGn').click()


#count_tag = soup.find("span",{"class": "Nnq7C "})
#count_tag = soup.find("span",{"class": "g47SY"})
#totalCount = driver.find_elements_by_class_name('g47SY').text
#span_tag = soup.find("span",{"id":"react-root"})

#print(count_tag)
#print(totalCount)
#print(span_tag)

#driver.close()