'''
class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color


    def nacer(self):
        print("El animal ha nacido.")


    def hablar(self):
        print("El animal hace un sonido.")



class Pajaro(Animal):
    def __init__(self, edad,color,altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio pio")
    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")

piolin = Pajaro(2, "amarillo", 60)
mi_animal = Animal(5, "verde")

print(piolin)
'''




class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja ja ja")


class Hijo(Padre, Madre):
    pass



class Nieto(Hijo):
    pass




mi_nieto = Nieto()
mi_nieto.reir()