# 다차원 배열을 처리하는데 필요한 기능을 제공 (머신러닝, 데이터 분석 등)

# 터미널에 pip install matplotlib, numpy 등을 입력하여 설치를 해야한다. 
# 경로 C:\Users\RiGun\Python>

    # 배열의 n차원 크기를 rank
    # 크기를 튜플로 표시 shape
    # EX) 행이 2 열이 3 2차원 배열 = rank는 2 , shape는 (2,3)
import numpy as np

list1 = [1,2,3,4]
a = np.array(list1)
print(a.shape) # (4, )  = 하나의 요소만 있으면 뒤에 콤마

b = np.array([[1,2,3],[4,5,6]]) # 하나의 리스트만 들어가므로 리스트의 리스트를 추가
print(b.shape)  # (2, 3)
print(b[0,0])   # 1


    # zeros() - 해당 배열에 모두 0을 집어넣는다.
    # ones()  - 모두 1을 집어넣는다.
    # full()  - 사용자가 지정한 값을 넣음
    # eyes()  - 대각선으로 1 나머지 0인 2차원 배열 생성
 
a = np.zeros((2,2))
print(a)
# 출력:
# [[ 0.  0.]
#  [ 0.  0.]]
 
a = np.ones((2,3))
print(a)
# 출력:
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]
 
a = np.full((2,3), 5)
print(a)
# 출력:
# [[5 5 5]
#  [5 5 5]]
 
a = np.eye(3)
print(a)
# 출력:
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
 
a = np.array(range(20)).reshape((4,5))
print(a)
# 출력:
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]

    # numpy 슬라이싱
import numpy as np
 
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst)
 
# 슬라이스
a = arr[0:2, 0:2]
print(a)
# 출력:
# [[1 2]
#  [4 5]]
 
a = arr[1:, 1:]
print(a)
# 출력:
# [[5 6]
#  [8 9]]

    # 정수 인덱싱

lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
a = np.array(lst)
 
# 정수 인덱싱
s = a[[0, 2], [1, 3]]
 
print(s)
# 출력
# [2 12]

    # boolean 인덱싱
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)
 
bool_indexing_array = np.array([
    [False,  True, False],
    [True, False,  True],
    [False,  True, False]
])
 
n = a[bool_indexing_array];
print(n)   

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)
 
# 배열 a 에 대해 짝수면 True, 홀수면 False 
bool_indexing = (a % 2 == 0)
 
print(bool_indexing)
# 출력: 부울린 인덱싱 배열
# [[False  True False]
#  [ True False  True]
#  [False  True False]]
 
# 부울린 인덱스를 사용하여 True인 요소만 뽑아냄
print(a[bool_indexing])
# 출력:
# [2 4 6 8]
 
# 더 간단한 표현
n = a[ a % 2 == 0 ]
print(n)

    # numpy 연산
    
a = np.array([1,2,3])
b = np.array([4,5,6])
 
# 각 요소 더하기
c = a + b
# c = np.add(a, b)
print(c)  # [5 7 9]
 
# 각 요소 빼기
c = a - b
# c = np.subtract(a, b)
print(c)  # [-3 -3 -3]
 
# 각 요소 곱하기
# c = a * b
c = np.multiply(a, b)
print(c)  # [4 10 18]
 
# 각 요소 나누기
# c = a / b
c = np.divide(a, b)
print(c)  # [0.25 0.4 0.5]

    #
lst1 = [
    [1,2],
    [3,4]
]
 
lst2 = [
    [5,6],
    [7,8]
]
a = np.array(lst1)
b = np.array(lst2)
 
c = np.dot(a, b)
print(c)
# 출력:
# [[19 22]
#  [43 50]]

    #
a = np.array([[1,2],[3,4]])
 
s = np.sum(a)
print(s)   # 10
 
# axis=0 이면, 컬럼끼리 더함
# axis=1 이면, 행끼리 더함
s = np.sum(a, axis=0)
print(s)   # [4 6]
 
s = np.sum(a, axis=1)
print(s)   # [3 7]
 
s = np.prod(a)
print(s)   # 24