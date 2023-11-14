import pygame

# Definimos algunas variables globales
screen = None
running = True

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 680

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("arialblack", 40)

# Función para dibujar el menú
def draw_menu():
    global screen

    # Limpiamos la pantalla
    screen.fill((0, 0, 0))

    # Dibujamos el título del menú
    title_font = pygame.font.Font("freesansbold.ttf", 30)
    title = title_font.render("Menú de opciones", True, (255, 255, 255))
    screen.blit(title, (100, 50))

    # Dibujamos las opciones del menú
    option_font = pygame.font.Font("freesansbold.ttf", 20)
    options = ["Jugar", "Opciones", "Salir"]
    for i, option in enumerate(options):
        option_surface = option_font.render(option, True, (255, 255, 255))
        screen.blit(option_surface, (100, 100 + i * 30))

# Función para procesar los eventos del menú
def handle_menu_events():
    global running

    for event in pygame.event.get():
        # Si el evento es de cierre de ventana
        if event.type == pygame.QUIT:
            running = False

        # Si el evento es de clic de mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtenemos las coordenadas del clic
            x, y = event.pos

            # Iteramos por las opciones del menú
            options = ["Jugar", "Opciones", "Salir"]
            for i, option in enumerate(options):
                # Si el clic está dentro del rectángulo de la opción
                if x > 100 and x < 400 and y > 100 + i * 30 and y < 130 + i * 30:
                    # Ejecutamos la acción asociada a la opción
                    if i == 0:
                        # Comenzamos el juego
                        pass
                    elif i == 1:
                        # Mostramos el menú de opciones
                        pass
                    elif i == 2:
                        # Salimos del juego
                        running = False

# Bucle principal
while running:
    # Dibujamos el menú
    draw_menu()

    # Procesamos los eventos del menú
    handle_menu_events()

    # Actualizamos la pantalla
    pygame.display.flip()

# Finalizamos Pygame
pygame.quit()