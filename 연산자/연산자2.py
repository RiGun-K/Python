# 파이썬 비교 , 논리연산자 예제

# 비교
a = 0
if a != 1:
    print("1이 아님.")
else:
    print("1입니다.")

# 논리
# and = 양쪽의 값이 모두 참일 경우 참
# or  = 한 쪽만 참이면 참
# not = 참이면 거짓 , 거짓이면 참 
x = True
y = False

if x and y:
    print("Yes")
else:
    print("No")

# Bitwise 연산자
# 이진수의 표현을 참 거짓으로 판별해 계산후 결과를 반환 
# 이미지 분석, 파일전송, 해시, 암호화 등에 사용, 특정 문자 위치추출 등 그 외 사용 X
a = 8       # 0000 1000 (8)
b = 5       # 0000 0101 (5)
c = a & b   # 0000 0000 (0)     = 같으면 1 다르면 0 , 0 끼리는 제외
d = a ^ b   # 0000 1101 (13)    = 다르면 1 같으면 0 
print(c)
print(d)

# 멤버 연산자
a = [1,2,3,4,5]
print(a)
b = 3 in a
print(b)    # True False 반환

print('3은 있다' if 3 in a else '3은 없다')
print('7은 없다' if 7 not in a else '7은 있다')

# 리스트 안의 데이터 반복문으로 찾기 
members = ['리건','병석','동민']
while True:
    name = input('찾는 조원의 이름을 입력하시오(Enter 종료)')
    if name=='':
        break
    print('조원' if name in members else '다른 조원', '입니다')


# Identity 연산자
# 양쪽 값들이 동일한 객체(자료형)인지 체크 ( 같은 메모리 주소를 가졌는가 ) , is 와 is not

a = 5
b = 5
print(a is b)       # True
print(a is not b)   # False

print(5 == 5.0)     # True   연산자는 단순히 값을 비교
print(5 is 5.0)     # False  객체의 주소가 다르므로 


