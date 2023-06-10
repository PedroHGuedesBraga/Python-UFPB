sexo = input('vc é homem ou mulher ?')

altura =  float(input('qual sua altura ? '))

calculo1 = float(72.*altura) - 58

calculo2 = (62.*altura) - 44.7

if sexo == "homem":
    print(calculo1)
elif sexo == "mulher":
    print(calculo2)