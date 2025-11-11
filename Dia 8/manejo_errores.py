def suma():
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))
    print("La suma es:", n1 + n2)
    print("gracias por sumar")




try:
    suma()
except TypeError:
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Debes ingresar un numero")
else:
    print("Hiciste todo bien")
finally:
    print("eso fue todo")



def pedir_numero():
    while True:
        try:
            numero = int(input("Ingresa un numero"))
        except:
            print("Ese no es un numero")
        else:
            print("Numero ingresado correctamente:", numero)
            break
    print("Gracias por usar el programa")

pedir_numero()