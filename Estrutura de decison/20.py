nota1 = float(input("Digite uma nota ")) 
nota2 = float(input("Digite uma nota "))
nota3 = float(input("Digite uma nota "))

media = (nota1+nota2+nota3)/3

if   7<= media <= 9.9:
    distincao = "Aprovado"
elif media < 7:
    distincao = "Reprovado"
elif media == 10.0:
    distincao = "Aprovado com Distinção"

print(distincao)
