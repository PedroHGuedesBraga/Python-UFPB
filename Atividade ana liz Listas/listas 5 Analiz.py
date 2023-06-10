notas = [ ]
nota8 = 0
for c in range(5):
    nota = float(input("Qual a sua nota ? "))
    notas.append(nota)

for c in range(5):
    if notas[c] > 8:
        nota8 += 1
        
print(f"Foram : {nota8} acima de 8" )
