a = "Now is better than never"

a.find('y') # 1
a.find('p') # -1(찾지못함)

a.index('y')    # 1
a.index('p')    # 에러

b = ","
c = b.join('Abcd')
print(c)    # 'A, b, c, d'

a.upper()   # 'PYTHON'
a.lower()   # 'python'

d = " py "
d.lstrip()  # 'py   '
d.rsplit()  # '   py'

a = 'Pithon'
a[1] = 'y'  # 에러

a = "Python is difficult"
a.replace("difficult", "funny")     # 'Python is funny'
a.split()   # ['Python', 'is', 'difficult']

b = "a,b,c,d"
print(b)    # 'a,b,c,d'
b.split(',')    # ['a','b','c','d']  

