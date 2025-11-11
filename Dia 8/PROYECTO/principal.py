import numeros 


def preguntar():
    print("\n Bienvenido a la farmacia, en que sector desea tomar numero?:")
    while True:
        print("Si desea Perfumeria, oprima P")
        print("Si desea Farmacia, oprima F")
        print("Si desea Cosmetica, oprima C")
        try:
            opcion = input("Seleccione una opcion: ").upper()
            ["P", "F", "C"].index(opcion)
        except ValueError:
            print("Opcion invalida. Intente de nuevo.")
        else:
            break
    numeros.decorador(opcion)


def main():
    while True:
        preguntar()
        try: 
            otro_turno = input("\nDesea tomar otro numero? (S/N): ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Opcion invalida. Intente de nuevo.")
        else:
            if otro_turno == "N":
                print("Gracias por su visita.")
                break
            

main()
                
