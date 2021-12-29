# 튜플 (Tuple) 
    # 새로운 요소를 추가,갱신,삭제 할 수 없다 !! , 고정된 값
    # 표현 : (...) 
t = ("AB", 10, False)
print(t)
    
    # 요소가 하나일 경우 뒤에 콤마(,) 를 붙여 Tuple 임을 명시해야한다 ! 
t1 = (123)  # int 타입
t2 = (123,) # tuple 타입

# 튜플 인덱싱과 슬라싱
t = (1, 5, 10)
    # 인덱스
second = t[1]   # 5
last = t[-1]    # 10
    # 슬라이스
s = t[1:2]      # (5)
s = t[1:]       # (5, 10)

# 튜플 병합과 반복
    # 병합
a = (1, 2)
b = (3, 4, 5)
c = a + b   # (1, 2, 3, 4, 5)
    # 반복
d = a * 3   # "d = 3 * a"와 동일

# 튜플 변수 할당
name = ("Kim", "Ri", "Gun")
print(name) # ('Kim', 'Ri', 'Gun')

firstname, middlename, lastname = ("Kim", "Ri", "Gun")
print(lastname, ",", middlename, ",", lastname) # Gun, Ri, Kim



