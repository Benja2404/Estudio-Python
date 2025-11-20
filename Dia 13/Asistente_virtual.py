import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia



# Escuchar nuestro microfono y devolver audio via texto

def transformar_audio():
    # almacenar reconocedor en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8
        
        # informar que comenzo la grabacion
        print("ya puedes hablar")

        # guardar audio
        audio = r.listen(origen)

        try: 
            # buscar en google
            pedido = r.recognize_google(audio, language="es-cl")

            # pruebas de que pudo ingresar y transformar
            print("Dijiste: " + pedido)

            # devolver pedido 
            return pedido
        except sr.UnknownValueError:
            # prueba de que no comprendio audio 
            print("ups, no entendi")


            # devolver error

            return "Sigo esperando"

        # en caso de no poder resolver el pedido
        except sr.RequestError:
            
            print("ups, no hay servicio")

            return "Sigo esperando"
        # error inesperado
        except:
            print("ups, algo ha salido mal")

def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# informar dia de la semana
def pedir_dia():
    # variables
    dia = datetime.date.today()
    dia_semana = dia.weekday()
    
    # diccionario 
    dic = {0: "Lunes", 1: "Martes", 2: "Miercoles", 3: "Jueves", 4: "Viernes", 5: "Sabado", 6: "Domingo"}
    hablar(f"Hoy es {dic[dia_semana]}")

# informar que hora es 
def pedir_hora():
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos"
    # decir la hora
    hablar(hora)

def saludo():
    # crear variables con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif  6 <= hora.hour < 13:
        momento = "Buen dia"
    else: 
        momento = "Buenas tardes"
    hablar(f"{momento}, soy tuti tu polola hermosa. Porfavor dime en que te puedo ayudar")



def main():
    # saludar 
    saludo()

    comenzar = True

    # loop centrall
    while comenzar:
        # activar microfono y guardar el pedido en string
        pedido = transformar_audio().lower()
        if 'abrir youtube' in pedido:
            hablar('Con gusto estoy abriendo Youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro ahora abro google')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = (pedido.replace('wikipedia',''))
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'
                       } 
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontre, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdon no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break


main()
