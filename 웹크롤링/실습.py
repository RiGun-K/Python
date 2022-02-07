import os
import sys
import urllib.request
import datetime
import time
import json
client_id = ''           # 발급받은 ID 값 입력
client_secret = ''       # 발급받은 KEY 값 입력


# 터미널 상에서 원하는 검색어 입력하면 데이터 조회후 같은경로에서 JSON 파일(데이터 파일) 생성 
    # 1. 검색어 지정
    # 2. 네이버 뉴스 검색   ( getNaverSearch() , getRequestUrl() )
    # 3. 응답 데이터 정리 후 리스트에 저장 ( getPostData() )
    # 4. 리스트를 JSON 파일로 저장

#[CODE 1]
# API 접속 설정
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
    
#[CODE 2]
# 데이터 가져올 API 주소 설정
def getNaverSearch(node, srcText, start, display):  
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s"%(urllib.parse.quote(srcText), start, display)

    # url 구성
    url = base + node + parameters
    responseDecode = getRequestUrl(url) #[CODE 1]

    if (responseDecode == None):
        return None
    else:
        # 요청 결과를 JSON으로 받기 
        return json.loads(responseDecode)

#[CODE 3]
# 조회할 데이터 설정

# getPostData() - 응답 데이터를 정리하여 리스트에 저장하기
def getPostData(post, jsonResult, cnt):
    title = post['title']   # post 객체의 title 항목에 저장된 값
    description = post['description']   
    org_link = post['originallink']
    link = post['link']

    # 조회한 실시간 날짜 설정
    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')  # 문자열을 날짜 객체 형식으로 변환
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S') # 날짜 객체의 표시 형식을 지정

    # 리스트 객체인 jsonResult에 원소를 추가 
    jsonResult.append({'cnt':cnt, 'title':title, 'description':description, 'org_link':org_link, 'link':org_link, 'pDate':pDate})
    return

#[CODE 0]
# 터미널 상에서 조회후 JSON으로 파일 생성
def main():
    node = 'news' #크롤링할 대상
    srcText = input('조회할 검색어를 입력하세요: ') # 사용자 입력으로 받은 검색어 저장
    cnt = 0 # 검색 결과 카운트
    jsonResult = [] # 결과를 저장할 리스트 객체
    jsonResponse = getNaverSearch(node, srcText, 1, 100) # 1부터 100개의 검색 결과를 처리 [CODE 2] 
    total = jsonResponse['total']   # 전체 검색 결과수 = 네이버 뉴스 검색에 대한 응답을 저장하는 객체
    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1    # 1개 씩 증가 하도록
            getPostData(post, jsonResult, cnt) #[CODE 3]

        # getNaverSearch() 호출하여 새 결과를 저장하고 for 문 다시 반복
        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100) #[CODE 2]

    print('전체 검색 : %d 건' %total)

    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf8') as outfile:
        # jsonFile = JSON 파일에 저장할 데이터를 담은 객체
        jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True, ensure_ascii = False)
        # json.dumps() - 리스트를 JSON 파일로 저장하기
         
        outfile.write(jsonFile)

    print("가져온 데이터 : %d 건" %(cnt))   
    print('%s_naver_%s.json SAVED' % (srcText, node))

if __name__ == '__main__':
    main()


    
