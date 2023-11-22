import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Configuración de la ventana
ANCHO = 400
ALTO = 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulación de Gancho de Pescador")

# Posición inicial del gancho
gancho_x = ANCHO // 2
gancho_y = 50

# Altura de la cuerda
cuerda_altura = ALTO - gancho_y

# Velocidad del gancho
velocidad_bajada = 5
velocidad_subida = 5  # Velocidad más lenta al subir

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener el estado de las teclas
    teclas = pygame.key.get_pressed()

    # Mover el gancho hacia abajo mientras se presiona la flecha hacia abajo
    if teclas[pygame.K_DOWN]:
        gancho_y += velocidad_bajada

        # Limitar la posición del gancho para que no se salga de la ventana
        if gancho_y > ALTO:
            gancho_y = ALTO

    else:
        # Si no se presiona la flecha hacia abajo, subir el gancho de manera más lenta
        gancho_y -= velocidad_subida

        # Limitar la posición del gancho para que no se salga de la ventana en la parte superior
        if gancho_y < 50:
            gancho_y = 50

    # Limpiar la pantalla
    ventana.fill(BLANCO)

    # Dibujar la cuerda (línea negra)
    pygame.draw.line(ventana, NEGRO, (ANCHO // 2, 0), (gancho_x, gancho_y), 5)

    # Dibujar el gancho (rectángulo)
    pygame.draw.rect(ventana, NEGRO, (gancho_x - 10, gancho_y - 10, 20, 20))

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad de actualización
    pygame.time.Clock().tick(30)