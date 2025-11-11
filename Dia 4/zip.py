nombres = ['Juan', 'Ana', 'Pedro']
edades = [25, 30, 22]
ciudades = ['Madrid', 'Barcelona', 'Valencia']

combinados = list(zip(nombres, edades, ciudades))
for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")