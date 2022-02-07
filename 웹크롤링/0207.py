# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 터미널 상에서 JSON 으로 데이터 출력하는 방법 

import os
import sys
import urllib.request
client_id = ""                  # 발급받은 ID 값 입력
client_secret = ""              # 발급받은 KEY 값 입력
encText = urllib.parse.quote("대통령 선거")     # 원하는 키워드 입력
url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    # news blogs cafearticle 로 변환가능 

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)