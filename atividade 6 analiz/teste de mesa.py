a = 2
b = 7

if(b - a >3 ):
    c = a + b
    b = 2 * b
    a = a + 3
else:
    c = a - b
    b = b/2
while (c/3>1):
    d = c + 1
    c = c / 3
    for e in range (1,3):
        a = a +e
        b = b - e 
    e = a + c - b
    if((a+c) == (d+1)):
        a = d
        c = b

print(a,b,c,d,e)
