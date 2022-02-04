import matplotlib
# pyplot 모듈 import
import matplotlib.pyplot as plt 
print(matplotlib.__version__)

# 데이터 준비
x = [2016,2017,2018,2019,2020]
y = [350,410,520,695,543]

# x축과 y축 데이터를 지정하여 라인플롯 생성
plt.plot(x, y)

# 차트 제목 설정
plt.title('Annual sales')

# x축 y축 레이블 설정
plt.xlabel('years')
plt.ylabel('sales')

# 라인플롯 표시 
plt.show()
