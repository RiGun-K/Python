# 데이터를 차트나 플롯으로 그려주는 데이터 시각화 패키지
# 과학용 파이썬 '아나콘다'를 설치해서 Jupyter Notebook을 사용하면 편리함.

from matplotlib import pyplot as plt

plt.plot([1,2,3,], [110,130,120])
plt.show()

    # 제목과 축 레이블

plt.plot(["Seoul", "Paris", "Seattle"], [30,25,55])
plt.xlabel('City')
plt.ylabel('Response')
plt.title('Experiment Result')
plt.show()

    # 범례 추가
    
plt.plot([1,2,3], [1,4,9])
plt.plot([2,3,4],[5,6,7])
plt.xlabel('Sequence')
plt.ylabel('Time(secs)')
plt.title('Experiment Result')
plt.legend(['Mouse', 'Cat'])
plt.show()

    # 다양한 차트 및 플롯

y = [5, 3, 7, 10, 9, 5 ,3.5, 8]
x = range(len(y))
plt.bar(x, y, width=0.7, color="blue")
plt.show()
