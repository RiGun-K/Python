import requests
from bs4 import BeautifulSoup

# html 문서를 탐색해서 원하는 부분만 뽑아낼 수 있는 라이브러리 

webpage = requests.get("https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=2&sido=&gugun=&store=")
soup = BeautifulSoup(webpage.content, "html.parser")

# print(soup.text) - 전체 html 출력
print(soup.a.string) # 첫번째 a태그의 텍스트만 출력




