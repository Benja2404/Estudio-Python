cliente = {'nombre': 'Benjamin', 'edad': 22, 'ocupacion': 'Estudiante'}
pelicula = {'titulo': 'Matrix', 'ficha_tecnica':{'protagonista': 'Keanu Reeves', 'director': 'Lana y Lilly Wachowski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case{
            'nombre':nombre,
            'edad':edad,
            'ocupacion':ocupacion
        }:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case{
            'titulo': titulo,
            'ficha_tecnica':{
                'protagonista': protagonista,
                'director': director
            }
        }:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("Es un elemento desconocido")
