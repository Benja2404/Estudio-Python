
#Crear una funcion que cuente la cantidad de parametros que recibe y devuelva esa cantidad


def cantidad_atributos(**kwargs):
    return len(kwargs)


cantidad_atributos(x=10, y=15)



#Crear una funcion que devuelva en forma de lista los atributos que recibe en forma de clave (keywords) la funcion debe preveer recibir cualquier cantidad de argumentos de ese tipo
def lista_atributos(**kwargs):
    return list(kwargs.values())






def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
        
describir_persona("Maria", color_ojos="azules", color_pelo="rubio")

