import pygame
import random
import math
from pygame import mixer
# Inicializar pygame
pygame.init()





# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("Dia 10/aterrizaje-de-ovni (1).png")
pygame.display.set_icon(icono)  # Establecer el icono de la ventana
fondo = pygame.image.load("Dia 10/fondo.jpg")



# Musica 
mixer.music.load("Dia 10/MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)


# Efectos de sonido




# Jugador 
img_jugador = pygame.image.load("Dia 10/cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0


# Enemigo 
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 6

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("Dia 10/enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)
    
# Variables de la Bala
img_bala = pygame.image.load("Dia 10/bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

# puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# Funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# texto final 
fuente_final = pygame.font.Font('freesansbold.ttf', 40)
def texto_final():
    texto_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(texto_final, (60, 200))



# Funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))

# Funcion enemigo 
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene], (x,y))

# Funcion disparo de bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

# Funcion Detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False



# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    # Imagen de fondo
    pantalla.blit(fondo, (0, 0))
    for evento in pygame.event.get():

        # Cerrar el juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("Dia 10/Disparo.mp3") 
                sonido_bala.play() 
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
    
    # Actualizar la posición del jugador
    jugador_x += jugador_x_cambio

    # Mantener al jugador dentro de los límites de la pantalla
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736


    # Actualizar la posición del Enemigo
    for e in range(cantidad_enemigos):
        # Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break   

        enemigo_x[e] += enemigo_x_cambio[e]
        # Mantener al enemigo dentro de los límites de la pantalla
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]
         # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound("Dia 10/Golpe.mp3")
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        enemigo(enemigo_x[e], enemigo_y[e], e)
    
    # Movimiento de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

   

    # Llamar a las funciones del jugador y enemigo
    jugador(jugador_x, jugador_y)
   

    # Mostrar puntaje
    mostrar_puntaje(texto_x, texto_y)

    # Actualizar la pantalla
    pygame.display.update()







