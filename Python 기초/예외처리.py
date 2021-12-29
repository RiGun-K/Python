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


# 복수 예외들이 동일한 except 블