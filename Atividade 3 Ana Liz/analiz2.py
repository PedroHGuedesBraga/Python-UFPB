produto = int(input("Qual o valor do produto ? "))
dinheiro = int(input('Quanto vc vai pagar ? '))

troco = dinheiro - produto

if troco == 1:
    print(" 1 Real de troco ")
if troco == 2:
   print("  1 nota de 2 Reais de troco ") 
if troco == 5:
   print("  1 nota de 5 Reais de troco ")

if troco == 0:
    print(f" sem troco ")

if troco != 0: 
    print(f'o Seu troco foi de: {troco}')
    troco1 = troco//5
    print(f" Sao : {troco1} nota(s) de 5 reais " )
    if troco1 != 0 :
        troco2 = (troco - (troco1*5))//2
        print(f" Sao : {troco2} nota(s) de 2 reais " ) 
        
        if troco2 != 0:
            troco3 = troco-((troco1*5)+(troco2*2))
            print(f" Sao : {troco3} moeda(s) de 1 real" ) 
#MEU DEUS DO CEU, EU PASSEI ... SEM MEME, 1 HORA ESCREVENDO A LOGICA DOS TROCOS PQ NAO ENTRAVA NA MINHA CABEÇA, MAS DEU CERTO
#OBRIGADO MÃE, PAI, MINHA FAMILIA POR ESSA CONQUISTA 
        
        
        
        
       
          


