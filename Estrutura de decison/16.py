a = float(input('Digite um Valor para A '))

b = float(input('Digite um Valor para B '))

c = float(input('Digite um Valor para C '))


delta = (b**2) - 4 * a * c

raiz = float(delta)**0.5

x1 = (-b + (raiz))/2*a

x2 = (-b - (raiz))/2*a

if a == 0:
    print(' a equação não é do segundo grau ')
elif delta < 0:
    print('a equação não possui raizes reais.')
elif delta == 0:
    if b < 0:
        print(x1)
else:
    print(x1)
    print(x2)
    








