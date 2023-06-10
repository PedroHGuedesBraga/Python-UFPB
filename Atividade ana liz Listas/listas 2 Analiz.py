quantidadeFor = 5
numeros = []
for c in range (quantidadeFor):
    numero = int(input("Digite um numero : "))
    numeros.append(numero)
    numeros.sort()

print(f" O ultimo numero foi :{numeros[4]} ")
