# str (문자열 클래스)

s = "ABC"
type(s)     # class 'str'
v = s[1]    # B
type(s[1])  # class 'str'

# s[1]의 타입이 char가 아니라 문자열 str 타입
# type(변수명) = 해당 변수의 타입 리턴

# 자주 사용되는 str 메서드

# str.join()    - 여러 개의 문자열을 하나로 결합 
s = ','.join(['가나','다라','마바'])
c = ''.join(['가나','다라','마바'])
print(s)    # 가나,다라,마바
print(c)    # 가나다라마바

# str.split()   - 문자열을 분리하여 리스트를 리턴 ( join()과 반대 )
items = '가나,다라,마바'.split(',')
print(items)    # ['가나','다라','마바']

# str.partition()   - 문자열을 분리하여 n개의 값을 리턴
departure, _, arrival = "Seattle-Seoul".partition('-')
print(departure)    # Seattle

# str.format()      - 가장 많이 사용

    # 위치를 기준으로 한 포맷팅
s = "Name: {0}, Age: {1}".format("강정수", 30)
print(s)    # Name: 강정수, Age: 30
    # 필드명을 기준으로 한 포맷팅
s = "Name: {name}, Age: {age}".format(name="강정수", age=30)
print(s)    # Name: 강정수, Age: 30
    # Object의 인덱스 혹은 키를 사용한 포맷팅
area = (10, 20)
s = "width: {x[0]}, height: {x[1]}".format(x = area)
print(s)    # width: 10, height: 20

# bytes ( 바이트 클래스 )

s = "Hello"
b = s.encode()
print(b)    # b'Hello'
s2 = b.decode()
print(s2)   # 'Hello'

# 특정 인코딩 방식을 지정한 경우
x = "안녕".encode("UTF-8")
y = x.decode("UTF-8")


