import pygame
import sys
import math

# -----------------------------
# Iniciar Pygame
# -----------------------------

pygame.init()

# -----------------------------
# Ventana
# -----------------------------

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
body_accessory = pygame.image.load(ruta + "body_accessory.png").convert_alpha()

# -----------------------------
# Posición base
# -----------------------------

BASE_X = 300
BASE_Y = 100

# -----------------------------
# Offsets
# -----------------------------

BODY_OFFSET_X = 210
BODY_OFFSET_Y = 530

ACCESSORY_OFFSET_X = 25
ACCESSORY_OFFSET_Y = 10

HEAD_OFFSET_X = 0
HEAD_OFFSET_Y = 0

EYES_OFFSET_X = 0
EYES_OFFSET_Y = -1

BROWS_OFFSET_X = 0
BROWS_OFFSET_Y = -2

MOUTH_OFFSET_X = 0
MOUTH_OFFSET_Y = 0

FRONT_OFFSET_X = 0
FRONT_OFFSET_Y = 1

BACK_OFFSET_X = 0
BACK_OFFSET_Y = 0

# -----------------------------
# Tiempo
# -----------------------------

tiempo = 0.03

# -----------------------------
# Bucle principal
# -----------------------------

ejecutando = True

while ejecutando:

    # -------------------------
    # Eventos
    # -------------------------

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # -------------------------
    # Tiempo
    # -------------------------

    tiempo += 0.10


    # =========================================================
    # CUERPO
    # =========================================================

    body_x = BASE_X + BODY_OFFSET_X
    body_y = BASE_Y + BODY_OFFSET_Y

    # =========================================================
    # ACCESORIO DEL CUERPO
    # =========================================================

    accessory_x = body_x + ACCESSORY_OFFSET_X
    accessory_y = body_y + ACCESSORY_OFFSET_Y

    # Squash & Stretch

    escala_y = 1.0 + math.sin(tiempo) * 0.03
    escala_x = 1.0 - math.sin(tiempo) * 0.02

    nuevo_ancho = int(body.get_width() * escala_x)
    nuevo_alto = int(body.get_height() * escala_y)
    

    body_escalado = pygame.transform.scale(
        body,
        (nuevo_ancho, nuevo_alto)
    )

    body_draw_x = body_x - (nuevo_ancho - body.get_width()) // 2
    body_draw_y = body_y - (nuevo_alto - body.get_height())

    # =========================================================
    # RESPIRACIÓN DEL ACCESORIO
    # =========================================================

    escala_acc_x = 1.0 - math.sin(tiempo) * 0.14
    escala_acc_y = 1.0 - math.sin(tiempo) * 0.02

    nuevo_ancho_acc = int(body_accessory.get_width() * escala_acc_x)
    nuevo_alto_acc = int(body_accessory.get_height() * escala_acc_y)

    accessory_escalado = pygame.transform.scale(
        body_accessory,
        (nuevo_ancho_acc, nuevo_alto_acc)
   )

    accessory_draw_x = accessory_x - (nuevo_ancho_acc - body_accessory.get_width()) // 2
    accessory_draw_y = accessory_y - math.sin(tiempo) * 2
    
    # =========================================================
    # CABEZA
    # =========================================================

    head_x = (
        BASE_X
        + HEAD_OFFSET_X
        + math.sin(tiempo * 0.8) * 3
    )

    head_y = (
        BASE_Y
        + HEAD_OFFSET_Y
        + math.cos(tiempo * 0.8) * 2
    )

    # =========================================================
    # OJOS
    # =========================================================

    eyes_x = head_x + EYES_OFFSET_X
    eyes_y = head_y + EYES_OFFSET_Y

    # =========================================================
    # CEJAS
    # =========================================================

    brows_x = head_x + BROWS_OFFSET_X
    brows_y = head_y + BROWS_OFFSET_Y

    # =========================================================
    # BOCA
    # =========================================================

    mouth_x = head_x + MOUTH_OFFSET_X
    mouth_y = head_y + MOUTH_OFFSET_Y

    # =========================================================
    # CABELLO
    # =========================================================

    front_x = head_x + FRONT_OFFSET_X
    front_y = head_y + FRONT_OFFSET_Y

    back_x = head_x + BACK_OFFSET_X
    back_y = head_y + BACK_OFFSET_Y

    # -------------------------
    # Dibujar
    # -------------------------

    pantalla.fill((40, 40, 40))

    pantalla.blit(back_layer, (back_x, back_y))
    pantalla.blit(body_escalado, (body_draw_x, body_draw_y))
    pantalla.blit(face, (head_x, head_y))
    pantalla.blit(eye_left, (eyes_x, eyes_y))
    pantalla.blit(eye_right, (eyes_x, eyes_y))
    pantalla.blit(eyebrow_left, (brows_x, brows_y))
    pantalla.blit(eyebrow_right, (brows_x, brows_y))
    pantalla.blit(mouth, (mouth_x, mouth_y))
    pantalla.blit(front_layer, (front_x, front_y))
    pantalla.blit(accessory_escalado, (accessory_draw_x, accessory_draw_y))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()