mf = str(input("Digite o sexo sendo M ou F ")).lower()

#While consegue usar operacao != da matematica para caracterizar strings diferentes
while not mf == 'm' or mf == 'f':
    print("Digite novamente ")
    mf = str(input("Digite o sexo sendo M ou F ")).lower()
if mf == "m":
    print("Masculino")
if mf == "f":
    print("feminino")
    
       


