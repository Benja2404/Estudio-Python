import re
'''
texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas de servicio de ayuda online' 

patron = 'ayuda'

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
    '''

texto = 'no atendemos los lunes en la tarde'

buscar = re.search(r'lunes|martes', texto)
print(buscar.span())  # Saída: <re.Match object; span=(11, 17), match='lunes'>
