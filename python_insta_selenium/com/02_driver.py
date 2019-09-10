from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="../webdriver/chromedriver.exe"
)

url="https://www.instagram.com/explore/tags/발레/?hl=ko"
driver.get(url)
#driver.close()
