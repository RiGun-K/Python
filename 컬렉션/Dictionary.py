# "키(Key) - 값(Value)" 쌍을 요소로 갖고 Map이라 불림
# 키(Key)로 신속하게 값(Value)을 찾아냄 
# 키(Key)는 값을 변경 X  , 값(Value)은 변경가능 
# 키(Key)로 문자열이나 Tuple로 사용가능 , 단 리스트는 X
# 표현 : {...} 

scores = {"철수":90, "민수":85, "영희":80}
v = scores["민수"]      # 특정 요소 읽기
scores["민수"] = 88     # 변경 (값은 변경 가능)
del scores["영희"]      # 삭제
print(scores)

# 1. Tuple List로 부터 dict 생성
persons = [('김기수',30), ('홍대길',35), ('강찬수',25)]
mydict = dict(persons)

age = mydict["홍대길"]
print(age)      # 35

# 2. Key=Value 파라미터로부터 dict 생성
scores = dict(a=80, b=90, c=85)
print(scores['b'])  # 90

# 추가,수정,삭제,읽기
scores = {"철수":90, "민수":85, "영희":80}

for key in scores:
    val = scores[key]
    print("%s : %d" % (key, val))
    # 철수 : 90 민수 : 85 영희 : 80

    # keys 값 뽑기
keys = scores.keys()
for k in keys:
    print(k)
    # values 값 뽑기
values = scores.values()
for v in values:
    print(v)

# dict의 items() 는 키-값 쌍 Tuple로 구성된 객체를 리턴
scores = {"철수":90, "민수":85, "영희":80}
items = scores.items()
print(items)
    # dict_items([('민수',85), ('영희',80), ('철수',90)])

    # dict_items를 리스트로 변환
itemsList = list(items)

# dict.get() - 특정 키에 해당하는 값을 리턴 , 없으면 None 리턴
scores = {"철수":90, "민수":85, "영희":80}
v = scores.get("민수")  # 85
v = scores.get("길동")  # None
v = scores["길동"]      # 에러
    # 멤버쉽연산자 in 사용 , 키가 Dictionary에 존재하는지 체크
if "길동" in scores:
    print(scores["길동"])

scores.clear()          # 모두 삭제

# dict.update()
persons = [('김기수',30), ('홍대길,35'), ('강찬수',25)]
mydict = dict(persons)
    # 여러 데이터를 한꺼번에 변경 
mydict.update({'홍대길':33, '강찬수':26})   
