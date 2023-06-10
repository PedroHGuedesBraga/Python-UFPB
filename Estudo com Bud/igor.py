
produto = input('qual o produto desejado : fungicida, herbicida ou inseticida? ').strip().lower()

area = float(input('Qual a Area em hecatares ? '))

dosefun = 1.0 * area

doseherb = 0.3 * area

doseinset = 2.5 * area

totfun = dosefun // 50

totherb = doseherb // 1

totinset = doseinset //30

fungicida = area*6.4

herbicida = area*30

inseticida = area*33.3

if fungicida <= 50.0:
    print('fungicida')
    print(area)
    print('1 fungicida(s) O valor a ser pago é 320.00 Reais')


elif fungicida >= 50.0 :
        print('fungicida')
        print(area)
        print(f'{totfun} O valor a ser pago é {fungicida:.2f} ')


    
if produto == 'herbicida':
        print('herbicida')
        print(area)
        print(f'{totherb} O valor a ser pago é {herbicida:.2f} ')


if produto == 'inseticida':
        print(area)
        print('inseticida')
        print(f'{totinset} O valor a ser pago é {inseticida:.2f} ')