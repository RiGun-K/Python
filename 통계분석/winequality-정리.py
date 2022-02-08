import pandas as pd

# (;) 를 열 구분자로 사용하여 .csv 파일을 새로 생성

    # 파일을 읽어 온 후 (;) 으로 구분
red_df = pd.read_csv('C:/Users/RiGun/Python/통계분석/winequality-red.csv', sep = ';', header=0, engine='python')
while_df = pd.read_csv('C:/Users/RiGun/Python/통계분석/winequality-white.csv', sep = ';', header=0, engine='python')

    # 구분한 파일을 새 파일로 저장
red_df.to_csv('C:/Users/RiGun/Python/통계분석/winequality-red2.csv', index = False)
while_df.to_csv('C:/Users/RiGun/Python/통계분석/winequality-white2.csv', index = False)