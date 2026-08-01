import pygame
import sys

# Iniciar Pygame
pygame.init()

# Tamaño de la ventana
ANCHO = 1280
ALTO = 720

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("PTuber")

reloj = pygame.time.Clock()

# -----------------------------
# Cargar imágenes
# -----------------------------

ruta = "assets/avatars/Suki/"

back_layer = pygame.image.load(ruta + "back_layer.png").convert_alpha()
body = pygame.image.load(ruta + "body.png").convert_alpha()
face = pygame.image.load(ruta + "face.png").convert_alpha()
eye_left = pygame.image.load(ruta + "eye_left.png").convert_alpha()
eye_right = pygame.image.load(ruta + "eye_right.png").convert_alpha()
eyebrow_left = pygame.image.load(ruta + "eyebrow_left.png").convert_alpha()
eyebrow_right = pygame.image.load(ruta + "eyebrow_right.png").convert_alpha()
mouth = pygame.image.load(ruta + "mouth.png").convert_alpha()
front_layer = pygame.image.load(ruta + "front_layer.png").convert_alpha()

# Posición donde aparecerá el personaje
x = 300
y = 100

# -----------------------------
# Bucle principal
# -----------------------------

ejecutando = True

while ejecutando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill((40, 40, 40))

    # Dibujar las capas en orden
    pantalla.blit(back_layer, (x, y))
    pantalla.blit(body, (x, y))
    pantalla.blit(face, (x, y))
    pantalla.blit(eye_left, (x, y))
    pantalla.blit(eye_right, (x, y))
    pantalla.blit(eyebrow_left, (x, y))
    pantalla.blit(eyebrow_right, (x, y))
    pantalla.blit(mouth, (x, y))
    pantalla.blit(front_layer, (x, y))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
