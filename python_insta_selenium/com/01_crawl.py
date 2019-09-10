from libs.crawler import crawl

url = "https://www.instagram.com/explore/tags/발레"

pageString = crawl(url)
print(pageString)
