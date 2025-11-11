from tkinter import *

operador = ''


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador 
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''




def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
# iniciar tkinter

app = Tk()


# tamaño de la ventana
app.geometry('1020x630+0+0')

# evitar maximizar 
app.resizable(False,False)


# Titulo de la ventana
app.title('Mi Restaurante- Sistema de Facturación')

#color fondo de la ventana
app.config(bg='burlywood')

# Panel superior
panel_superior = Frame(app, bd=1, relief=FLAT)
panel_superior.pack(side=TOP, fill='x')

# etiqueta titulo (sin width y ocupando el ancho)
etiqueta_titulo = Label(
    panel_superior,
    text="Sistema de Facturacion",
    fg='azure4',
    font=('Dosis', 58),
    bg='burlywood'
)
etiqueta_titulo.pack(fill='x')


# Panel Izquierdo

panel_izquierdo = Frame(app, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT, fill='both', expand=True)

#panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_costos.pack(side=BOTTOM)


#panel comidas 
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(app, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT, fill='both', expand=True)  


#panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack(fill='x', padx=10, pady=10)

# columnas/filas elásticas de la calculadora
for i in range(4):
    panel_calculadora.grid_columnconfigure(i, weight=1, uniform='calc')
for r in range(1, 5):
    panel_calculadora.grid_rowconfigure(r, weight=1)

#panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack(fill='both', expand=True, padx=10, pady=(0,10)) 

# permitir que el contenido del recibo expanda
panel_recibo.grid_columnconfigure(0, weight=1)
panel_recibo.grid_rowconfigure(0, weight=1)

#panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack(fill='x', padx=10, pady=10)


# lista de productos
lista_comidas = ['Pollo', 'Cerdo', 'Tacos', 'merluza', 'Pizza1', 'Pizza2', 'Pizza3']
lista_bebidas = ['Agua', 'Soda', 'Jugo', 'Vino', 'Cerveza', 'Pisco', 'Gin']
lista_postres = ['Helado', 'Fruta', 'Brownie', 'Flan', 'Mousse', 'Pastel1', 'Pastel2', 'Pastel3']

#Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    # crear los check button
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                         text=comida.title(), 
                         font=('Dosis',19,'bold'),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador, 
                column=0, 
                sticky=W)

    # crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    
    cuadros_comida[contador].grid(row=contador,
                                  column=1)


    contador +=1



# Generar items bebidas
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis',19,'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebida[contador], command=revisar_check)
    bebida.grid(row=contador, column=0, sticky=W)

    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    
    contador +=1

# Generar items postres
variables_postres = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis',19,'bold'),
                         onvalue=1, offvalue=0, variable=variables_postres[contador], command=revisar_check)
    postre.grid(row=contador, column=0, sticky=W)

    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    
    cuadros_postre[contador].grid(row=contador,
                                  column=1)
    
    contador +=1


#variables 
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


# Etiqueta de costo y campos de entrada

etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_comida.grid(row=0,column=0)
texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# Bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_bebida.grid(row=1,column=0)
texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)


# Postre
etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_postre.grid(row=2,column=0)
texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# subtotal
etiqueta_subtotal = Label(panel_costos,
                              text='SubTotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_subtotal.grid(row=0,column=2)
texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

#Impuestos
etiqueta_impuesto = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_impuesto.grid(row=1,column=2)
texto_impuesto = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

# Total
etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_total.grid(row=2,column=2)
texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)



# botones
botones = ['total', 'recibo', 'guardar', 'resetear']
for i in range(4):
    panel_botones.grid_columnconfigure(i, weight=1)
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    boton.grid(row=0, column=columnas, sticky='ew', padx=5, pady=2)
    columnas += 1

# area de recibo 
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)



# Calculadora

visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          bd=1)

visor_calculadora.grid(row=0, column=0, columnspan=4, sticky='ew', padx=2, pady=2)
botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'R', 'B', '0', '/']
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1)
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna, sticky='nsew', padx=2, pady=2)
    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))




# Evitar que la ventana se cierre
app.mainloop()

