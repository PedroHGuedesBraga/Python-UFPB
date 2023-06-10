peixesporquilo = float(input('quantos quilos de peixe ? '))

if peixesporquilo > 50:


    execendete1 = (peixesporquilo-50)
    execendete2 = (peixesporquilo-50)*4 
    print(f'vc ultrapassou o peso limitem em :{execendete1:.2f} reais ')
    print(f'vc deve pagar a mais : {execendete2:.2f} reais')

else : 
    print("Vc não ultrapassou o limite")