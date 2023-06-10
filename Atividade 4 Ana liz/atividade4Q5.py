#Após a execução do código abaixo, quais serão os valores das variáveis a, b e c?
a = 5
b = a - 2

if(b>a):
    if(a>7):
        b = a + 1
        c = 2 * a 
    else:
        c = a - b
elif(a < 5 ):
    if(b == 3):
        a = a + b
    else :
        b = 2*b + a
else:
    if(a > 2):
        b = a - 5
        c = 2*a - b
    else:
        b = 3 - a
        c = 4 + a*2
a = b - 1

print(a)
print(b)
print(c)
