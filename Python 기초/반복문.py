# 반복문 : while , for , break/continue, range

# while ( 참일 경우 무한반복 )
i = 1
while i <= 10:
    print(i)    # 1 ~ 10 까지 출력
    i += 1

# for ( 하나의 요소를 가져와, 루프 내 문장을 실행 )
    # 리스트, Tuple, 문자열 등의 컬렉션 - " for 요소변수 in 컬렉션" 형식
    # 내장함수 range(n) 함수는 0 부터 n-1 까지의 숫자를 갖는 리스트를 리턴
sum = 0
for i in range(11):
    sum += i    # 0 부터 10까지 숫자를 받아 합을 리턴
print(sum)      # 55

    # 각 문자열들을 순차적으로 출력
list = ["This", "is", "a", "book"]
for s in list:
    print(s)

# break/continue 
    # break ( 반복문을 빠져나옴. )
    # continue ( 이후 문장들을 실행하지 않고 다시 반복문으로 이동 )
i = 0
sum = 0
while True:
    i += 1
    if i == 5:
        continue
    if i > 10:
        break
    sum += i
print(sum)  # 1 부터 10 까지 합 ( 단, 5를 제외 )

# range 
    # range(3)      Stop                = 0,1,2
    # range(3,6)    Start, Stop         = 3,4,5
    # range(2,11,2) Start, Stop, Step   = 2,4,6,8,10

numbers = range(2, 11, 2)

for x in numbers:
    print(x)
    # 각 라인에 2 4 6 8 10 출력

    # 몇 번 루프를 도는가를 표시
for i in range(10):
    print("Hello Python")   
    # 문자열을 10번(0 부터 9까지) 출력 

