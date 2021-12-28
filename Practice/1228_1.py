print(5 ** 2)   # 제곱 **
print(5 % 2)    # 나머지    
print(5 // 2)   # 나누기에 소숫점 이하 삭제

# 코맨드 처리
# 콜론(:) = if for def문 끝에서 항상
# 들여쓰기 = 클론 내부 코딩블럭은 동일한 들여쓰기를 사용

# 할당 연산자
a = 4   # 오른쪽 값을 왼쪽 변수에 할당
b = 3
c = 2
print(a,b,c)

a += b  # a = a+b 
print(a,b)

a -= b  # a = a-b
print(a,b)

c *= 10 # c = c * 10
print("C의 값은" + str(c))  # !!! 중요 !!!
# 파이썬은 숫자와 문자를 합칠 수 없다 하나로 묶어야 함 !!
# numo = 10 stro = "10" 
# print(str(numo) + "입니다")   # 문자로 바꿔 합치기
# print(int(stro) + 20)         # 숫자로 바꿔 합치기 

a *= b  # a = a*b
print(a,b)

print(type(a)) # 변수 a의 type 표시

a **= b # a = a**b (12의 3제곱)
print(a,b)


if a != 1:
    print("1이 아님.")
else:
    print("1입니다.")

