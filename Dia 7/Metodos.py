class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    def piar(self):
        print("Pío, mi color es {}!".format(self.color))
    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")
        


piolin = Pajaro("amarillo", "canario")
piolin.piar()  # Salida: Pío, pío!
piolin.volar(100)  # Salida: El pájaro ha volado 100 metros.


