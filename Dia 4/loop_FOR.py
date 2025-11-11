#lista = ['a','b','c','d']
#for letra in lista:
   # numero_letra = lista.index(letra) + 1
   # print(f"Letra {numero_letra}: {letra}") 


#lista = ['Pablo', 'laura', 'fede', 'luis', 'julia']
#for nombre in lista:
  #  if nombre.startswith('l'):
  #      print(nombre)
   # else:
       # print("nombre que no comienza con l")
#mi_valor = 0
#for numero in lista:
   # mi_valor = mi_valor + numero
    #print(mi_valor)

#palabra = 'python' # cadena de caracteres
#for letra in palabra: # iterar sobre cada letra
   # print(letra) # cadena de caracteres



#for a,b in [[1,2], [3,4], [5,6]]:  # lista de listas
   # print(a) # imprime el primer elemento de cada sublista
   # print(b) # imprime el segundo elemento de cada sublista
  

#dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
#for a,b in dic.items():
    #print(a,b)



lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for num in lista_numeros:
    if num % 2 == 0:
       suma_pares = suma_pares + num
    else:
        suma_impares = suma_impares + num
print("Suma de números pares:", suma_pares)
print("Suma de números impares:", suma_impares)
