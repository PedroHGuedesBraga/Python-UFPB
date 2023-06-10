nota1 = float(input('Digita sua primeira nota : '))

nota2 = float(input('Digita sua segunda nota : '))

media = (nota1+nota2)/2 

if (9.0< media <=10.0):
    conceito =  'A'
elif (7.5< media <=9.0):
    conceito = 'B'
elif (6.0< media <=7.5):
    conceito = 'C'
elif (4.0< media <=6.0):
    conceito = 'D'
else:
    conceito = 'E'

print(f'Sua primeira Nota foi: {nota1}')

print(f'Sua Segunda Nota foi: {nota2}')

print(f'Sua Media foi: {media}')

if conceito == 'A' or conceito == 'B' or conceito == 'C' :
    print('Voce Foi Aprovado')
elif conceito == 'D' or conceito ==  'E':
    print('Voce Foi Reprovado')






