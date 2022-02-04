from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

# print(bsObject) # 웹 문서 전체출력 
print(bsObject.head.title)  # 태그로 구성된 트리에서 title 태그만 출력