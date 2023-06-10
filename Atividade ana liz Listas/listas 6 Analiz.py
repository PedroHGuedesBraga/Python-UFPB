Quantidade_Alunos = [ ]
soma = 0

for c in range (4):
    turma = int(input("Quantos Alunos tem A turma ? "))
    Quantidade_Alunos.append(turma)
    soma += turma
print (f" Ao total tem-se : {soma} Alunos ")
print (f" Sao turmas de  : {Quantidade_Alunos} Alunos ")
