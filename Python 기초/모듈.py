# 모듈
    # 모듈 안에는 함수,클래스,변수 또는 실행 코드들이 정의될 수 있음.
    # 사용법 : import 모듈1[, 모듈2[,... 모듈N]

import math
n = math.factorial(5)

    # 하나의 함수만을 불러 사용
    # 호출시 "모듈명.함수명" 이 아니라 직접 "함수명"만 사용.
from math import factorial
n = factorial(5) / factorial(3)

    # 여러 함수를 import
from math import (factorial, acos)
n = factorial(3) + acos(1)

    # 모든 함수를 import
from math import *
n = sqrt(5) + fabs(-12.5)

    # factorial() 함수를 f()로 사용 가능
from math import factorial as f
n = f(5) / f(3)

# 모듈의 작성
    # 모듈 mylib.py가 있는 디렉토리에서 그 모듈을 import 후 mylib의 함수들을 사용
def add(a,b):
    return a + b
def substract(a,b):
    return a - b

    # exec.py
# from mylib import *

i = add(10,20)
i = substract(20,5)

    # run.py
import sys
def openurl(url):
    # ..본문생략
    print(url)
if __name__ == '__main__':
    openurl(sys.argv[1])

