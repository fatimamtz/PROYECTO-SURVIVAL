import pygame
import random

class Entorno:
    def __init__(self):
        self.ancho_mundo = 5000
        self.alto_mundo = 5000

        self.arboles = []
        self.piedra=[]
        self.hierro=[]
        #texturas
        self.imagen_piedra=pygame.image.load(
            "img/objetos/piedra.png"
        )
        self.imagen_piedra=pygame.transform.scale(
            self.imagen_piedra,
            (35,35)
        )
        self.imagen_hierro=pygame.image.load(
            "img/objetos/carro_destruido.png"
        )
        self.imagen_hierro=pygame.transform.scale(
            self.imagen_hierro,
            (120,80)
        )
    
        self.pasto=pygame.image.load(
            "img/objetos/pasto.png"
        )
        self.pasto=pygame.transform.scale(
            self.pasto,
            (800,600)
        )
        self.imagen_arboles=pygame.image.load(
            "img/objetos/arboles.png"
        )
        self.imagen_arboles=pygame.transform.scale(
            self.imagen_arboles,
            (50,100)
        )
        for i in range(200):

            while True:
                x = random.randint(0, self.ancho_mundo)
                y = random.randint(0, self.alto_mundo)
                valido = True

                # No cerca de otros árboles
                for ax, ay in self.arboles:
                    if abs(x - ax) < 100 and abs(y - ay) < 100:
                        valido = False
                        break
                if valido:
                    self.arboles.append((x, y))
                    break

        for i in range(80):
            while True:
                x = random.randint(0, self.ancho_mundo)
                y = random.randint(0, self.alto_mundo)
                valido = True


                # No cerca de otros árboles
                for ax, ay in self.piedra:
                    if abs(x - ax) < 60 and abs(y - ay) < 60:
                        valido = False
                        break

                if valido:
                 self.piedra.append((x, y))
                break

        for i in range(40):
            while True:
                x = random.randint(0, self.ancho_mundo)
                y = random.randint(0, self.alto_mundo)
                valido = True


                # No cerca de otros hierros
                for ax, ay in self.hierro:
                    if abs(x - ax) < 100 and abs(y - ay) < 100:
                        valido = False
                        break

                if valido:
                 self.hierro.append((x, y))
                break

    def draw(self, pantalla, camara):
        pantalla.blit(
            self.pasto,
            (0,0)
        )
        for x, y in self.piedra:
            pantalla.blit(
                    self.imagen_piedra,
                    (x - camara.x, y - camara.y)
                
            )
        for x, y in self.hierro:
                pantalla.blit(
                    self.imagen_hierro,
                    (x - camara.x, y - camara.y)
                )
        for x, y in self.arboles:
                 pantalla.blit(
                    self.imagen_arboles,
                    (x - camara.x, y - camara.y)
             )
             
    def colision(self, rect_jugador):
        for x,y in self.arboles:
            arbol_rect=pygame.Rect(
                x+17,
                y+72,
                16,
                18
            )
            if rect_jugador.colliderect(arbol_rect):
                return True
            
        for x,y in self.piedra:
                piedra_rect = pygame.Rect(
                    x+4,
                    y+6,
                    27,
                    23
                    )
                if rect_jugador.colliderect(piedra_rect):
                    return True
                
        for x,y in self.hierro:
                hierro_rect = pygame.Rect(
                    x+12,
                    y+28,
                    95,
                    35
                    )
                if rect_jugador.colliderect(hierro_rect):
                    return True
        return False
   
    def per_rect(self, dx=0, dy=0):
       return pygame.Rect(
        self.x + dx + 10,
        self.y + dy + 25,
        20,
        15
       )
