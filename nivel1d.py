import pygame
import random
import math
import sys
import os
import button
from pygame.locals import *

def nivel1dificil_():
    pygame.init()
    
    #Paleta de colores en formato RGB
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    ROJO = (255, 0, 0)
    VERDE = (0, 255, 0)

    #aqui configuras el ancho de la pantalla
    Ancho, Alto = 1200, 680
    screen = pygame.display.set_mode((Ancho, Alto))

    # Títulos de juego
    pygame.display.set_caption('Fishing Road')
    icono = pygame.image.load("imagenes/iconopesca.png")
    pygame.display.set_icon(icono)


    # Carga de imágenes y música
    lago = pygame.image.load("imagenes/Fondos/castillolago.png").convert_alpha()
    lago = pygame.transform.scale(lago, (Ancho, Alto))

    #botones en pausa
    restart_imagen = pygame.image.load('imagenes/Botones/botonrestart.png').convert_alpha()
    home_imagen = pygame.image.load('imagenes/Botones/pantallaprincipal.png').convert_alpha()
    botonnomute_imagen = pygame.image.load('imagenes/Botones/boton_nomuted.png').convert_alpha()
    botonmute_imagen = pygame.image.load('imagenes/Botones/boton_muted.png').convert_alpha()
    botonpausa_imagen = pygame.image.load('imagenes/Botones/botonpausa.png').convert_alpha()

    #botones al ganar
    siguientenivel_imagen = pygame.image.load('imagenes/Botones/siguientenivel.png').convert_alpha()
    home_imagen = pygame.image.load('imagenes/Botones/pantallaprincipal.png').convert_alpha()
    restart_imagen = pygame.image.load('imagenes/Botones/botonrestart.png').convert_alpha()

    #botones declarados
    botonpausa_img = button.Button(1130, 10, botonpausa_imagen, 1)
    #restart_img = pygame.tranform.scale(restart_imagen, (60, 60))

    #Colocar musica
    pygame.mixer.music.load('musica/sonidodenivel1.mp3')
    pygame.mixer.music.play(-1)

    #Cargar las imagenes del jugador
    jugadors1 = pygame.image.load('imagenes/Personaje/caballerod.png').convert_alpha()
    jugadors2 = pygame.image.load('imagenes/Personaje/caballeroi.png').convert_alpha()

    run = True
    while True:
        jugadorX = 10
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
        health_bar = HealthBar(10, 100, 300, 10, 4000)
        health_bar.hp = 100

        #Arpon
        arpon = pygame.image.load('imagenes/Personaje/arpon.png').convert_alpha()
        arponX=20
        arponY=-50
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

        for i in range(2):  # Crear 10 basuras
            basuras.append({
            'x': random.randint(100, 700),
            'x':100,
            'y': random.randint(100, 850),
            'y':700,
            'x_change': 2,
            'y_change': 0.2,
            'img': basuras_a
        })
            basuras.append({
            'x': random.randint(200, 700),
            'x':200,
            #'y': random.randint(390, 290),
            'y':700,
            'x_change': 2,
            'y_change': 0.2,
            'img': basuras_b
            })
            basuras.append({
            'x': random.randint(300, 700),
            'x':300,
            #'y': random.randint(390, 290),
            'y':700,
            'x_change': 2,
            'y_change': 0.2,
            'img': basuras_c
            })
            basuras.append({
            'x': random.randint(400, 700),
            'x':400,
            #'y': random.randint(390, 290),
            'y':700,
            'x_change': 2,
            'y_change': 0.2,
            'img': basuras_d
            })
            basuras.append({
            'x': random.randint(500, 700),
            'x':500,
            #'y': random.randint(390, 290),
            'y':700,
            'x_change': 2,
            'y_change': 0.2,
            'img': basuras_f
            })

            #inicio de bucle
        game_pause = False
        menu_state = "nivel1"
        
        running = True  
        while running:

            if game_pause == False:
                if menu_state == "nivel1":
                    #screen.fill((255,255,255))
                    screen.blit(lago, (0, 0))

                    if botonpausa_img.draw(screen):
                        print("hola mundo")
                        pause()
                        
                    #restart_img = button.Button(270, 30, restart_imagen, 1)

                    # Eventos
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                        #elif event.type == pygame.VIDEORESIZE:
                            #ANCHO, ALTO = event.w, event.h
                            #screen = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                jugadorx_change = -3
                                jugadors3 = jugadors2
                                arponX = jugadorX+40
                                arponlimit = 100
                                #screen.blit(jugadors, (jugadorX, jugadorY))
                            elif event.key == pygame.K_RIGHT:
                                jugadorx_change = 3
                                jugadors3 = jugadors1
                                arponX = jugadorX+10
                            elif event.key == pygame.K_DOWN:
                                arpony_change = 2
                        elif event.type == pygame.KEYUP:
                            jugadorx_change = 0
                            if event.key == pygame.K_DOWN:
                                arpony_change = -2

                        #Mover jugador
                    jugadorX += jugadorx_change
                    jugadorX = max(-10, min(jugadorX, 1100))  # Asegurate de que el jugador no salga de la pantalla
                        
                    #Mover arponX
                    arponX += jugadorx_change
                    arponX = max(25, min(arponX, 1110))

                    #Mover arponY
                    arponY += arpony_change
                    arponY= max(290, min(arponY, 620))
                    
                    #Mostrar jugador
                    screen.blit(jugadors3, (jugadorX, jugadorY))

                    #Mostrar arpón en pantalla
                    screen.blit(arpon, (arponX, arponY))

                    #Mostrar y mover basuras
                    for basura in basuras:
                        screen.blit(basura['img'], (basura['x'], basura['y']))
                        basura['x'] += basura['x_change']
                        #basura['y'] += basura['y_change']
                        if str(basura['img'])=="<Surface(64x64x32 SW)>":
                            imgin=64
                        else:
                            imgin=32
                        if (basura['y']>=arponY and basura['y']<=arponY+70) and ((basura['x']>=arponX and basura['x']<=arponX+70)or(basura['x']+imgin>=arponX and basura['x']+imgin<=arponX+70)):
                            score+=1
                            basura['y']=390
                            basura['x'] = random.randint(250, 700)

                        # Si la basura sale de la pantalla, reinicia su posición
                        if basura['x'] > 1000:
                            basura['y'] = random.randint(390, 620)
                            basura['x'] = random.randint(10, 20)
                        
                        # Mostrar puntuación
                    score_value = myfont.render("Score: " + str(score), True, (NEGRO))
                    screen.blit(score_value, (145, 55))

                    #Mostrar Tiempo
                    health_bar.draw(screen)

                    #Mostrar level1
                    level1_rec = pygame.image.load('imagenes/level1.png').convert_alpha()
                    screen.blit(level1_rec, (520,10))
                    objetivo1 = pygame.image.load('imagenes/objetivo1.png').convert_alpha()
                    screen.blit(objetivo1, (10,10))
                    puntuacion = pygame.image.load('imagenes/puntuacion.png').convert_alpha()
                    screen.blit(puntuacion, (10,50))
                    #Decremento
                    health_bar.hp -= 1

                    #Youwin dectecta
                    if score == 5:
                        youwin = True

                    if youwin == True:
                        victory()

                    #gameover detecta
                    if health_bar.hp == 0:
                        gameover = True

                    if gameover == True:
                        running = False
                        defeat()

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
    pygame.display.set_caption("Victory screen")

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
        home_imagen = pygame.image.load('imagenes/Botones/pantallaprincipal.png').convert_alpha()
        ganadordraw = pygame.image.load("imagenes/Victoria/ganadordraw.png").convert_alpha()
        ganadortext = pygame.image.load("imagenes/Victoria/ganadortext.png").convert_alpha()
        siguientenivel_imagen = pygame.image.load('imagenes/Botones/siguientenivel.png').convert_alpha()
        home_imagen = pygame.image.load('imagenes/Botones/pantallaprincipal.png').convert_alpha()
        restart_imagen = pygame.image.load('imagenes/Botones/botonrestart.png').convert_alpha()

        #Funcion para darle uso al boton después de definirlo
        home_button1 = button.Button(10, 130, home_imagen, 1)
        ganador_text = button.Button(200, 15, ganadortext, 1)
        ganador_draw = button.Button(460, 270, ganadordraw, 1)
        #siguientenivel_boton = button.Button(10, 450, siguientenivel_imagen, 1)
        restart_boton = button.Button(10, 290, restart_imagen, 1)

        lago = pygame.image.load("imagenes/Fondos/castillolago.png").convert_alpha()
        lago = pygame.transform.scale(lago, (SCREEN_WIDTH, SCREEN_HEIGHT))

        #Función para revisar si el juego está pausado
        if game_paused == False:

            #Función para revisar el estado del menú
            #Estado del juego: En la pantalla principal
            if menu_state == "pantalladevictoria":
                screen.blit(lago, (0, 0))

            if ganador_text.draw(screen):
                print("Ganador texto")
            if ganador_draw.draw(screen):
                print("Ganador imagen")
            #if siguientenivel_boton.draw(screen):
                #print("Siguiente nivel")
            if restart_boton.draw(screen):
                print("Restart boton")
                from nivel1d import nivel1dificil_
                nivel1dificil_()

                #Regresar al home en caso de presionar
            if home_button1.draw(screen):
                from main import main
                main()

            #Función para procesar los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            #Actualizamos los cambios realizados en la pantalla
            pygame.display.update()
        
def defeat():
    # Inicializa Pygame
    pygame.init()

    # Crea una ventana de 640x480 píxeles con el título "Mi ventana"
    SCREEN_HEIGHT = 680
    SCREEN_WIDTH = 1200

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Defeat screen")

    # Paleta de colores en formato RGB
    BLANCO = (255, 255, 255)
    BLANCOOS = (255, 255, 250)
    NEGRO = (0, 0, 0)
    ROJO = (255, 0, 0)
    VERDE = (0, 255, 0)
    AZUL = (0, 0, 255)

    pygame.mixer.music.load('musica/gameover.mp3')
    pygame.mixer.music.play()

    # Icono y título
    pygame.display.set_caption('Fishing Road')
    icono = pygame.image.load("imagenes/iconopesca.png")
    pygame.display.set_icon(icono)

    game_paused = False
    menu_state = "pantalladederrota"

    #def winner_():

    run = True
    while run:
        #Cargamos las imagenes desarrolladas
        gameoverdraw = pygame.image.load("imagenes/Derrota/gameoverdraw.png").convert_alpha()
        gameovertext = pygame.image.load("imagenes/Derrota/gameovertext.png").convert_alpha()
        home_imagen = pygame.image.load('imagenes/Botones/pantallaprincipal.png').convert_alpha()
        restart_imagen = pygame.image.load('imagenes/Botones/botonrestart.png').convert_alpha()

        #Funcion para darle uso al boton después de definirlo
        home_button1 = button.Button(10, 130, home_imagen, 1)
        defeat_text = button.Button(200, 50, gameovertext, 1)
        defeat_draw = button.Button(490, 310, gameoverdraw, 1)
        restart_boton = button.Button(10, 290, restart_imagen, 1)

        lago = pygame.image.load("imagenes/Fondos/castillolago.png").convert_alpha()
        lago = pygame.transform.scale(lago, (SCREEN_WIDTH, SCREEN_HEIGHT))

        #Función para revisar si el juego está pausado
        if game_paused == False:

            #Función para revisar el estado del menú
            #Estado del juego: En la pantalla principal
            if menu_state == "pantalladederrota":
                screen.blit(lago, (0, 0))

            if defeat_text.draw(screen):
                print("Ganador texto")
            if defeat_draw.draw(screen):
                print("Ganador imagen")
            if restart_boton.draw(screen):
                print("Restart boton")
                from nivel1d import nivel1dificil_
                nivel1dificil_()

                #Regresar al home en caso de presionar
            if home_button1.draw(screen):
                from main import main
                main()

            #Función para procesar los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            #Actualizamos los cambios realizados en la pantalla
            pygame.display.update()
        
def pause():
    # Inicializa Pygame
    pygame.init()

    # Crea una ventana de 640x480 píxeles con el título "Mi ventana"
    Alto = 680
    Ancho = 1200

    screen = pygame.display.set_mode((Ancho, Alto))
    pygame.display.set_caption("Pause screen")

    #pygame.mixer.music.load('musica/win.mp3')
    #pygame.mixer.music.play()

    # Icono y título
    pygame.display.set_caption('Fishing Road')
    icono = pygame.image.load("imagenes/iconopesca.png")
    pygame.display.set_icon(icono)

    game_paused = False
    menu_state = "fondopausa"
    
    # Carga de imágenes y música
    lago = pygame.image.load("imagenes/Fondos/castillolago.png").convert_alpha()
    lago = pygame.transform.scale(lago, (Ancho, Alto))

    run = True
    while run:
        #Cargamos las imagenes desarrolladas
        home_imagen = pygame.image.load('imagenes/Botones/pantallaprincipal1.png').convert_alpha()
        botonnomute_imagen = pygame.image.load('imagenes/Botones/boton_nomuted.png').convert_alpha()
        botonmute_imagen = pygame.image.load('imagenes/Botones/boton_muted.png').convert_alpha()
        fondopausa_img = pygame.image.load('imagenes/Botones/gamepaused.png').convert_alpha()
        restart_imagen = pygame.image.load('imagenes/Botones/botonrestart1.png').convert_alpha()

        #Funcion para darle uso al boton después de definirlo
        home_button1 = button.Button(500, 400, home_imagen, 1)
        botonson_button = button.Button(700, 300, botonnomute_imagen, 1)
        botonnoson_button = button.Button(325, 300, botonmute_imagen, 1)
        fondopausa_image = button.Button(210, 70, fondopausa_img, 1)
        restart_boton1 = button.Button(260, 400, restart_imagen, 1)

        #Función para revisar si el juego está pausado
        if game_paused == False:

            #Función para revisar el estado del menú
            #Estado del juego: En la pantalla principal
            if menu_state == "fondopausa":
                screen.blit(lago, (0, 0))

            if fondopausa_image.draw(screen):
                print("Ganador texto")
                #Regresar al home en caso de presionar
            
            if home_button1.draw(screen):
                from main import main
                main()
            
            if restart_boton1.draw(screen):
                nivel1dificil_()

            #Función para procesar los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            #Actualizamos los cambios realizados en la pantalla
            pygame.display.update()