import bs4 
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html"

# lista de titulos con 4 a 5 estrellas
t4_5 = []


#iterar paginas
for pagina in range(1, 51):
    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado =  requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #seleccionar datos de los libros
    libros = sopa.select('.product_pod')
    
    #iterar libros
    for libro in libros:
        #chequear que tenga 4 o 5 estrellas
        if  len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            #Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']
            #agregar libro a la lista
            t4_5.append(titulo_libro)

for t in t4_5:
    print(t)
