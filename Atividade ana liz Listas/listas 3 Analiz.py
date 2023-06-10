numeros = []
quantidadeFor = 8

for c in range(quantidadeFor):
    n =  int(input("Digite um numero "))
    numeros.append(n)

for c in range (quantidadeFor):
    if (numeros[c] % 2 == 0):
        print(numeros[c])
print(numeros)


    