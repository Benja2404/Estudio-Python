class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    def piar(self):
        print("Pío, mi color es {}!".format(self.color))
    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")
        self.piar()
    def pintar_negro(self):
        self.color = "negro"
        print(f"ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"El pájaro ha puesto {cantidad} huevos.")

    @staticmethod
    def mirar():
        print("El pájaro está mirando alrededor.")

Pajaro.poner_huevos(3)




class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = 10  
    
    def lanzar_flecha(self):  
        self.cantidad_flechas -= 1  
        print(f"Flechas restantes: {self.cantidad_flechas}")

