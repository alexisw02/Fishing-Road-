import pygame
import random
import math
import sys
import os
import button
from pygame.locals import *

def nivel2facil_():
    pygame.init()

    #aqui configuras el ancho de la pantalla
    Ancho, Alto = 1200, 680
    screen = pygame.display.set_mode((Ancho, Alto))

    # Títulos de juego
    pygame.display.set_caption('Fishing Road')
    icono = pygame.image.load("imagenes/iconopesca.png")
    pygame.display.set_icon(icono)


    # Carga de imágenes y música
    lago = pygame.image.load("imagenes/Fondos/fondorio.png").convert_alpha()
    lago = pygame.transform.scale(lago, (Ancho, Alto))

    pygame.mixer.music.load('musica/sonidodenivel1.mp3')
    pygame.mixer.music.play(-1)

    # Jugador
    jugadors1 = pygame.image.load('imagenes/Personaje/caballerod.png').convert_alpha()
    jugadors2 = pygame.image.load('imagenes/Personaje/caballeroi.png').convert_alpha()


    run = True
    while True:
        jugadorX = 50
        jugadorY = 215
        jugadorx_change = 0
        jugadors3=jugadors1

        gameover=False
        youwin=False

        # Puntuación
        score = 0
        myfont = pygame.font.Font(None, 32)  # Utilizando una fuente predeterminada

        #Tiempo
        class HealthBar():
                def __init__(self, x, y, w, h, max_hp):
                    self.x = x
                    self.y = y
                    self.w = w
                    self.h = h
                    self.hp = max_hp
                    self.max_hp = max_hp

                def draw(self, surface):
                    #calculate health ratio
                    ratio = self.hp / self.max_hp
                    pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
                    pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))
            
        #Barra de vida
        health_bar = HealthBar(10, 30, 300, 10, 4000)
        health_bar.hp = 4000

        #Arpon
        arpon = pygame.image.load('imagenes/Personaje/arpon.png').convert_alpha()
        arponX=20 #MODIFICAR A 20
        arponY=50 #MODIFICAR A 50
        arponlimit=28+0
        arpony_change=0

        #Peces
        '''class basura_a():
            def __init__(self, x, y, x_change, y_change):
                self.image = basuras_a
                self.x = x
                self.y = y
                self.x_change = x_change
                self.y_change = y_change

                def update(self):
                    self.y += self.y_change

                def draw(self, screen):
                    pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y))'''


        # Basura
        basuras_a = pygame.image.load('imagenes/Basura/jugo.png').convert_alpha()
        basuras_b = pygame.image.load('imagenes/Basura/BOLSA DE PAPAS.png').convert_alpha()
        basuras_c = pygame.image.load('imagenes/Basura/botella de agua1.png').convert_alpha()
        basuras_d = pygame.image.load('imagenes/Basura/LATA DE SODA.png').convert_alpha()
        basuras_f = pygame.image.load('imagenes/Basura/LLANTA.png').convert_alpha()
        basuras = []

        #for i in range(3):  # Crear 10 basuras
        basuras.append({
            'x': random.randint(100, 700),
            'x':100,
            'y': random.randint(100, 850),
            'y':700,
            'x_change': 0.2,
            'y_change': 0.2,
            'img': basuras_a
        })
        basuras.append({
            'x': random.randint(200, 700),
            'x':200,
            #'y': random.randint(390, 290),
            'y':700,
            'x_change': 0.2,
            'y_change': 0.2,
            'img': basuras_b
        })
        basuras.append({
            'x': random.randint(300, 700),
            'x':300,
            #'y': random.randint(390, 290),
            'y':700,
            'x_change': 0.2,
            'y_change': 0.2,
            'img': basuras_c
        })
        basuras.append({
            'x': random.randint(400, 700),
            'x':400,
            #'y': random.randint(390, 290),
            'y':700,
            'x_change': 0.2,
            'y_change': 0.2,
            'img': basuras_d
        })
        basuras.append({
            'x': random.randint(500, 700),
            'x':500,
            #'y': random.randint(390, 290),
            'y':700,
            'x_change': 0.2,
            'y_change': 0.2,
            'img': basuras_f
        })

            #inicio de bucle
        running = True  
        while running:
            screen.fill((255,255,255))
            screen.blit(lago, (0, 0))

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        jugadorx_change = -3
                        jugadors3 = jugadors2
                        arponX = jugadorX+40 #MODIFICAR A +40
                        arponlimit = 100
                        #screen.blit(jugadors, (jugadorX, jugadorY))
                    elif event.key == pygame.K_RIGHT:
                        jugadorx_change = 3
                        jugadors3 = jugadors1
                        arponX = jugadorX+10 #MODIFICAR A +10
                    elif event.key == pygame.K_DOWN:
                        arpony_change = 2
                elif event.type == pygame.KEYUP:
                    jugadorx_change = 0
                    if event.key == pygame.K_DOWN:
                        arpony_change = -2

                #Mover jugador
            jugadorX += jugadorx_change
            jugadorX = max(-10, min(jugadorX, 1100))  # Asegurate de que el jugador no salga de la pantalla
                        #MODIFICAR -10   #MODIFICAR 1100
            #Mover arponX
            arponX += jugadorx_change
            arponX = max(25, min(arponX, 1110))
                        #MODIFICAR 25, MODIFICAR 1110
            #Mover arponY
            arponY += arpony_change
            arponY= max(290, min(arponY, 620))
                        #MODIFICAR 290
            #Mostrar jugador
            screen.blit(jugadors3, (jugadorX, jugadorY))

            #Mostrar arpón en pantalla
            screen.blit(arpon, (arponX, arponY))

            #Mostrar y mover basuras
            for basura in basuras:
                screen.blit(basura['img'], (basura['x'], basura['y']))
                #basura['x'] += basura['x_change']
                basura['y'] += basura['y_change']
                if str(basura['img'])=="<Surface(64x64x32 SW)>":
                    imgin=64
                else:
                    imgin=32
                if (basura['y']>=arponY and basura['y']<=arponY+70) and ((basura['x']>=arponX and basura['x']<=arponX+70)or(basura['x']+imgin>=arponX and basura['x']+imgin<=arponX+70)):
                    score+=1
                    basura['y']=390
                    basura['x'] = random.randint(250, 700)

                # Si la basura sale de la pantalla, reinicia su posición
                if basura['y'] > Alto:
                    basura['y'] = 390
                    basura['x'] = random.randint(250, 700)
                
                # Mostrar puntuación
            score_value = myfont.render("Score: " + str(score), True, (255, 255, 255))
            screen.blit(score_value, (10, 10))

            #Mostrar Tiempo
            health_bar.draw(screen)

            #Mostrar level1
            level1_rec = pygame.image.load('imagenes/level1rec.png').convert_alpha()
            screen.blit(level1_rec, (520,10))

            #Decremento
            health_bar.hp -= 1

            #Youwin dectecta
            if score == 50:
                youwin = True

            if youwin == True:
                victory()

            #gameover detecta
            if health_bar.hp == 0:
                gameover = True

            if gameover == True:
                running = False
                from gameover import gameover
                gameover()

            pygame.display.update()
            pygame.time.Clock().tick(120)  #Fotogramas
        
            pygame.display.update()

def victory():
    # Inicializa Pygame
    pygame.init()

    # Crea una ventana de 640x480 píxeles con el título "Mi ventana"
    SCREEN_HEIGHT = 680
    SCREEN_WIDTH = 1200

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Main Menu")

    # Paleta de colores en formato RGB
    BLANCO = (255, 255, 255)
    BLANCOOS = (255, 255, 250)
    NEGRO = (0, 0, 0)
    ROJO = (255, 0, 0)
    VERDE = (0, 255, 0)
    AZUL = (0, 0, 255)

    pygame.mixer.music.load('musica/win.mp3')
    pygame.mixer.music.play()

    # Icono y título
    pygame.display.set_caption('Fishing Road')
    icono = pygame.image.load("imagenes/iconopesca.png")
    pygame.display.set_icon(icono)

    game_paused = False
    menu_state = "pantalladevictoria"

    #def winner_():

    run = True
    while run:
        #Cargamos las imagenes desarrolladas
        jugar_imagen = pygame.image.load("imagenes/Botones/botondeplay.png").convert_alpha()
        opciones_imagen = pygame.image.load("imagenes/Botones/botondeconfiguracion.png").convert_alpha()
        creditos_imagen = pygame.image.load("imagenes/Botones/botondecreditos.png").convert_alpha()
        salir_imagen = pygame.image.load("imagenes/Botones/botondesalir.png").convert_alpha()
        nivel1_imagen = pygame.image.load('imagenes/Botones/botonlvl1.png').convert_alpha()
        nivel2_imagen = pygame.image.load('imagenes/Botones/botonlvl2.png').convert_alpha()
        nivel3_imagen = pygame.image.load('imagenes/Botones/botonlvl3.png').convert_alpha()
        home_imagen = pygame.image.load('imagenes/Botones/pantallaprincipal.png').convert_alpha()
        regresar_imagen = pygame.image.load('imagenes/Botones/botonregresar.png').convert_alpha()
        avanzar_imagen = pygame.image.load('imagenes/Botones/botonavanzar.png').convert_alpha()
        botonnomute_imagen = pygame.image.load('imagenes/Botones/boton_nomuted.png').convert_alpha()
        botonmute_imagen = pygame.image.load('imagenes/Botones/boton_muted.png').convert_alpha()
        ganadordraw = pygame.image.load("imagenes/Victoria/ganadordraw.png").convert_alpha()
        ganadortext = pygame.image.load("imagenes/Victoria/ganadortext.png").convert_alpha()

        #Funcion para darle uso al boton después de definirlo
        jugar_button = button.Button(490, 270, jugar_imagen, 1)
        opciones_button = button.Button(390, 465, opciones_imagen, 1)
        creditos_button = button.Button(525, 465, creditos_imagen, 1)
        salir_button = button.Button(650, 470, salir_imagen, 1)
        nivel1_button = button.Button(250, 300, nivel1_imagen, 1)
        nivel2_button = button.Button(525, 300, nivel2_imagen, 1)
        nivel3_button = button.Button(800, 300, nivel3_imagen, 1)
        salir_button = button.Button(660, 465, salir_imagen, 1)
        home_button = button.Button(10, 10, home_imagen, 1)
        regresar_button = button.Button(10, 290, regresar_imagen, 1)
        avanzar_button = button.Button(1070, 290, avanzar_imagen, 1)
        botonson_button = button.Button(700, 300, botonnomute_imagen, 1)
        botonnoson_button = button.Button(325, 300, botonmute_imagen, 1)
        ganador_text = button.Button(300, 500, ganadortext, 1)

        #Función para revisar si el juego está pausado
        if game_paused == False:

            #Función para revisar el estado del menú
            #Estado del juego: En la pantalla principal
            if menu_state == "pantalladevictoria":
                screen.fill(BLANCOOS)
            if ganador_text.draw(screen):
                print("Ganador texto")
                #Regresar al home en caso de presionar
            if home_button.draw(screen):
                from main import main
                main()

            #Función para procesar los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            #Actualizamos los cambios realizados en la pantalla
            pygame.display.update()     