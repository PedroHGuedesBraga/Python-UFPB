import random
qual = str(input(' Par ou impar ? '))
num = int(input('Digite um numero entre 0 e 10 '))
numpc = random.randint(0,10)
jogos = 1
    
print(f'O computador jogou {numpc} ')
    
if num >10:
    print('Numero invalido')
if (num+numpc)%2 == 0:
    print('Deu Par')
if(num+numpc)%2 != 0:
    print('Deu Impar')

play = str(input("Ainda quer jogar ? Sim ou Nao ? ")).lower().strip()

while not play == "nao" :
    jogos += 1
    
    numpc = random.randint(0,10)

    qual = str(input(' Par ou impar ? '))

    num = int(input('Digite um numero entre 0 e 10 '))
    
    print(f'O computador jogou {numpc} ')
    
    if num >10:
        print('Numero invalido')
    if (num+numpc)%2 == 0:
        print('Deu Par')
    if(num+numpc)%2 != 0:
        print('Deu Impar')
    play = str(input("Ainda quer jogar ? Sim ou Nao ? ")).lower().strip()
    print(f"Vc jogou {jogos} vezes")