# Set 은 중복이 없는 요소들로 구성 , { } 으로 표현
# 요소들을 순서대로 저장 X , 인덱스 사용 불가
# 중복된 값을 입력하는 경우, 출력은 중복된 하나의 값만 출력

# set 정의
myset = { 1, 1, 3, 5, 5 }   
print(myset)                # { 1, 3, 5 }

# 리스트를 set으로 변환
mylist = ["A", "A", "B", "B", "B"]
s = set(mylist)
print(s)                    # {'A', 'B'}

# Set에서의 추가 및 삭제
    # 추가 : add()
    # 한꺼번에 추가: update()
    # 삭제 : remove() , discard()
    # 모두 삭제: clear()
myset = { 1, 3, 5 } 

myset.add(7)                # {1,3,5,7}
myset.update({4,2,10})      # {1,2,3,4,5,7,10} - 순서 상관 X
myset.remove(1)             # {1} 삭제
myset.clear()               # All 삭제

# 집합 연산
a = {1,3,5}
b = {1,2,5}

    # 교집합
i = a & b                   # {1,5}

    # 합집합
u = a | b                   # {1,2,3,5}

    # 차집합
d = a - b                   # {3}
