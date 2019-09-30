from time import sleep
from bs4 import BeautifulSoup
from urllib.request import urlopen
import bs4
import selenium.webdriver as webdriver
import urllib
from datetime import datetime
import pandas as pd

#인스트 해시태그 검색어
search_text = "예술강사"
#search_text = "한국문화예술교육진흥원"
#search_text = "서울문화재단"

url="https://www.instagram.com/explore/tags/"+search_text   #search_text라는 변수를 생성하여 사용

#webdriver 옵션으로 크롤링되는 창을 숨기고 싶을경우 사용 현재 테스트 진행중이므로 테스트창 노출
#options = webdriver.ChromeOptions()
#options.headless = True
#options.add_argument('disable-gpu')

#driver 옵션을 적용한 chromedriver 사용
#driver = webdriver.Chrome(
#    executable_path="../../webdriver/chromedriver.exe", chrome_options=options
#)
driver = webdriver.Chrome(
    executable_path="../../webdriver/chromedriver.exe"
)

driver.get(url)
sleep(2)    #인스타 해시태그 검색 시 잠깐의 대기시간이 발생하여야 한다.
soup = BeautifulSoup(driver.page_source, "html.parser")     #호출된 페이지의 url에 담겨진 페이지의 태그를 beautifulsoup을 이용하여 soup함수에 담기
num = 0 #for문 반복값
urlList = []    #url 추가
result = [] #결과값 리스트
now = datetime.now()    #오늘날짜

for tag in soup.find_all("div",{"class":"v1Nh3"}): #div중 게시물과 관련된 div 추출
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")    #페이지 스크롤을 down하기 위함
    #sleep(2)
    for link in tag.find_all('a'): #a tag 의 주소만 추출
        if 'href' in link.attrs: #추출된 a tag 의 주소 href만 추출
            urlList.append(link.attrs['href'])  # urlList에 url실제주소 리스트로 담기

for cnt in range(len(driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']"))):     #담아온 갯수만큼 반복문을 사용
#for cnt in range(3):
    #driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']")[num].click()
    #url 추가
    #print(urlList[num])
    ###################
    url = "https://www.instagram.com"+urlList[num]  #실제 크롤링 되는 페이지의 주소
    driver.get(url)  # enter 치는것
    sleep(2)    #역시 마찬가지로 잠깐의 대기시간을 사용하기 위함
    html = urllib.request.urlopen(url)
    pageString = driver.page_source
    driver_obj = bs4.BeautifulSoup(pageString, "html.parser")   #실제 크롤링 되는 페이지의 소스담기
    driver_title = driver_obj.find("title") # title태그의 요소만 뽑아서 담기
    driver_id = driver_obj.find("a",{"class","FPmhX notranslate TlrDj"})    #a 태그의 class name으로 명확한 크롤링 대상을 검색
    #driver_text = driver_obj.find("div", {"class": "C4VMK"}).find_all("a", {"class": ""})
    driver_text = driver_obj.find("div", {"class": "C4VMK"}).find_all("a", {"class": ""})   #find와 find_all의 차이점은 단수, 복수의 차이점이 존재함(find_all로 호출 할 경우 리스트 형태로 표출)
    driver_date = driver_obj.find("div", {"class": "k_Q0X NnvRN"}).find("time", {"class": "_1o9PC Nzb55"})
    #driver_good = driver_obj.find("div",{"class": "Nm9Fw"}).find("span")    #좋아요 , 사진게시물일경우 좋아요
    #driver_cnt = driver_obj.find("span",{"class":"vcOH2"})  #조회수    동영상게시물일경우 조회수
    #print(driver_good.text)
    wmcymd = datetime.strptime(driver_date.get("datetime")[0:10], '%Y-%m-%d')   #게시물의 업로드 날짜를 DATE형식으로 형변환
    tag = ""    #해시태그 문자열을 담기위한 변수
    for i in driver_text:
        tag+=i.text+","     #크롤링된 해시태그의 구분자를 나타내기 위함
    result.append([urlList[num],tag,driver_id.text,wmcymd,driver_title.text,datetime.strftime(now,"%Y-%m-%d"),search_text])     #원하는 데이터의 형식으로 result변수에 리스트 형태로 담기
    num+=1      #모든 과정이 마치면 num+1증감
    sleep(1)
#driver.close()
#print(now.strftime('%Y%m%d'))
data = pd.DataFrame(result, columns=["URL","HASH","ID","DATE","CONTENT","UPDATE_DATE","SEARCH_TEXT"])   #DataFrame을 이용하여 엑셀데이터의 컬럼명을 추가(데이터의 컬럼의 수와 컬럼명의 수가 일치해야함)
excelWriter = pd.ExcelWriter(str(now.strftime('%Y%m%d'))+'_해시태그_'+search_text+'.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})     #엑셀데이터 export시 제목 설정
#excelWriter = pd.ExcelWriter('test해시태그_'+search_text+'.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})
#data.to_csv('해쉬태그.csv', encoding='utf-8')
data.to_excel(excelWriter)
excelWriter.close()
#data.to_json("hash.json",orient="table")