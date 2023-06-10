valorporhora =  float(input('qual valor por hora ? '))

numerodehoras = float(input('quantas horas trabalhadas no mes  ? '))

salario = valorporhora*numerodehoras

ir = salario%11

inss = salario%8

sindicato = salario%5

salarioliquido = salario - (ir + inss +  sindicato)

print(salarioliquido)