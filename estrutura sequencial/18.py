
tamanhoemMB = float(input('Qual o tamanho do arquivo ? '))

velocidade = float(input('Qual a velocidade da internet '))

tempo = tamanhoemMB/(velocidade/8)

tempoEmMinutos = tempo/60

print(f'seu tempo em minutos de donwload foi de {tempoEmMinutos:.2f} Minutos')
