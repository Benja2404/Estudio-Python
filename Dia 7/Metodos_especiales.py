class CD:
    def __init__(self, autor, titulo, cantidad_canciones):
        self.autor = autor
        self.titulo = titulo
        self.cantidad_canciones = cantidad_canciones
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}."
    def __len__(self):
        return self.cantidad_canciones
    def __del__(self):
        print(f"El CD {self.titulo} ha sido eliminado.")


mi_cd = CD("Pink Floyd", "The Wall", 26)

def __str__(self):
        return f'"{self.titulo}", de {self.autor}'