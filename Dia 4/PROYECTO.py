from random import *
intentos = 0
m = 0
nombre = input("Ingrese tu nombre: ")
n = randint(1, 100)

print(f"Bueno {nombre} He pensado en un numero entre el 1 al 100 y quiero que lo adivines" )
while intentos < 8:
    m = int(input("Cual es el numero? "))
    intentos += 1
    if m < 1 or m > 100:
        print("El número debe estar entre 1 y 100.")
    if m > n:
        print("Has elegido un numero mayor que el que he pensado.")
    if m < n:
        print("Has elegido un numero menor que el que he pensado.")
    if m == n:
        print(f"¡Felicidades {nombre}! Has acertado el número secreto {n} en {0 + intentos} intentos.")
        break

if m != n:
    print(f"Lo siento {nombre}, has agotado tus 8 intentos. El número era {n}.")
    print("¡Inténtalo de nuevo!")
  
