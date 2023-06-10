frase = str(input("Digite uma frase : ")).upper().replace(" ", "")
frasea = frase.count("A")
#o +1 foi adicionado pois o python comeca a contar
#apartir do zero, logo, numa situacao real
#a letra ficaria em uma posicao menor do 
#que a deveria
fraseI = frase.find("A")+1
#a adicao do `r` foi para achar apartir do
#lado direito 
frasefinal = frase.rfind("A")+1
print(frase)
print(frasea)
print(fraseI)
print(frasefinal)