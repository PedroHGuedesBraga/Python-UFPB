import emoji
from emoji.core import emojize

sogro = str(input('Sograo vai dormir aqui ? '))

if sogro == 'sim':
     print(emoji.emojize('Mimir no colchao :pensive:',use_aliases=True))

if sogro == 'nao':
    print(emoji.emojize('Mimir na cama, minha coluna agradece :smiley:',use_aliases=True ))

