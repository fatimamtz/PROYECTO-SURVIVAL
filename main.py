import pygame
import random
from src.config.configuracion import *
from src.entities.jugador import Jugador
from src.world.entorno import *
from src.world.camara import Camara
from src.entities.enemigos import Zombie
from src.entities.enemigos import Saqueador
from src.entities.enemigos import Animal1
from src.UI.hud import Hud
from src.UI.inventario import Inventario
pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(TITULO)

reloj = pygame.time.Clock()

hud = Hud()
#se agrego el inventario provisional
inventario = Inventario()

jugador = Jugador(100, 100)
jugador.inventario.append("madera")
entorno = Entorno()
camara = Camara()

#Funcion para que los enemigos no aparezcan dentro de los arboles, carros y piedras
def posicion_valida(entorno,enemigos):
    while True:
        x = random.randint(0,760)
        y = random.randint(0,560)
        rect = pygame.Rect(x+10, y+20, 15, 10)
        valido = True

        #Comprueba los arboles, piedras y carros
        if entorno.colision(rect):
            valido = False
        for enemigo in enemigos:
            if rect.colliderect(enemigo.rect):
                valido = False
                break
        if valido:
            return x,y
        
enemigos = []
for i in range(8):
    x,y = posicion_valida(entorno,enemigos)
    enemigos.append(Zombie(x,y))
for i in range(4):
    x,y = posicion_valida(entorno,enemigos)
    enemigos.append(Saqueador(x,y))
for i in range(7):
    x,y = posicion_valida(entorno,enemigos)
    enemigos.append(Animal1(x,y))

ejecutando = True

while ejecutando:

    moviendo = False

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_e:
                inventario.toggle()


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
            jugador.imagen_actual = jugador.caminar_arriba[0]
    
    pantalla.fill((0,0,0))

    camara.actualizar(jugador)
    entorno.draw(pantalla, camara)
    jugador.draw(pantalla, camara)

    for enemigo in enemigos:
        enemigo.mover(jugador,entorno,enemigos)
        enemigo.atacar(jugador)
    #dibuja los enemigos en la pantalla
    for enemigo in enemigos:
        enemigo.draw(pantalla,camara)
    
    hud.draw(pantalla, jugador)

    inventario.draw(
        pantalla,
        jugador.inventario
    )

    pygame.display.flip()

    reloj.tick(FPS)

pygame.quit()