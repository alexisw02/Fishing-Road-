def main():
  #Función para añadir librerías
  import pygame
  import button
  import sys

  #Funcion para iniciar pygame
  pygame.init()

  #Funcion para especificar el tamaño de la ventana
  SCREEN_WIDTH = 1200
  SCREEN_HEIGHT = 680
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Main Menu")
  imagen_icono = pygame.image.load('imagenes/iconopesca.png')
  pygame.display.set_icon(imagen_icono)

  # Musica del juego
  pygame.mixer.music.load('musica/sonidodemenu.mp3')
  pygame.mixer.music.play(-1)

  #Variable del control del volumen
  musica_mute = False
  original_volume = 0.5

  #Variables del juego
  game_paused = False
  menu_state = "main"
  musica_silenciada = False

  #Definir fuentes
  font = pygame.font.SysFont("arialblack", 40)

  # Paleta de colores en formato RGB
  BLANCO = (255, 255, 255)
  NEGRO = (0, 0, 0)
  ROJO = (255, 0, 0)
  VERDE = (0, 255, 0)
  AZUL = (0, 0, 255)

  #Fondo del juego
  BG = pygame.image.load("imagenes/Fondos/fondo.png")
  BG = pygame.transform.scale(BG, (1200, 680))

  def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    
  #Bucle principal del juego

  #def main_():

  run = True
  while run:

      #Cargar el fondo en el bucle
      screen.blit(BG, (0,0))
      
      #Cargamos las imagenes desarrolladas
      jugar_imagen = pygame.image.load("imagenes/Botones/botondeplay.png").convert_alpha()
      opciones_imagen = pygame.image.load("imagenes/Botones/botondeconfiguracion.png").convert_alpha()
      creditos_imagen = pygame.image.load("imagenes/Botones/botondecreditos.png").convert_alpha()
      salir_imagen = pygame.image.load("imagenes/Botones/botondesalir.png").convert_alpha()
      video_imagen = pygame.image.load('imagenes/Botones/button_video.png').convert_alpha()
      audio_imagen = pygame.image.load('imagenes/Botones/button_audio.png').convert_alpha()
      llave_imagen = pygame.image.load('imagenes/Botones/button_keys.png').convert_alpha()
      regreso_imagen = pygame.image.load('imagenes/Botones/button_back.png').convert_alpha()
      nivel1_imagen = pygame.image.load('imagenes/Botones/botonlvl1.png').convert_alpha()
      nivel2_imagen = pygame.image.load('imagenes/Botones/botonlvl2.png').convert_alpha()
      nivel3_imagen = pygame.image.load('imagenes/Botones/botonlvl3.png').convert_alpha()
      home_imagen = pygame.image.load('imagenes/Botones/pantallaprincipal.png').convert_alpha()
      regresar_imagen = pygame.image.load('imagenes/Botones/botonregresar.png').convert_alpha()
      avanzar_imagen = pygame.image.load('imagenes/Botones/botonavanzar.png').convert_alpha()
      cp1 = pygame.image.load('imagenes/Comic/capitulo1.png').convert_alpha()
      cp2 = pygame.image.load('imagenes/Comic/capitulo2.png').convert_alpha()
      cp3 = pygame.image.load('imagenes/Comic/capitulo3.png').convert_alpha()
      cp4 = pygame.image.load('imagenes/Comic/capitulo4.png').convert_alpha()
      cp5 = pygame.image.load('imagenes/Comic/capitulo5.png').convert_alpha()
      cp6 = pygame.image.load('imagenes/Comic/capitulo6.png').convert_alpha()
      titulo1_imagen = pygame.image.load("imagenes/Titulo/fishing.png").convert_alpha()
      titulo2_imagen = pygame.image.load("imagenes/Titulo/road.png").convert_alpha()
      botonnomute_imagen = pygame.image.load('imagenes/Botones/boton_nomuted.png').convert_alpha()
      botonmute_imagen = pygame.image.load('imagenes/Botones/boton_muted.png').convert_alpha()
      botonmoverizq_imagen = pygame.image.load('imagenes/Botones/movizquierda.png').convert_alpha()
      botonmoverder_imagen = pygame.image.load('imagenes/Botones/movderecha.png').convert_alpha()
      botonbajar_imagen = pygame.image.load('imagenes/Botones/botonbajar.png').convert_alpha()
      botonconfigjugar_imagen = pygame.image.load('imagenes/Botones/botoncomojugar.png').convert_alpha()
      botonesc_imagen = pygame.image.load('imagenes/Botones/botonesc.png').convert_alpha()
      texthow_imagen = pygame.image.load('imagenes/Titulo/howtoplaytext.png').convert_alpha()
      textmove_imagen = pygame.image.load('imagenes/Titulo/movetext.png').convert_alpha()
      textthrow_imagen = pygame.image.load('imagenes/Titulo/throwtext.png').convert_alpha()
      texthook_imagen = pygame.image.load('imagenes/Titulo/hooktext.png').convert_alpha()
      textmenu_imagen = pygame.image.load('imagenes/Titulo/openmenutext.png').convert_alpha()

      #Funcion para darle uso al boton después de definirlo
      jugar_button = button.Button(490, 270, jugar_imagen, 1)
      opciones_button = button.Button(390, 465, opciones_imagen, 1)
      creditos_button = button.Button(525, 465, creditos_imagen, 1)
      salir_button = button.Button(650, 470, salir_imagen, 1)
      titulo1_button = button.Button(290, 30, titulo1_imagen, 1)
      titulo2_button = button.Button(420, 130, titulo2_imagen, 1)
      video_button = button.Button(426, 75, video_imagen, 1)
      audio_button = button.Button(425, 200, audio_imagen, 1)
      llave_button = button.Button(446, 325, llave_imagen, 1)
      regresar_button = button.Button(332, 450, regreso_imagen, 1)
      nivel1_button = button.Button(250, 300, nivel1_imagen, 1)
      nivel2_button = button.Button(525, 300, nivel2_imagen, 1)
      nivel3_button = button.Button(800, 300, nivel3_imagen, 1)
      salir_button = button.Button(660, 465, salir_imagen, 1)
      home_button = button.Button(10, 10, home_imagen, 1)
      regresar_button = button.Button(10, 290, regresar_imagen, 1)
      avanzar_button = button.Button(1070, 290, avanzar_imagen, 1)
      cp1_button = button.Button(165, 137, cp1, 1)
      cp2_button = button.Button(165, 137, cp2, 1)
      cp3_button = button.Button(305, 30, cp3, 1)
      cp4_button = button.Button(305, 30, cp4, 1)
      cp5_button = button.Button(305, 30, cp5, 1)
      cp6_button = button.Button(305, 30, cp6, 1)
      botonson_button = button.Button(700, 300, botonnomute_imagen, 1)
      botonnoson_button = button.Button(325, 300, botonmute_imagen, 1)
      botonconfigplay_button = button.Button(500, 330, botonconfigjugar_imagen, 1)
      botonmovizq_img = button.Button(100, 270, botonmoverizq_imagen, 1)
      botonmovder_img = button.Button(240, 270, botonmoverder_imagen, 1)
      botonbaj_img = button.Button(520, 350, botonbajar_imagen, 1)
      botonesc_img = button.Button(820, 270, botonesc_imagen, 1)
      texthow_img = button.Button(270, 30, texthow_imagen, 1)
      textmove_img = button.Button(105, 200, textmove_imagen, 1)
      throwtext_img = button.Button(330, 480, textthrow_imagen, 1)
      hooktext_img = button.Button(465, 550, texthook_imagen, 1)
      menutext_img = button.Button(630, 200, textmenu_imagen, 1)

      #Función para revisar si el juego está pausado
      if game_paused == False:

        #Función para revisar el estado del menú
        #Estado del juego: En la pantalla principal
        if menu_state == "main":

          #Introducción de los botones de la pantalla principal
          if titulo1_button.draw(screen):
            print("titulo1")
          if titulo2_button.draw(screen):
            print("titulo2")
          if jugar_button.draw(screen):
            menu_state = "jugar"
            if nivel1_button.draw(screen):
              menu_state = "nivel1"
          if opciones_button.draw(screen):
            menu_state = "opciones"
          if creditos_button.draw(screen):
            menu_state = "creditos"
          if salir_button.draw(screen):
            run = False
        
        #Funcion para obtener la posicion del mouse
        mouse_pos = pygame.mouse.get_pos()

        #Introducción de elementos en el botón de jugar
        #Estado del juego: En la pantalla jugar
        if menu_state == "jugar":
          screen.blit(BG, (0,0))

          if nivel1_button.draw(screen):
            print("Click a nivel 1")
            pygame.mixer.music.stop()
            from nivel1facil import nivel1_
            nivel1_()


          if nivel2_button.draw(screen):
            print("Click a nivel 2")
            pygame.mixer.music.stop()
            from nivel2 import nivel2
            nivel2()

          if nivel3_button.draw(screen):
            print("Inicio")
            #from nivel1 import nivel1
            #nivel1()

          if home_button.draw(screen):
            menu_state = "main"

        #Introducción de elementos en boton opciones
        #Estado del juego: En la pantalla opciones
        if menu_state == "opciones":
          screen.blit(BG, (0,0))

          #Se dibuja los botones del menú
          if botonson_button.draw(screen):
            print("botonmute")
          if botonnoson_button.draw(screen):
            print("botonmute")
          if botonconfigplay_button.draw(screen):
            menu_state = "opcionesjugar"
          if home_button.draw(screen):
            menu_state = "main"
        
        if menu_state == "opcionesjugar":
          screen.blit(BG, (0,0))
          if botonmovizq_img.draw(screen):
            print("botonmovizq")
          if botonmovder_img.draw(screen):
            print("botonmovder")
          if botonbaj_img.draw(screen):
            print("botonbaj")
          if botonesc_img.draw(screen):
            print("botonesc")
          if texthow_img.draw(screen):
            print("botonesc")
          if textmove_img.draw(screen):
            print("botonesc")
          if throwtext_img.draw(screen):
            print("botonesc")
          if hooktext_img.draw(screen):
            print("botonesc")
          if menutext_img.draw(screen):
            print("botonesc")
          if home_button.draw(screen):
            menu_state = "main"

        #Se dibujan los botones de los créditos
        #Estado del juego: En la pantalla créditos
        if menu_state == "creditos":
          screen.blit(BG, (0,0))
          if cp1_button.draw(screen):
            print("cp1")
          if avanzar_button.draw(screen):
            menu_state = "avanzar1"
          if home_button.draw(screen):
            menu_state = "main"
          
        #Estado del juego: En la pantalla avanzar1
        if menu_state == "avanzar1":
          screen.blit(BG, (0,0))
          if cp2_button.draw(screen):
            print("cp2")
          if avanzar_button.draw(screen):
            menu_state = "avanzar2"
          if regresar_button.draw(screen):
            menu_state = "creditos"
          if home_button.draw(screen):
            menu_state = "main"
        
        #Estado del juego: En la pantalla avanzar2
        if menu_state == "avanzar2":
          screen.blit(BG, (0,0))
          if cp3_button.draw(screen):
            print("cp3")
          if avanzar_button.draw(screen):
            menu_state = "avanzar3"
          if regresar_button.draw(screen):
            menu_state = "avanzar1"
          if home_button.draw(screen):
            menu_state = "main"

        #Estado del juego: En la pantalla avanzar3
        if menu_state == "avanzar3":
          screen.blit(BG, (0,0))
          if cp4_button.draw(screen):
            print("cp4")
          if avanzar_button.draw(screen):
            menu_state = "avanzar4"
          if regresar_button.draw(screen):
            menu_state = "avanzar2"
          if home_button.draw(screen):
            menu_state = "main"

        #Estado del juego: En la pantalla avanzar4
        if menu_state == "avanzar4":
          screen.blit(BG, (0,0))
          if cp5_button.draw(screen):
            print("cp5")
          if avanzar_button.draw(screen):
            menu_state = "avanzar5"
          if regresar_button.draw(screen):
            menu_state = "avanzar3"
          if home_button.draw(screen):
            menu_state = "main"

        #Estado del juego: En la pantalla avanzar5
        if menu_state == "avanzar5":
          screen.blit(BG, (0,0))
          if cp6_button.draw(screen):
            print("cp6")
          if regresar_button.draw(screen):
            menu_state = "avanzar4"
          if home_button.draw(screen):
            menu_state = "main"

          #Si se presiona el boton regresa a la pantalla principal
          if home_button.draw(screen):
            menu_state = "main"


      #Función para procesar los eventos
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        
        #Funcion para pausar y despausar la música
        elif event.type == pygame.MOUSEBUTTONDOWN:
              if botonnoson_button.rect.collidepoint(event.pos):
                pygame.mixer.music.pause()
                musica_silenciada = True
              elif botonson_button.rect.collidepoint(event.pos):
                pygame.mixer.music.unpause()
                musica_pausada = False

      #Actualizamos los cambios realizados en la pantalla
      pygame.display.update()
  pygame.quit()
main()