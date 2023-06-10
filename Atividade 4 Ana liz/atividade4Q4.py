a = 8 % 5

if(a <= 3):
    b = a // 2
else:
    b = a % 1
a += 2
c = a + b - 3

if(b >= 4):
    a = 2 + c
    c = c - 5 
elif(a!= 5 ):
    b = a - 1 
c += 2 * a
print(a)
print(b)
print(c)