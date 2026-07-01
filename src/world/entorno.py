import pygame
import random

import pygame

class Recurso:

    def __init__(self, x, y, imagen, vida, rect):
        self.x = x
        self.y = y
        self.imagen = imagen
        self.vida = vida
        self.vida_max = vida
        self.rect = rect

    def recibir_dano(self, dano):
        self.vida -= dano
        return self.vida <= 0

    def draw(self, pantalla, camara):

        pantalla.blit(
            self.imagen,
            (self.x-camara.x,
             self.y-camara.y)
        )

        if self.vida < self.vida_max:

            pygame.draw.rect(
                pantalla,
                (255,0,0),
                (self.x-camara.x,
                 self.y-8-camara.y,
                 40,
                 4)
            )

            pygame.draw.rect(
                pantalla,
                (0,255,0),
                (
                    self.x-camara.x,
                    self.y-8-camara.y,
                    int(40*self.vida/self.vida_max),
                    4
                )
            )

class Entorno:
    def __init__(self):
        self.ancho_mundo = 5000
        self.alto_mundo = 5000

        self.arboles = []
        self.piedra = []
        self.hierro = []
        self.arbusto = []
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
        self.imagen_arbusto=pygame.image.load(
             "img/objetos/arbusto.png"
        )
        self.imagen_arbusto=pygame.transform.scale(
             self.imagen_arbusto,
             (25,50)
        )
        
        for i in range(200):

            while True:
                x = random.randint(0, self.ancho_mundo)
                y = random.randint(0, self.alto_mundo)
                valido = True

                # No cerca de otros árboles
                for arboles in self.arboles:
                    if abs(x - arboles.x) < 100 and abs(y - arboles.y) < 100:
                        valido = False
                        break
                if valido:
                    rect=pygame.Rect(
                        x+17,
                        y+52,
                        16,
                        18,
                    )
                    self.arboles.append(
                         Recurso(
                              x,
                              y,
                              self.imagen_arboles,
                              40,
                              rect
                         )
                    )
                    break


        for i in range(80):
            while True:
                x = random.randint(0, self.ancho_mundo)
                y = random.randint(0, self.alto_mundo)
                valido = True


                # No cerca de otras poiedras 
                for piedra in self.piedra:
                    if abs(x - piedra.x) < 60 and abs(y - piedra.y) < 60:
                        valido = False
                        break

                if valido:
                    rect=pygame.Rect(
                        x+4,
                        y+6,
                        16,
                        18,
                    )
                    self.piedra.append(
                         Recurso(
                              x,
                              y,
                              self.imagen_piedra,
                              30,
                              rect
                         )
                    )
                    break
                
        for i in range(40):
            while True:
                x = random.randint(0, self.ancho_mundo)
                y = random.randint(0, self.alto_mundo)
                valido = True


                # No cerca de otros hierros
                for hierro in self.hierro:
                    if abs(x - hierro.x) < 100 and abs(y - hierro.y) < 100:
                        valido = False
                        break

                if valido:
                    rect=pygame.Rect(
                        x+12,
                        y+28,
                        95,
                        35,
                    )
                    self.hierro.append(
                         Recurso(
                              x,
                              y,
                              self.imagen_hierro,
                              50,
                              rect
                         )
                    )
                    break
        
        for i in range(40):
            while True:
                x = random.randint(0, self.ancho_mundo)
                y = random.randint(0, self.alto_mundo)
                valido = True

                #No cerca de otros arbustos
                for arbusto in self.arbusto:
                    if abs(x - arbusto.x) < 100 and abs(y - arbusto.y) < 100:
                        valido = False
                        break
                
                if valido:
                    rect=pygame.Rect(
                        x+5,
                        y+25,
                        15,
                        20,
                    )
                    self.arbusto.append(
                         Recurso(
                              x,
                              y,
                              self.imagen_arbusto,
                              15,
                              rect
                         )
                    )
                    break

    def draw(self, pantalla, camara):
        pantalla.blit(
            self.pasto,
            (0,0)
        )
        for piedra in self.piedra:
            piedra.draw(pantalla,camara)

        for hierro in self.hierro:
            hierro.draw(pantalla,camara)

        for arboles in self.arboles:
            arboles.draw(pantalla,camara)

        for arbusto in self.arbusto:
            arbusto.draw(pantalla,camara)    
       
    def colision(self, rect_jugador):

    # Árboles
         for arboles in self.arboles:
           if rect_jugador.colliderect(arboles.rect):
            return True

    # Piedras
         for piedra in self.piedra:
          if rect_jugador.colliderect(piedra.rect):
            return True

    # Hierro
         for hierro in self.hierro:
          if rect_jugador.colliderect(hierro.rect):
            return True

    # Arbustos
         for arbusto in self.arbusto:
          if rect_jugador.colliderect(arbusto.rect):
            return True

         return False