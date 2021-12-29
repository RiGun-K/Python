# 함수 
# 일정 작업을 수행하는 코드블럭, 반복사용되는 코드들을 함수로 정의
# def 키워드 사용
    # def 함수명(입력파라미터):
    #     문장1
    #     문장2
    # [return 리턴값]

def sum(a, b):
    s = a + b
    return s
total = sum(4,6)
print(total)    # 10

# 파라미터 전달방식
    # 입력파라미터가 변경되지 않는 객체 (int, float, tuple, str, bool)면 변경 X
    # 함수가 그 함수 내에서 해당 객체의 내용을 변경시, 호출자에게 반영 ( 내부 함수 )
    # 하지만, 함수 내 새로운 객채에 파라미터가 할당되면 호출자에 반영 X ( 외부 함수 )

# 함수내 파라미터 값 변경
def f(i, mylist):
    i = i + 1
    mylist.append(0)

k = 10          # int (변경되지 않는 객체 = immutable)
m = [1,2,3]     # 리스트 (변경되는 객체 = mutable)

f(k,m)
print(k,m)      # 10 [1,2,3,0]

# Default Parameter
    # 입력파라미터 중 호출자가 전달하지 않으면 디폴트 값 1이 설정
def calc(i, j, factor = 1):
    return i * j * factor

result = calc(10, 20)   
print(result)   # 10 * 20 * 1

# Named Parameter
    # 정의된 파라미터 순서대로 말고 임의로 지정하는 방식
def report(name, age, score):
    print(name,score)
report(age=10, name="Gun", score=90)

# 가변길이 파라미터 
    # 입력파라미터 갯수를 미리 알 수 없거나, 0부터 N개의 파라미터를 받아 들이고자 할때 사용
    # 파라미터명 앞에 * 붙인다.
def total(*numbers):
    tot = 0
    for n in numbers:
        tot += n
    return tot

    # *numbers는 가변길이 파라미터이므로, total()을 호출시, 임의의 숫자 파라미터들을 지정할 수 있다.
t = total(1,2)
print(t)            # 3
t = total(1,5,2,6)
print(t)            # 14

# 리턴값
    # 함수로부터 호출자로 리턴
    # "return 리턴값"
def calc(*numbers):
    count = 0
    tot = 0
    for n in numbers:
        count += 1
        tot += n
    return count, tot   # 필요한 수만큼 콤마(,)로 구분하여 작성 

count, sum = calc(1,5,2,6)  # (count, tot) 튜플을 리턴
print(count, sum)           # 4 14 
