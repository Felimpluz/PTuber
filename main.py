import pygame
import sys

# Inicializa todos los módulos de Pygame
pygame.init()

# Tamaño de la ventana
ANCHO = 1280
ALTO = 720

# Crear la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Título de la ventana
pygame.display.set_caption("PTuber")

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# Variable que mantiene el programa abierto
ejecutando = True

while ejecutando:

    # Revisar eventos (cerrar ventana, teclado, etc.)
    for evento in pygame.event.get():

        # Si el usuario presiona la X
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Color de fondo (30,30,30 = gris oscuro)
    pantalla.fill((30, 30, 30))

    # Actualizar la ventana
    pygame.display.flip()

    # Limitar a 60 FPS
    reloj.tick(60)

# Cerrar Pygame correctamente
pygame.quit()
sys.exit()
