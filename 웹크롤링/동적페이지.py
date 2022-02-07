from selenium import webdriver

# 다운받은 파일을 불러와 크롬 WebDriver 객체를 생성
wd = webdriver.Chrome('C:/Users/RiGun/Python/WebDriver/chromedriver.exe')

wd.get("http://www.hanbit.co.kr")

# 동적페이지는 vscode로 안됨 Shell 로만 가능 
