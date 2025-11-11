##mi_tuple = (1,2,(10,20),4)
#mi_tuple = list(mi_tuple)  # Convierte el tuple a una lista para poder modificarlo
# mi_tuple[0] = 5 # Esto causará un error porque los tuples son inmutables
#print(mi_tuple[0])  # Imprime el primer elemento del tuple
#print(mi_tuple[2]) # Imprime el tercer elemento del tuple, que es otro tuple
#print(mi_tuple[2][0])  # Imprime el primer elemento del tercer elemento del tuple
#print(type(mi_tuple))  # Imprime el tipo de mi_tuple, que ahora es una lista

####
t = (1,2,3,1)

# x,y,z= t  # Desempaquetado de tuplas
#print(x,y,z)  
#print(len(t))  # Imprime la longitud de la tupla
print(t.count(1))  # Cuenta cuántas veces aparece el número 1 en la tupla
print(t.index(2))  # Encuentra el índice del primer elemento que es igual a 2

