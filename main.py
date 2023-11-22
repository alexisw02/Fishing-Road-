def main():
  #Función para añadir librerías
  import pygame
  import button
  #import sys

  #Funcion para iniciar pygame
  pygame.init()

  #Funcion para especificar el tamaño de la ventana
  SCREEN_WIDTH = 1200
  SCREEN_HEIGHT = 680
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Fishing Road")
  imagen_icono = pygame.image.load('imagenes/iconopesca.png')
  pygame.display.set_icon(imagen_icono)

  # Musica del juego
  pygame.mixer.music.load('musica/sonidodemenu.mp3')
  pygame.mixer.music.play(-1)

  #Variable del control del volumen
  #musica_mute = False
  #original_volume = 0.5

  #Variables del juego
  game_paused = False
  menu_state = "main"
  #musica_silenciada = False

  #Definir fuentes
  #font = pygame.font.SysFont("arialblack", 40)

  # Paleta de colores en formato RGB
  #BLANCO = (255, 255, 255)
  #NEGRO = (0, 0, 0)
  #ROJO = (255, 0, 0)
  #VERDE = (0, 255, 0)
  #AZUL = (0, 0, 255)

  #Fondo del juego
  BG = pygame.image.load("imagenes/Fondos/fondo.png")
  BG = pygame.transform.scale(BG, (1200, 680))

  #def draw_text(text, font, text_col, x, y):
    #img = font.render(text, True, text_col)
    #screen.blit(img, (x, y))
    
  #Bucle principal del juego
  run = True
  while run:

      #Cargar el fondo en el bucle
      screen.blit(BG, (0,0))
      
      #Cargamos las imagenes desarrolladas
      jugar_imagen = pygame.image.load("imagenes/Botones/botondeplay.png").convert_alpha()
      jugar1_imagen = pygame.image.load("imagenes/Botones/botondeplay1.png").convert_alpha()
      opciones_imagen = pygame.image.load("imagenes/Botones/botondeconfiguracion.png").convert_alpha()
      creditos_imagen = pygame.image.load("imagenes/Botones/botondecreditos.png").convert_alpha()
      salir_imagen = pygame.image.load("imagenes/Botones/botondesalir.png").convert_alpha()
      regreso_imagen = pygame.image.load('imagenes/Botones/button_back.png').convert_alpha()
      nivel1_imagen = pygame.image.load('imagenes/Botones/botonlvl1.png').convert_alpha()
      nivel2_imagen = pygame.image.load('imagenes/Botones/botonlvl2.png').convert_alpha()
      nivel3_imagen = pygame.image.load('imagenes/Botones/botonlvl3.png').convert_alpha()
      nivel1hard_imagen = pygame.image.load('imagenes/Botones/botonlvl1hard.png').convert_alpha()
      nivel2hard_imagen = pygame.image.load('imagenes/Botones/botonlvl2hard.png').convert_alpha()
      nivel3hard_imagen = pygame.image.load('imagenes/Botones/botonlvl3hard.png').convert_alpha()
      home_imagen = pygame.image.load('imagenes/Botones/pantallaprincipal.png').convert_alpha()
      regresar_imagen = pygame.image.load('imagenes/Botones/botonregresar.png').convert_alpha()
      regresarhard_imagen = pygame.image.load('imagenes/Botones/botonregresar1.png').convert_alpha()
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
      botoneasy_imagen = pygame.image.load('imagenes/Botones/botoneasy.png').convert_alpha()
      botondificil_imagen = pygame.image.load('imagenes/Botones/botonhard.png').convert_alpha()
      fondoobjetivos_imagen = pygame.image.load('imagenes/Fondos/objetivos.png').convert_alpha()
      timelvl1f_imagen = pygame.image.load('imagenes/timelvl1f.png').convert_alpha()
      objetivolvl1f_imagen = pygame.image.load('imagenes/objetivoslvl1f.png').convert_alpha()
      timelvl2m_imagen = pygame.image.load('imagenes/timelvl1m.png').convert_alpha()
      objetivolvl1m_imagen = pygame.image.load('imagenes/objetivoslvl1m.png').convert_alpha()
      timelvl1d_imagen = pygame.image.load('imagenes/timelvl1d.png').convert_alpha()
      objetivolvl1d_imagen = pygame.image.load('imagenes/objetivoslvl1d.png').convert_alpha()
      timelvl2f_imagen = pygame.image.load('imagenes/timelvl2f.png').convert_alpha()
      objetivolvl2f_imagen = pygame.image.load('imagenes/objetivoslvl2f.png').convert_alpha()
      timelvl2m_imagen = pygame.image.load('imagenes/timelvl2m.png').convert_alpha()
      objetivolvl2m_imagen = pygame.image.load('imagenes/objetivoslvl2m.png').convert_alpha()
      timelvl2d_imagen = pygame.image.load('imagenes/timelvl2d.png').convert_alpha()
      objetivolvl2d_imagen = pygame.image.load('imagenes/objetivoslvl2d.png').convert_alpha()
      fondoobjetivos_imagen = pygame.transform.scale(fondoobjetivos_imagen, (1200, 680))
      timelvl1f_imagen = pygame.image.load('imagenes/timelvl1f.png').convert_alpha()
      timelvl1m_imagen = pygame.image.load('imagenes/timelvl1m.png').convert_alpha()
      timelvl1d_imagen = pygame.image.load('imagenes/timelvl1d.png').convert_alpha()
      timelvl2f_imagen = pygame.image.load('imagenes/timelvl2f.png').convert_alpha()
      timelvl2m_imagen = pygame.image.load('imagenes/timelvl2m.png').convert_alpha()
      timelvl2d_imagen = pygame.image.load('imagenes/timelvl2d.png').convert_alpha()

      #Funcion para darle uso al boton después de definirlo
      jugar_button = button.Button(490, 270, jugar_imagen, 1)
      jugar1_button = button.Button(70, 50, jugar1_imagen, 1)
      opciones_button = button.Button(390, 465, opciones_imagen, 1)
      creditos_button = button.Button(525, 465, creditos_imagen, 1)
      #salir_button = button.Button(650, 470, salir_imagen, 1)
      titulo1_button = button.Button(290, 30, titulo1_imagen, 1)
      titulo2_button = button.Button(420, 130, titulo2_imagen, 1)
      regresar_button = button.Button(332, 450, regreso_imagen, 1)
      regresarhhard_button = button.Button(10, 550, regresarhard_imagen, 1)
      nivel1_button = button.Button(250, 300, nivel1_imagen, 1)
      nivel2_button = button.Button(525, 300, nivel2_imagen, 1)
      nivel3_button = button.Button(800, 300, nivel3_imagen, 1)
      nivel1hard_button = button.Button(250, 300, nivel1hard_imagen, 1)
      nivel2hard_button = button.Button(525, 300, nivel2hard_imagen, 1)
      nivel3hard_button = button.Button(800, 300, nivel3hard_imagen, 1)
      salir_button = button.Button(660, 465, salir_imagen, 1)
      home_button = button.Button(10, 10, home_imagen, 1)
      regresar_button = button.Button(10, 290, regresar_imagen, 1)
      regresar1_button = button.Button(10, 550, regresar_imagen, 1)
      avanzar_button = button.Button(1070, 290, avanzar_imagen, 1)
      cp1_button = button.Button(165, 137, cp1, 1)
      cp2_button = button.Button(165, 137, cp2, 1)
      cp3_button = button.Button(165, 137, cp3, 1)
      cp4_button = button.Button(165, 137, cp4, 1)
      cp5_button = button.Button(165, 137, cp5, 1)
      cp6_button = button.Button(165, 137, cp6, 1)
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
      botoneasy_button = button.Button(430, 170, botoneasy_imagen, 1)
      fondoobjetivos_img = button.Button(0, 0, fondoobjetivos_imagen, 1)
      botondificil_button = button.Button(430, 450, botondificil_imagen, 1)
      objetivolvl1facil_img = button.Button(100, 230, objetivolvl1f_imagen, 1)
      objetivolvl1medio_img = button.Button(60, 230, objetivolvl1m_imagen, 1)
      objetivolvl1dificil_img = button.Button(60, 230, objetivolvl1d_imagen, 1)
      objetivolvl2facil_img = button.Button(70, 230, objetivolvl2f_imagen, 1)
      objetivolvl2medio_img = button.Button(70, 230, objetivolvl2m_imagen, 1)
      objetivolvl2dificil_img = button.Button(70, 230, objetivolvl2m_imagen, 1)
      timelvl1f_imagen = button.Button(270, 470, timelvl1f_imagen, 1)
      timelvl1m_imagen = button.Button(270, 470, timelvl1m_imagen, 1)
      timelvl1d_imagen = button.Button(270, 470, timelvl1d_imagen, 1)
      timelvl2f_imagen = button.Button(270, 470, timelvl2f_imagen, 1)
      timelvl2m_imagen = button.Button(270, 470, timelvl2m_imagen, 1)
      timelvl2d_imagen = button.Button(270, 470, timelvl2d_imagen, 1)
      

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
            #if nivel1_button.draw(screen):
              #menu_state = "nivel1"
          if opciones_button.draw(screen):
            menu_state = "opciones"
          if creditos_button.draw(screen):
            menu_state = "creditos"
          if salir_button.draw(screen):
            run = False
        
        #Funcion para obtener la posicion del mouse
        #mouse_pos = pygame.mouse.get_pos()

        #Introducción de elementos en el botón de jugar
        #Estado del juego: En la pantalla jugar
        if menu_state == "jugar":
          screen.blit(BG, (0,0))

          if botoneasy_button.draw(screen):
            menu_state = "niveleseasy"

          if botondificil_button.draw(screen):
            menu_state = "nivelesdificil"

          if home_button.draw(screen):
            menu_state = "main"

        if menu_state == "niveleseasy":
          screen.blit(BG, (0,0))

          if nivel1_button.draw(screen):
            print("Click a nivel 1")
            menu_state = "nivel1facil"
            pygame.mixer.music.stop()
            #from nivel1f import nivel1facil_
            #nivel1facil_()

          if nivel2_button.draw(screen):
            print("Click a nivel 2")
            menu_state = "nivel1medio"
            pygame.mixer.music.stop()
            #from nivel1m import nivel1medio_
            #nivel1medio_()

          if nivel3_button.draw(screen):
            print("Click a nivel 3")
            menu_state = "nivel1dificil"
            pygame.mixer.music.stop()
            #from nivel1d import nivel1dificil_
            #nivel1dificil_()

          if regresar1_button.draw(screen):
            menu_state = "jugar"
        
        if menu_state == "nivelesdificil":
          screen.blit(BG, (0,0))

          if nivel1hard_button.draw(screen):
            menu_state = "nivel2facil"
            pygame.mixer.music.stop()
            print("Click a nivel 1")
            #from nivel2f import nivel2facil_
            #nivel2facil_()

          if nivel2hard_button.draw(screen):
            print("Click a nivel 2")
            menu_state = "nivel2medio"
            pygame.mixer.music.stop()
            #from nivel2m import nivel2medio_
            #nivel2medio_()

          if nivel3hard_button.draw(screen):
            print("Click a nivel 3")
            menu_state = "nivel2dificil"
            pygame.mixer.music.stop()
            #from nivel2d import nivel2dificil_
            #nivel2dificil_()

          if regresarhhard_button.draw(screen):
            menu_state = "jugar"

        if menu_state == "nivel1facil":
          screen.blit(BG, (0,0))
          
          if fondoobjetivos_img.draw(screen):
            print("hola")
          
          if objetivolvl1facil_img.draw(screen):
            print("hola")
          
          if timelvl1f_imagen.draw(screen):
            print("hola")
          
          if jugar1_button.draw(screen):
            print("hola")
            from nivel1f import nivel1facil_
            nivel1facil_()



        if menu_state == "nivel1medio":
          screen.blit(BG, (0,0))
          
          if fondoobjetivos_img.draw(screen):
            print("hola")

          if objetivolvl1medio_img.draw(screen):
            print("hola")
          
          if timelvl1m_imagen.draw(screen):
            print("hola")

          if jugar1_button.draw(screen):
            print("hola")
            from nivel1m import nivel1medio_
            nivel1medio_()




        if menu_state == "nivel1dificil":
          screen.blit(BG, (0,0))
          
          if fondoobjetivos_img.draw(screen):
            print("hola")

          if objetivolvl1dificil_img.draw(screen):
            print("hola")

          if timelvl1d_imagen.draw(screen):
            print("hola")
        
          if jugar1_button.draw(screen):
            print("hola")
            from nivel1d import nivel1dificil_
            nivel1dificil_()



        if menu_state == "nivel2facil":
          screen.blit(BG, (0,0))
          
          if fondoobjetivos_img.draw(screen):
            print("hola")

          if objetivolvl2facil_img.draw(screen):
            print("hola")
          
          if timelvl2f_imagen.draw(screen):
            print("hola")

          if jugar1_button.draw(screen):
            print("hola")
            from nivel2f import nivel2facil_
            nivel2facil_()
      

        if menu_state == "nivel2medio":
          screen.blit(BG, (0,0))
          
          if fondoobjetivos_img.draw(screen):
            print("hola")
          
          if objetivolvl2medio_img.draw(screen):
            print("hola")

          if timelvl2m_imagen.draw(screen):
            print("hola")

          if jugar1_button.draw(screen):
            print("hola")
            from nivel2m import nivel2medio_
            nivel2medio_()

        
        if menu_state == "nivel2dificil":
          screen.blit(BG, (0,0))
          
          if fondoobjetivos_img.draw(screen):
            print("hola")

          if objetivolvl2dificil_img.draw(screen):
            print("hola")
          
          if timelvl2d_imagen.draw(screen):
            print("hola")

          if jugar1_button.draw(screen):
            print("hola")
            from nivel2d import nivel2dificil_
            nivel2dificil_()
          
          

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