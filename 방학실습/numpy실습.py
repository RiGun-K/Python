import numpy as np
print(np.__version__)

# 리스트를 이용하여 numpy 생성 np.array()
ar1 = np.array([1,2,3,4,5])
print(ar1)
print(type(ar1))

ar2 = np.array([[10,20,30],[40,50,60]])
print(ar2)

# 값의 범위를 지정하여 numpy 생성 np.arange(시작값, 끝값, 간격)
ar3 = np.arange(1, 11, 2)
print(ar3)

# 구조를 지정하여 numpy 생성 np.array().reshape()
ar4 = np.array([1,2,3,4,5,6]).reshape((3,2))
print(ar4)

