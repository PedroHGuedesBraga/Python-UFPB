nome = str(input("Qual o seu nome ? ")).strip()

maius = nome.upper()
minusc = nome.lower()
prim = nome.split()[0]
sobre = nome.split()[1:15]

print(maius)
print(minusc)
print(len(nome))
print(prim)
print(sobre)
