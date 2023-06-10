valorhora = float(input('Qual seu valor por hora ? '))

horastrab = float(input('Quantas horas trabalhadas ? '))

salariobruto = valorhora * horastrab

inss = salariobruto * 0.10

fgts = salariobruto * 0.11

if salariobruto <= 900:
    impostoDeRenda = 0 
    imposto = 0.00
elif salariobruto <= 1500:
    impostoDeRenda = salariobruto * 0.05
    imposto = 0.05

elif salariobruto <= 2500:
    impostoDeRenda = salariobruto * 0.10
    imposto = 0.10
else:
    impostoDeRenda = salariobruto * 0.20
    imposto = 0.20

totalDescontos = inss +  impostoDeRenda

salarioliquido = salariobruto - totalDescontos

print(f'Salario Bruto : ({valorhora} * {horastrab}) : R$ {salariobruto}')
print(f' (-) IR ({imposto*100}%)  : R$ {impostoDeRenda}')
print(f' (-) INSS (10%)           : R$ {inss}')
print(f' (-) FGTS (11%)           : R$ {fgts}')
print(f'Total De descontos        : R$ {totalDescontos}')
print(f'Salário Liquido           : R$ {salarioliquido}')


