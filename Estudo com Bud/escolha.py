import random
numero = int(input("Descubra qual o numero entre 0 e 1 "))
computador = random.randint(0,10)
tentativas = 0
if numero == computador:
        print("Voce achou o numero : ")
        print(computador)
while numero != computador:
    if numero == computador:
        print("Voce achou o numero : ")
        print(computador)
        
    if numero < computador:
        print('Mais')
        tentativas += 1
        numero = int(input("Descubra qual o numero entre 0 e 100 "))
    if numero > computador:
        print("menos")
        tentativas += 1
        numero = int(input("Descubra qual o numero entre 0 e 100 "))
    
    if numero == computador:
        print("Voce achou o numero : ")
        
        print(computador)
        
        print(f"Voce tentou {tentativas} vezes ")
        
        
    
