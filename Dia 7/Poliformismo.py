class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " dice Muuu")


class Obeja:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " dice Beee")


vaca1 = Vaca('Aurora')
obeja1 = Obeja('nube')

animales = [vaca1, obeja1]
for animal in animales:
    animal.hablar()





    
    
