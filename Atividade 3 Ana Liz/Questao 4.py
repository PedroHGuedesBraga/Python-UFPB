#Considerando a elaboração de um programa para automatizar a folha de pagamento dos funcionários da empresa PagueAqui, classifique cada afirmativa como Verdadeira ou Falsa

horas = float(input(' Quantas horas trabalhadas ? '))

valorporhora = 200

salario = horas * valorporhora

imposto = salario * 0.07

salarioLiq = salario - imposto 

print(f'Seu Salario sera de : {salarioLiq} Reais ')

