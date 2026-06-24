import pygame
import math

class Enemigos:
    def __init__(self, x, y, vida, danio, velocidad, imagen):
        self.x = x
        self.y = y

        self.hp_max = vida
        self.hp_actual = vida
        self.danio = danio
        self.velocidad = velocidad

        self.imagen = imagen
        self.rect=pygame.Rect(
            x+10,
            y+20,
            15,
            10
        )

    def distancia_jugador(self, jugador):
        dx = jugador.x - self.x
        dy = jugador.y - self.y
        return math.sqrt(dx**2 + dy**2)

    def mover(self, jugador, entorno, enemigos):
        if self.distancia_jugador(jugador) < 200:
            dx = jugador.x - self.x
            dy = jugador.y - self.y
            distancia = math.sqrt(dx**2 + dy**2)

            if distancia > 0:
                mov_x = (dx / distancia) * self.velocidad
                mov_y = (dy / distancia) * self.velocidad
             #en esta parte lo que hace es que el enemigo rodeara el obstaculo para que se vea mas natural 
                nuevo_rect_x=self.rect.copy()
                nuevo_rect_x.x+=mov_x
                libre_x= not entorno.colision(nuevo_rect_x)
                for enemigo in enemigos:
                    if enemigo != self and nuevo_rect_x.colliderect(enemigo.rect):
                        libre_x = False
                if libre_x:
                    self.x +=mov_x

                nuevo_rect_y=self.rect.copy()
                nuevo_rect_y.y+=mov_y
                libre_y= not entorno.colision(nuevo_rect_y)
                for enemigo in enemigos:
                    if enemigo != self and nuevo_rect_y.colliderect(enemigo.rect):
                        libre_y = False
                if libre_y:
                    self.y +=mov_y
                    
                self.rect.x=int(self.x+10)
                self.rect.y=int(self.y+20)

            

    def atacar(self, jugador):
        if self.rect.colliderect(jugador.rect):
            jugador.recibir_dano(self.danio)

    def recibir_dano(self, dano):
        self.hp_actual -= dano

    def morir(self):
        return self.hp_actual <= 0

    def draw(self, pantalla, camara):
        pantalla.blit(self.imagen,(self.x - camara.x, self.y - camara.y))


class Zombie(Enemigos):
    def __init__(self, x, y):
        imagen = pygame.image.load("img/entidades/zombie.png").convert_alpha()
        imagen = pygame.transform.scale(imagen, (35, 30))

        super().__init__(
            x=x,
            y=y,
            vida=100,
            danio=10,
            velocidad=1,
            imagen=imagen
        )

    def zombie_rect(self, dx=0, dy=0):
        return pygame.Rect(
            self.x + dx + 10,
            self.y + dy + 20,
            15,
            10
        )
class Saqueador(Enemigos):
    def __init__(self, x, y):
        imagen = pygame.image.load("img/entidades/saqueador.png").convert_alpha()
        imagen = pygame.transform.scale(imagen, (35, 30))

        super().__init__(
            x=x,
            y=y,
            vida=100,
            danio=10,
            velocidad=1,
            imagen=imagen
        )

    def saqueador_rect(self, dx=0, dy=0):
        return pygame.Rect(
            self.x + dx + 10,
            self.y + dy + 20,
            15,
            10
        )
class Animal1(Enemigos):
    def __init__(self, x, y):
        imagen = pygame.image.load("img/entidades/animal1.png").convert_alpha()
        imagen = pygame.transform.scale(imagen, (40, 40))

        super().__init__(
            x=x,
            y=y,
            vida=100,
            danio=10,
            velocidad=1,
            imagen=imagen
        )

    def animal1_rect(self, dx=0, dy=0):
        return pygame.Rect(
            self.x + dx + 10,
            self.y + dy + 20,
            15,
            10
        )