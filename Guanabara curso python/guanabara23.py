numero = input("Digite um Numero com 4 casas ")

mil= numero[0:1]
cent = numero[1:2]
dez = numero[2:3]
unidade = numero[3:4]

print(f'Seu numero foi : {numero}')
print(f'Seu numero tem {mil} mil ')
print(f'Seu numero tem {cent}  centenas ')
print(f'Seu numero tem {dez}  dezenas  ')
print(f'Seu numero tem {unidade}  unidade ')