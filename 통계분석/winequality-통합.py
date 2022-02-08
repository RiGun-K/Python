import pandas as pd

# red_df 와 while_df 파일 하나로 합치기

red_df = pd.read_csv('C:/Users/RiGun/Python/통계분석/winequality-red.csv', sep = ';', header=0, engine='python')
while_df = pd.read_csv('C:/Users/RiGun/Python/통계분석/winequality-white.csv', sep = ';', header=0, engine='python')

red_df.head()
red_df.insert(0, column='type', value='red')
red_df.head()
red_df.shape

while_df.head()
while_df.insert(0, column='type', value='white')
while_df.head()
while_df.shape

    # pd.concat() 사용
wine=pd.concat([red_df,while_df])
wine.shape
    # 새 파일로 저장
wine.to_csv('C:/Users/RiGun/Python/통계분석/wine.csv', index=False)

wine.columns = wine.columns.str.replace(' ','_')
wine.head()
    # describe() 를 통해 속성별 개수, 평균, 표준편차, 최소값, 전체 데이터 백분율(25%,50%,75%,최대값) 출력
print(wine.describe())

    # quality 속성값 중에서 유일한 값 출력
print(sorted(wine.quality.unique()))

    # quality 속성값에 대한 빈도수 측정
print(wine.quality.value_counts())

print(wine.groupby('type')['quality'].describe())
print(wine.groupby('type')['quality'].mean())
print(wine.groupby('type')['quality'].std())
print(wine.groupby('type')['quality'].agg(['mena','std']))