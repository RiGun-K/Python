# 예외처리
    # try.. except.. finally 문
    
    # except 뒤에 "에러타입" 또는 "에러타입 as 에러변수" 작성시 
    # 특정 타입의 에러가 발생할 경우만 해당 except 블럭 실행

def calc(values):
    sum = None
    # try...except...else
    try:
        sum = values[0] + values[1] + values[2]
    except IndexError as err:
        print('인덱스에러')
    except Exception as err:
        print(str(err))
    else:
        print('에러없음')
    finally:
        print(sum)

calc([1, 2, 3, 6])  # 에러없음 6
calc([1, 2])        # 인덱스에러 None


# 복수 예외들이 동일한 except 블럭을 가지면,
# 하나의 except 문에 묶어서 사용 가능

def calc(values2):
    sum = None
    try:
        sum = values[0] + values[1] + values[2]
    except:
        print('오류발생')
    print(sum)

# 에러무시와 에러생성
    # 보통 pass문 사용

try:
    check()
except FileExistsError:
    pass

    # 에러를 던지기 위해 raise문 사용 (뒤에 공백이면 현재 Exception)

if total < 0:
    raise Exception('Total Error')

# 파일 에러 처리 예제
try:
    fp = open("test.txt", "r")
    try:
        lines = fp.readlines()
        print(lines)
    finally:
        fp.close()
except IOError:
    print('파일에러')

with open('test.txt', 'r') as fp:
    lines = fp.readlines()
    print(lines)