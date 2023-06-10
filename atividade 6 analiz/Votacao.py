marcilio = 0 
aurelio = 0
branco = 0

for c in range (4):

    voto = str(input("Qual Seu voto ? ")).lower.replace(" ","")

    
    if voto =='marcilio':
        marcilio = marcilio + 1
    elif voto == 'aurelio':
       aurelio = aurelio + 1
    elif voto == 'branco':
     branco = branco + 1

    
if (marcilio > aurelio) and (marcilio > branco):
    print("Marcilio")     
   
if (aurelio > marcilio) and (aurelio > branco):
    print('Aurelio')
else : 
    print("Nova votação")

resultado = marcilio , aurelio , branco

print(resultado)


        
    

