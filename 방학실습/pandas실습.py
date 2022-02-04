import pandas as pd
print(pd.__version__)

# Pandas => 데이터 분석에서 주로 사용하는 테이블 형태를 다룰 수 있는 라이브러리
# 1차원 자료구조 Series , 2차원 DataFrame , 3차원 Panel 

# 리스트를 이용하여 Series 생성
data1 = [10,20,30,40,50]

sr1 = pd.Series(data1)
sr2 = pd.Series(['월','화','수','목','금'])
print(sr1)
print(sr2)

# 인덱스를 지정하여 Series 생성
sr5 = pd.Series(data1, index = [1000,1001,1002,1003,1004])
print(sr5)

sr8 = pd.Series(data1, index = sr2)
print(sr8)

# Series 인덱싱
print(sr8[2])
print(sr8['수'])
print(sr8[-1])