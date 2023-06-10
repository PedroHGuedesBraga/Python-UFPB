import math
ang = float(input('Qual o Angulo ? '))

seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'Seno {seno:.1f}')
print(f'Cosseno {cos:.1f}')
print(f'Tangente {tan:.1f}')
