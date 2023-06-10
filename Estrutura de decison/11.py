salario = float(input('Qual seu Salario ?   '))

if salario <= 280.0:
    acrescimo = salario * 1.20
    aumento = salario * 0.20
    porcentagem1 = '20%' 
elif 280 < salario < 700:
    acrescimo = salario * 1.15
    aumento = salario * 0.15
    porcentagem1 = '15%' 
elif 700 < salario < 1500:
    acrescimo = salario * 1.10
    aumento = salario * 0.10
    porcentagem1 = '10%' 
else:
    acrescimo = salario * 1.05
    aumento = salario * 0.05
    porcentagem1 = '05%' 

print(f'Seu Salario é de : {salario} ')
print(f'Seu aumento é de : {aumento} ')
print(f'Sua porcentagem é de : {porcentagem1} ')
print(f'o acrescimo foi de : {acrescimo} ')


