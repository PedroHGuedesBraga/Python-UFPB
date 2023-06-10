

preço1 = float(input('Qual valor do produto 1 ? '))
preço2 = float(input('Qual valor do produto 2 ? '))
preço3 = float(input('Qual valor do produto 3 ? '))

if preço1 < preço2 < preço3 :
   print(f'O melhor preço foi o {preço1}')
elif preço2 <preço1 < preço3 :
    print(f'O melhor preço foi o {preço2}')
elif preço3 < preço2 < preço1 :
    print(f'O melhor preço foi o {preço3}')



