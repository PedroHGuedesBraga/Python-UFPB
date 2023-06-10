#Para calcular o preço do seu computador selecione as opcões para as  seguintes peças 

#processadores =  

ryzen51600AF = 799.00

ryzen52400g = 1207.00

ryzen53400g = 1279.00


#placasDeVideo = 
    
gtx1650 = 1700.00 

gtx1660Super = 3000.00

rx570 = 2083.00


#placaMãe 

msiTomahawk = 596.00

asusB450MA = 649.00

biostarRacingX370GTN = 589.00


#memoriaRam = 

crucialBALLISTIX_2x8GB = 549.00

corsairVengeanceRGB_2x8GB = 649.00

hyperXFury_2x8GB = 629.00  


#fonte 

cx750W80Plus = 659.00

evga500W80Plus = 299.00

cv550W80plus = 379.00


#Gabinete = 

aigoRainwbow2Preto = 179.00

bluecaseBG014 = 230.00

pichauLarkPGLK01 = 290.00


#EXEMPLO 



processador = str.lower((input('qual processador ')))


placasDeVideo = str.lower((input('qual placa de video ')))


placaMãe  = str.lower((input('qual placa mãe ')))


memoriaRam = str.lower((input('qual memoria RAM ')))


fonte = str.lower((input('qual fonte ')))


gabinete = str.lower((input('qual gabinete ')))


custo = processador + placasDeVideo + placaMãe + memoriaRam  + fonte + gabinete

#Processadoresparte 
if processador == "ryzen51600AF":
    print(ryzen51600AF)

if processador == "ryzen52400g":
    print(ryzen52400g)

if processador == "ryzen53400g":
    print(ryzen53400g)


    