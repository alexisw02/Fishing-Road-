import pygame

def gameover():
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


    gameoverdraw = pygame.image.load("imagenes/Derrota/gameoverdraw.png").convert_alpha()
    gameovertext = pygame.image.load("imagenes/Derrota/gameovertext.png").convert_alpha()

    pygame.mixer.music.load('musica/gameover.mp3')
    pygame.mixer.music.play()
    # Icono y título
    pygame.display.set_caption('Fishing Road')
    icono = pygame.image.load("imagenes/iconopesca.png")
    pygame.display.set_icon(icono)

    # Bucle principal del juego
    while True:
    #Obtiene los eventos del usuario
        eventos = pygame.event.get()
        
        screen.fill(BLANCOOS)
        screen.blit(gameoverdraw, (470, 270))
        screen.blit(gameovertext, (160, 100))
        # Comprueba si el usuario cerró la ventana
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        #Actualiza la pantalla
        pygame.display.update()

            #lago = pygame.image.load("imagenes/Fondos/fondorio.png").convert_alpha()
            #lago = pygame.transform.scale(lago, (Ancho, Alto))