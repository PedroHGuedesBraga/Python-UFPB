

nota1 = float(input('Qual sua primeira nota ? '))

nota2 = float(input('Qual sua segunda nota ? '))

media = (nota1+nota2)/2

if media == 10:
    print(f'Aprovado com distinçao {media} ')
elif media >= 7:
    print(f'Aprovado com {media} ')
elif media < 7:
    print(f'Reprovado {media} ')
