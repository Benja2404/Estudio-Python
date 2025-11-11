texto = input("Escribe un texto: ")
texto.lower()

print("\n")
letras1 = input("Escribe 1 letra: ")
letras2 = input("Escribe otra letra: ")
letras3 = input("Escribe otra letra: ")
cantidad1 = texto.count(letras1) 
cantidad2 = texto.count(letras2)
cantidad3 = texto.count(letras3)

print("\n")
print("CANTIDAD DE LETRAS")
print(f"Hemos encontrado la letra '{letras1}' {cantidad1} veces.")
print(f"Hemos encontrado la letra '{letras2}' {cantidad2} veces. ")
print(f"Hemos encontrado la letra '{letras3}' {cantidad3} veces.")

print("\n")
print("LONGITUD DEL TEXTO")
palabras = texto.split()
print(f"Hemos encontrado la cantidad de {len(palabras)} palabras en tu texto.")

print("\n")
print("PRIMERA Y ÚLTIMA LETRA")
primera = texto[0]

ultima = texto[-1]
print(f"La letra inicial es '{primera}' y la letra final es '{ultima}'.")

print("\n")
print("TEXTO AL REVÉS")
palabras.reverse()
alrevez = ' '.join(palabras)
print(f"El texto al revés es: {alrevez}")

print("\n")
print("VERIFICANDO SI 'python' ESTÁ EN EL TEXTO")
python = "python" in texto or "Python" in texto
if python == True:
    print("¡La palabra 'python' está en el texto!")
else:
    print("La palabra 'python' no está en el texto.")



