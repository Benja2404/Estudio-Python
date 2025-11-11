def suma(*args):
    total = 0
    for arg in args:
        total += arg 
    return total

print(suma(5, 6, 5, 1, 10, 500))

def suma_cuadrados(*args):

    total = 0
    for n in args:
        total += n**2
    return total
    
print(suma_cuadrados(1,2,3))


def suma_absolutos(*args):
    suma = 0
    for n in args:
        absoluto = abs(n)
        suma += absoluto
    return suma
   
    
print(suma_absolutos(1,2,3,4,-5))




def numeros_persona(nombre, *args):
    suma_numeros = 0
    for n in args:
        suma_numeros += n
        return print(f"{nombre}, la suma de tus números es {suma_numeros}")


numeros_persona("Federico", 75,20,65)