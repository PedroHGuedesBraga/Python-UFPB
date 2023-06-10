#Considerando a elaboração de um programa para automatizar a folha de pagamento dos funcionários da empresa PagueAqui, classifique cada afirmativa como Verdadeira ou Falsa. 
nome = input('Qual seu nome ? ').strip().lower()
dia = input('qual o dia da semana ? ').strip().lower()
hora = float(input('Qual a hora ? '))

if (hora == 8 ):
    if (dia =='segunda') or (dia == 'sexta '):
        print(nome)    
    