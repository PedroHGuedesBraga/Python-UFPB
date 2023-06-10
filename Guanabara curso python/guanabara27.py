n = str(input("Digite seu Nome ")).strip()
#o split() transforma a str em lista, entao nao ha alteracoes quando juntado com o .stip
nome = n.split()
#como a variavel nome esta numa lista [0,1,2,3..etc] eu pego a posicao 0 como primeiro nome
print(nome[0])
#neste caso o len vai contar quantas str tem na lista, e diminuir uma pois do python se conta a partir do zero
#para se obter a ultima str :
print(nome[len(nome)-1])
print(nome)



