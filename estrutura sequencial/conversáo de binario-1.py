num = int(input("Diga o numero a ser convertido :"))
conv = int(input("""Deseja converter ele para 
[-1-] Binario
[-2-] Hexadecimal
[-3-] Octal
"""))
if conv == 1:
 	print("Esse valor é {} em Binario" .format(bin(num)))
elif conv == 2:
 	print("Esse valor é {} em Hexadecimal" .format(hex(num)))
elif conv == 3:
 	print("Esse valor é {} em Octal" .format(oct(num)))