#lista = ['a', 'b', 'c']

# for item in enumerate(lista):
   # print(item)

#lista = "Python"
#lista_indices = list(enumerate(lista))
#for index, item in lista_indices:
  #  print(index, item)

# Output:
# 0 Python


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)
    else:
        continue

    