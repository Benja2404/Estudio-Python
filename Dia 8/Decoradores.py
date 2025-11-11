def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adiós")
    return otra_funcion

@decorar_saludo
def mayusculas(palabra):
    print(palabra.upper())


@decorar_saludo
def minusculas(palabra):
    print(palabra.lower())



mayusculas("Python")