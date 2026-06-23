import pygame
from src.config.configuracion import *
from src.entities.jugador import Jugador
from src.world.entorno import *
from src.world.camara import Camara

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(TITULO)

reloj = pygame.time.Clock()

jugador = Jugador(100, 100)
entorno = Entorno()
camara = Camara()

ejecutando = True

while ejecutando:

    moviendo = False

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LSHIFT]:
        velocidad = jugador.correr()
    else:
        velocidad = jugador.velocidad
        jugador.recuperar_energia()

    if teclas[pygame.K_LEFT]:
        nuevo_rect = jugador.per_rect( -velocidad,0)

        if not entorno.colision(nuevo_rect):
            jugador.mover(-velocidad,0)
            jugador.direccion = "izquierda"
            moviendo = True

    if teclas[pygame.K_RIGHT]:
        nuevo_rect = jugador.per_rect(velocidad,0)
        
        if not entorno.colision(nuevo_rect):
            jugador.mover(velocidad,0)
            jugador.direccion = "derecha"

            moviendo = True

    if teclas[pygame.K_UP]:
        nuevo_rect = jugador.per_rect(0,-velocidad)
        
        if not entorno.colision(nuevo_rect):
            jugador.mover(0,-velocidad)
            jugador.direccion = "arriba"
            moviendo = True

    if teclas[pygame.K_DOWN]:
        nuevo_rect = jugador.per_rect(0,velocidad)
        
        if not entorno.colision(nuevo_rect):
            jugador.mover(0,velocidad)
            jugador.direccion = "abajo"

            moviendo = True

    # Animación
    if moviendo:
        jugador.animar_caminar()

    else:
        if jugador.direccion == "abajo":
            jugador.imagen_actual = jugador.caminar_abajo[0]

        elif jugador.direccion == "derecha":
            jugador.imagen_actual = jugador.caminar_derecha[0]
        
        elif jugador.direccion == "izquierda":
            jugador.imagen_actual = jugador.caminar_izquierda[0]
        elif jugador.direccion == "arriba":
            jugador.imagen_actual == jugador.caminar_arriba[0]

    camara.actualizar(jugador)
    entorno.draw(pantalla, camara)
    jugador.draw(pantalla, camara)

    pygame.display.flip()

    reloj.tick(FPS)

pygame.quit()