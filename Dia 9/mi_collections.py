from collections import namedtuple, Counter, defaultdict, deque

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.75, 68)
print(ariel)


lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
print(Counter(lista))

mi_diccionario = defaultdict(lambda: 'Valor no hallado')
mi_diccionario['edad'] = 44


lista_ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
ciudades = deque(lista_ciudades)
