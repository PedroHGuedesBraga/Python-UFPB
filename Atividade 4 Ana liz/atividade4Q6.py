a = 3 
b = 2 * a
c = b % 5 

if (a + b < c + 7):
    b = c + 5
    if (b > 4):
        c = a + 8
    else :
         a = c + 2
else: 
    b = 5 * c
    if (b <= 5):
        c = a + b
    else : 
        a = 3 * b 
    b = (2 * a) - 1
a = a - b + c

print(a)
print(b)
print(c)
