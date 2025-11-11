#Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.


def cantidad_pares(lista):
    par = 0
    for n in lista:
        if n % 2 == 0:
            par += 1
    return par

lista_numeros = [1, 50, 502, 755, 34]
print(cantidad_pares(lista_numeros))
