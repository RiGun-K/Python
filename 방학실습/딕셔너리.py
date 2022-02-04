dic = {'name':'Hong', 'phone':'01012345678', 'birth':'0814'}
dic[1] = 'a'
dic # {'name':'Hong', 'phone':'01012345678', 'birth':'0814', 1:'a'}

dic['pet'] = 'dog'
dic # {'name':'Hong', 'phone':'01012345678', 'birth':'0814', 1:'a', 'pet':'dog'}

del dic[1]  # 원소 삭제
dic['pet']  # 'dog' , 원소의 value 구하기

dic.keys()  # dict_keys(['name','phone','birth','pet']) // key 리스트 생성
list(dic.keys())    # ['name','phone','birth','pet']

dic.values() # dict_values(['Hong','01012345678','0814','dog']) // value의 리스트 만들기
list(dic.values())  # ['Hong','01012345678','0814','dog']

dic.items() # key,value 쌍 구하기

dic.clear() # 원소 삭제
dic // {}
