import numpy as np

# 초기값과 구조를 지정하여 numpy 생성
ar5 = np.zeros((2,3))
print(ar5)

# numpy 슬라이싱
ar2 = ar2 = np.array([[10,20,30],[40,50,60]])
ar6 = ar2[0:2, 0:2]
print(ar6)

ar7 = ar2[0, :]
print(ar7)

# numpy 사칙연산
ar1 = np.array([1,2,3,4,5])
ar8 = ar1 + 10
print(ar8)
print(ar1 + ar8)
print(ar8 - ar1)
print(ar1 * 2)
print(ar1 / 2)

# numpy 행렬곱 연산
ar4 = np.array([1,2,3,4,5,6]).reshape((3,2))
ar9 = np.dot(ar2, ar4)
print(ar9)