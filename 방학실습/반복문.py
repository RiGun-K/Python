# for 문
test_list = ['one','two','three']
for i in test_list:
    x = i + '!'
    print(x)
    
# one! 
# two!
# three!

number = 0
for score in [90, 25, 67, 45, 93]:
    number += 1
    if score >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)
        
# 1번학생은 합격입니다
# 2번학생은 불합격입니다
# 3번학생은 합격입니다
# 4번학생은 불합격입니다
# 5번학생은 합격입니다

# While 문
i = 0
while i < 5:
    i += 1
    print('*' * i)
    
# *
# **
# ***
# ****
# *****

# for 반복변수 in range(start, stop, step):

list(range(10)) # [0,1,2,3,4,5,6,7,8,9]
list(range(1,10)) # [1,2,3,4,5,6,7,8,9]
list(range(0,11,2)) # [0,2,4,6,8,10]

sum = 0
for i in range(0,11,2):
    sum = sum + i

print(sum)  # 30