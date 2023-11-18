import pygame
import random
import math
import sys
import os
import button
from pygame.locals import *

def pausa_():
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
    menu_state = "pantalladevictoria"
    
    # Carga de imágenes y música
    lago = pygame.image.load("imagenes/Fondos/castillolago.png").convert_alpha()
    lago = pygame.transform.scale(lago, (Ancho, Alto))

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
        ganador_text = button.Button(200, 15, ganadortext, 1)

        #Función para revisar si el juego está pausado
        if game_paused == False:

            #Función para revisar el estado del menú
            #Estado del juego: En la pantalla principal
            if menu_state == "pantalladevictoria":
                screen.blit(lago, (0, 0))

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

pausa_()