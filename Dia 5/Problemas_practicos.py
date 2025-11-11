
#Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros

"""
def devolver_distintos(num1, num2, num3):
                                                #  Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
 if num1 + num2 + num3 > 15:
    return max(num1, num2, num3)
                                                # Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
 elif num1 + num2 + num3 in range(10,16):
    return sorted([num1, num2, num3])[1]
        
print(devolver_distintos(7, 5, 6))  # Debería devolver 6
"""



# Escribe una función (puedes ponerle cualquier nombre que
# quieras) que reciba cualquier palabra como parámetro, y que
# devuelva todas sus letras únicas (sin repetir) pero en orden
# alfabético.
""" 
def ordenar_letras(frase):
     letras = list(frase)
     alfabetizar = sorted(letras)
     sin_repetidos = set(alfabetizar)
     return sorted(sin_repetidos)


resultado = ordenar_letras("entretenido")
print(resultado)  # Esto mostrará: ['d', 'e', 'i', 'n', 'o', 'r', 't']
"""



""" 
def cero_repetido(*args):
   i = 0
   while i < len(args) - 1:
       if args[i] == 0 and args[i + 1] == 0:
          return True
       i += 1
       return False

resultado = cero_repetido(5,6,1,0,0,9,3,5)
resultado2 = cero_repetido(6,0,5,1,0,3,0,1)
print(resultado)   
print(resultado2)
"""



def contar_primos(num):
    for numero in range(2, num + 1):  # Empezamos desde 2 (primer primo)
        es_primo = True
        
        # Verificamos si el número actual es primo
        for divisor in range(2, numero):
            if numero % divisor == 0:
                es_primo = False
                break
        
        if es_primo:
            print(numero)  # Solo imprimimos el número primo

contar_primos(25)  # Sin asignar a variable, solo ejecuta





