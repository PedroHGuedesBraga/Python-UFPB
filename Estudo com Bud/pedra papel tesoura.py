#Pedra Papel E tesoura para pessoas tristes
import random
player = input('pedra, papel ou tesoura ').lower()
lista = ['tesoura','papel', 'pedra'] 
computador = random.choice(lista)

print(f'computador escolheu : {computador} ')

print(f'voce escolheu : {player} ')



if player == 'pedra' and computador == 'tesoura':
    print('Voce Ganhou')
if player == 'papel' and computador == 'tesoura':
    print('Voce Perdeu')
if player == 'tesoura' and computador == 'tesoura':
    print('Deu Empate')

if player == 'pedra' and computador == 'papel':
    print('Voce Perdeu')
if player == 'papel' and computador == 'papel':
    print('Deu Empate')
if player == 'tesoura' and computador == 'papel':
    print('Voce Ganhou')

if player == 'pedra' and computador == 'pedra':
    print('Deu Empate')
if player == 'papel' and computador == 'pedra':
    print('Voce Ganhou')
if player == 'tesoura' and computador == 'pedra':
    print('Voce Perdeu')

pergunta = str(input("Voce ainda quer jogar ? sim ou nao ? "))

while not pergunta == "nao":

    player = input('pedra, papel ou tesoura ')

    lista = ['tesoura','papel', 'pedra'] 
    
    computador = random.choice(lista)

    print(f'computador escolheu : {computador} ')

    print(f'voce escolheu : {player} ')


    if player == 'pedra' and computador == 'tesoura':
        print('Voce Ganhou')
    if player == 'papel' and computador == 'tesoura':
        print('Voce Perdeu')
    if player == 'tesoura' and computador == 'tesoura':
        print('Deu Empate')

    if player == 'pedra' and computador == 'papel':
        print('Voce Perdeu')
    if player == 'papel' and computador == 'papel':
        print('Deu Empate')
    if player == 'tesoura' and computador == 'papel':
        print('Voce Ganhou')

    if player == 'pedra' and computador == 'pedra':
        print('Deu Empate')
    if player == 'papel' and computador == 'pedra':
        print('Voce Ganhou')
    if player == 'tesoura' and computador == 'pedra':
        print('Voce Perdeu')

    pergunta = str(input("Voce ainda quer jogar ? S ou N ? "))