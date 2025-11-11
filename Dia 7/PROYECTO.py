class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class CLiente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    # metodo para imprimir cliente
    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}, Cuenta: {self.numero_cuenta}, Balance: ${self.balance}'

    #metodo para depositar en la cuenta
    def depositar(self, monto):
        self.balance += monto
        print(f'Depósito realizado: ${monto}. Nuevo balance: ${self.balance}')

    #metodo para retirar de la cuenta
    def retirar(self, monto):
        if monto > self.balance:
            print(f'Fondos insuficientes. No se pudo retirar: ${monto}')
        else:
            self.balance -= monto
            print(f'Retiro realizado: ${monto}. Nuevo balance: ${self.balance}')



def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su número de cuenta: ")
    cliente = CLiente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente

def main():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0
    while opcion != 'S':
        print("Elige: Depositar (D) , Retirar(R) o Salir(S)")
        opcion = input()
        if opcion == 'D':
            monto_dep = int(input("Ingrese el monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Ingrese el monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)
    print("Gracias por usar banco Python")


main()
