from random import shuffle

#lista inicial
palitos = ['-', '--', '---', '----']



# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista



#pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')
    return int(intento)



#Comprobar el intento si es el 1,2,3,4 
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos')
        print(f"Te ha tocado el palito: {lista[intento - 1]}")
    elif lista[intento - 1] == '----':
        print("¡Felicidades! Has ganado un premio especial.")
    else:
        print("Esta vez te has librado, pero no te confíes")
        print(f"Te ha tocado el palito: {lista[intento - 1]}")
 

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)







