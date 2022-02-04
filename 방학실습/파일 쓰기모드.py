f = open("C:/Users/RiGun/새파일.twt", 'w')
print(f)    # 파일경로 추적
f.close()   # 종료

f = open("C:/Users/RiGun/새파일.twt", 'w')
for i in range(1,6):
    data = "%d번째 줄입니다. \n"% i
    f.write(data)   # 메모장에 텍스트 추가 
    
f.close()   # close() 를 해야 작성됨 

# 파일모드 'a'
f = open("C:/Users/RiGun/새파일.twt", 'a')
for i in range(6,11):
    data = "%d번째 줄 추가입니다. \n"% i
    f.write(data)
    
f.close()

