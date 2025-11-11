from random import choice

def elegir_frase():
    palabras = ["python", "programacion", "funciones", "variables", "listas"]
    palabra_aleatoria = choice(palabras)
    return palabra_aleatoria

def reemplazar_letra(guiones, palabra_original):
    while True:
        letra = input("Ingresa una letra: ").lower()  # Agregar .lower()
        if len(letra) != 1:
            print("Por favor, ingresa solo una letra.")
            continue
        if not letra.isalpha():
            print("Solo se permiten letras.")
            continue
        break
    
    if letra in palabra_original:
        lista_guiones = list(guiones)
        for i in range(len(palabra_original)):
            if palabra_original[i] == letra:
                lista_guiones[i] = letra
        nuevo_guion = "".join(lista_guiones)
        return nuevo_guion, letra, True 
    else:
        print("La letra no está en la frase.")
        return guiones, letra, False  

# Generar la palabra una sola vez
palabra = elegir_frase()
guiones_resultado = "_" * len(palabra)
print(f"Adivina la palabra: {guiones_resultado}")

# Loop para múltiples intentos
intentos_fallidos = 0
max_errores = 6
letras_fallidas = []

while intentos_fallidos < max_errores and "_" in guiones_resultado:
    guiones_anterior = guiones_resultado
    guiones_resultado, letra, acerto = reemplazar_letra(guiones_resultado, palabra)
    print(f"Resultado: {guiones_resultado}")
    
    if not acerto:
        intentos_fallidos += 1
        letras_fallidas.append(letra)
        print(f"Te quedan {max_errores - intentos_fallidos} errores")
        print(f"❌ Letras fallidas: {', '.join(letras_fallidas)}")
    else:
        print("¡Bien! No pierdes intentos")
    
    # Verificar si ganó
    if "_" not in guiones_resultado:
        print("¡Felicidades! ¡Adivinaste la palabra!")
        break

if "_" in guiones_resultado:
    print(f"¡Perdiste! La palabra era: {palabra}")