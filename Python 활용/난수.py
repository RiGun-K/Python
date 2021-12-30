# 난수
# random 모듈을 사용
    # randint(최소, 최대) : 입력 파라미터인 최소부터 최대까지 중 임의의 정수 리턴
    # random()            : 0 부터 1 사이의 부동소수점(float) 숫자를 리턴
    # uniform(최소, 최대) : 입력 파라미터인 최소부터 최대까지 중 임의의 부동소수점 리턴
    # randrange(시작,끝[,간격]) : 시작부터 끝값까지 숫자 중 임의의 수 리턴

from random import *

i = randint(1, 100)
print(i)

f = random()
print(f)

f = uniform(1.0, 36.5)
print(f)

i = randrange(1, 101, 2)
print(i)

i = randrange(10)
print(i)

    # 난수를 생성후 어떤 숫자인지 맞추는 프로그램
    # 사용자가 입력한 숫자가 난수보다 큰지 작은지를 알려주고 계속 추측하여 맞추게하는 예제
from random import randint

n = randint(1, 100)

while True:
    ans = input("Guess my number (Q to exit): ")
    if ans.upper() == "Q":  # 사용자가 Q를 입력한다면
        break
    ians = int(ans)
    if (n == ians):         # 난수와 사용자가 입력한 값이 같다면
        print("Correct!")
        break
    elif (n > ians):
        print("Choose higher number")
    else:
        print("Choose lower number")
        
# 샘플링(sample)
    # 리스트, set, 튜플 등과 같은 컬렉션으로부터 일부를 샘플링하여 뽑아내는 기능
    
import random

    # (1) 숫자리스트 샘플링
numlist = [1,2,3,4,5,6,7,8,9]
s = random.sample(numlist, 3)
print(s)    # [1, 2, 8]

    # (2) 튜플 샘플링
frutes = ('사과', '귤', '포도', '배')
s = random.sample(frutes, 2)
print(s)    # ['배', '사과']