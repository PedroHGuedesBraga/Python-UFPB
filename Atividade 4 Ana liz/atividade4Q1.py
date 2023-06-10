#Para ser aprovado em uma disciplina, um aluno deve ter média pelo menos 7 e no máximo 20 faltas. Considerando um programa que receba como entrada as informações necessárias (média e faltas), marque os trechos de código abaixo que poderiam ser usados para exibir as mensagens corretamente no programa:
media = float(input('Qual sua media ? '))

faltas = int(input('Quantidade de faltas ? '))

#LETRA S N FUNCIONA

#LETRA E n funciona
'''if (media < 7) and (faltas > 20):   
    print('reprovado')
else:
    print('Aprovado')'''


#LETRA G FUNCIONA
'''if (media>= 7):
    if(faltas<= 20):
        print('Aprovado')
    else:
        print('reprovado')
else:
        print('reprovado')'''
    

# LETRA C funciona
'''if (media >= 7) and (faltas <= 20):
    print('Aprovado')
else:
    print('reprovado')'''

#LETRA M n funciona
'''if (media>=7):
   print('Aprovado') 
elif(faltas<=20):
    print('reprovado')
else:
    print('reprovado')'''

#LETRA V n funciona

'''if (media>=7):
    print('Aprovado') 
if (faltas<=20):
    print('Aprovado')
else:
   print('reprovado')'''






