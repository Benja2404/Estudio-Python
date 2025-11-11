
#lista = [letra for letra in 'pyton']
#print(lista)

#lista = [n if n * 2 > 10 else 'no' for n in range(0,21, 2)]
#print(lista)




#pies = [10,20,30,40,50]
#metros = [n / 3.281 for n in pies]
#print(metros)
 
#valores = [1, 2, 3, 4, 5, 6, 9.5] 
##valores_pares = [n for n in valores if n % 2 == 0]
#print(valores_pares)
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [ (n - 32)*(5/9) for n in temperatura_fahrenheit]
print(grados_celsius)