a = "Now is better than never"
print(a[0]) // 0
a[4]    // 'i'
a[-1]   // 'r'
a[-2]   // 'e'

b = a[0] + a[1] + a[2]
print(b)    // 'Now'

a[0:3]  // 'Now'
a[4:6]  // 'is'
a[19:]  // 'never'
a[:3]   // 'Now'
a[:]    // 'Now is better than never'
a[7:-11]    // 'better'

c = "Python"
c.count('p')    // 0