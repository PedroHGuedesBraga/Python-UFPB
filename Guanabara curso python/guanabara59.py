valor1 = float(input( "Digite um valor X "))
valor2 = float(input( "Digite um valor Y "))

menu = str(input('''--- Digite : 1 para somar
---Digite : 2 para multiplicar                      
---Digite : 3 para maior  
---Digite : 4 para novos numeros                     
---Digite : 5 para sair do programa '''))

while not menu == '5':
    if menu == "1":
        print(valor1+valor2)
        menu = str(input(''' Digite : 1 para somar
                                Digite : 2 para multiplicar                      
                                Digite : 3 para maior  
                                Digite : 4 para novos numeros
                                Digite : 5 para sair do programa-- '''))
    if menu == "2":
        print(valor1*valor2)
        menu = str(input(''' Digite : 1 para somar
                                Digite : 2 para multiplicar                      
                                Digite : 3 para maior  
                                Digite : 4 para novos numeros
                                Digite : 5 para sair do programa-- '''))
    if menu == "3":
        if valor1 > valor2:
            print(valor1)
            menu = str(input(''' Digite : 1 para somar
                                Digite : 2 para multiplicar                      
                                Digite : 3 para maior  
                                Digite : 4 para novos numeros
                                Digite : 5 para sair do programa--'''))
        if valor2 > valor1:
            print(valor2)
            menu = str(input(''' Digite : 1 para somar
                                Digite : 2 para multiplicar                      
                                Digite : 3 para maior  
                                Digite : 4 para novos numeros
                                Digite : 5 para sair do programa-- '''))
    if menu == "4":
        valor1 = float(input( "Digite um valor X "))
        valor2 = float(input( "Digite um valor Y "))
        menu = str(input('''     Digite : 1 para somar
                                Digite : 2 para multiplicar                      
                                Digite : 3 para maior  
                                Digite : 4 para novos numeros
                                Digite : 5 para sair do programa-- '''))
    if menu == "5":
        print("Fechando Calculadora")

