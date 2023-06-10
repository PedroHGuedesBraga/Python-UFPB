lado1 = float(input('Digite o  primeiro lado do Triângulo '))

lado2 = float(input('Digite o terceiro lado do Triângulo '))

lado3 = float(input('Digite o  terceiro lado do Triângulo '))

if lado1+lado2 > lado3:
    print('É um Triângulo : ')
elif lado2 + lado3 > lado1:
    print('É um Triângulo : ')
elif lado1+lado3 > lado2:
    print('É um Triângulo : ')
else:
    print('Nao é um Triângulo ')

if (lado1 or  lado2  or lado3) <= 0:
    print(' ')
elif lado1 == lado2 == lado3:
    print('Triângulo Equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
    print('Triângulo Isósceles ' )
else:
    print('Triângulo Escaleno')

