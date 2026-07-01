import pygame
from src.UI.armas as armas 

class Jugador:

    def __init__(self, x, y):

        # Posición
        self.x = x
        self.y = y

        # Atributos
        self.hp_max = 100
        self.hp_actual = 100
        self.energia = 100
        self.nivel = 1
        self.experiencia = 0

        self.velocidad = 2
        self.danio = 10

        #Sistema de combate
        self.contador_golpes = 0
        self.golpes_critico = 4
        self.danio_critico = 25

        self.inventario = {}

        # Tamaño
        self.size = 32
        self.rect = pygame.Rect(
        self.x + 8, 
        self.y + 20,
        16,
        12
        )

        # Dirección actual
        self.direccion = "abajo"

        # Spritesheet
        self.sprite_sheet = pygame.image.load(
            "img/personaje/personaje.png"
        ).convert_alpha()

        # Animación
        self.frame_actual = 0
        self.contador_animacion = 0

        self.caminar_abajo = []
        for columna in range(6):
            self.caminar_abajo.append(
                self.obtener_sprite(0, columna)
            )

        self.caminar_derecha = []
        for columna in range(6):
            self.caminar_derecha.append(
                self.obtener_sprite(4, columna)
            )

        self.caminar_izquierda = []
        for columna in range(6):
            sprite_derecha = self.obtener_sprite(4, columna)

            sprite_izquierda = pygame.transform.flip(
                sprite_derecha,True,False
    )
            self.caminar_izquierda.append(
                sprite_izquierda
    )
        self.caminar_arriba = []
        for columna in range(6):
            self.caminar_arriba.append(
                self.obtener_sprite(5, columna)
            )
    # Imagen inicial
        self.imagen_actual = self.caminar_abajo[0]

    def obtener_sprite(self, fila, columna):
        sprite = pygame.Surface(
            (32, 32),
            pygame.SRCALPHA
        )
        sprite.blit(
            self.sprite_sheet,
            (0, 0),
            (columna * 32, fila * 32, 32, 32)
        )

        return sprite

    def animar_caminar(self):

        self.contador_animacion += 1
        if self.contador_animacion >= 8:
            self.contador_animacion = 0
            self.frame_actual += 1

            if self.frame_actual >= 6:
                self.frame_actual = 0

        if self.direccion == "abajo":
            self.imagen_actual = self.caminar_abajo[
                self.frame_actual
            ]

        elif self.direccion == "derecha":
            self.imagen_actual = self.caminar_derecha[
                self.frame_actual
            ]
        elif self.direccion == "izquierda":
            self.imagen_actual = self.caminar_izquierda[
                self.frame_actual
            ]
        elif self.direccion == "arriba":
            self.imagen_actual = self.caminar_arriba[
                self.frame_actual
            ]

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

        self.rect.x = self.x + 8
        self.rect.y = self.y + 20

    def per_rect(self, dx, dy):
        return pygame.Rect(
            self.x + dx,
            self.y + dy,
            self.size,
            self.size
        )

    def correr(self):
        if self.energia > 0:
            self.energia = max(0, self.energia - 0.1)
            return self.velocidad * 1.5
        return self.velocidad

    def recuperar_energia(self):
        self.energia = min(
            100,
            self.energia + 0.05
        )

    def atacar(self, enemigo):
        if self.energia <= 0:
            return
        self.energia = max(0, self.energia - 5)
        
        self.contador_golpes += 1
        if self.contador_golpes >= self.golpes_critico:
            enemigo.recibir_danio(self.danio_critico)
            self.contador_golpes = 0
        else:
               enemigo.recibir_danio(self.danio)

    def recibir_danio(self,danio):
        self.hp_actual -= danio
        if self.hp_actual < 0:
           self.hp_actual = 0

    def talar_arboles(self, arboles):
        self.energia -= 5
        if arboles.recibir_dano(self.danio):
          self.experiencia += 10
          self.inventario["madera"]=(
            self.inventario.get("madera",0)+1
        )

    def picar_piedra(self, piedra):
        self.energia -= 5
        if piedra.recibir_dano(self.danio):
         self.experiencia += 10
         self.inventario["piedra"]=(
          self.inventario.get("piedra",0)+1
        )
    def picar_metal(self, metal):
        self.energia -= 8
        if metal.recibir_dano(self.danio):
         self.experiencia += 15
         self.inventario["metal"]=(
          self.inventario.get("metal",0)+1
        )
    def recolectar_palos(self, palos):
        self.energia -= 2
        if palos.recibir_dano(self.danio):
          self.experiencia += 4
          self.inventario["palos"]=(
           self.inventario.get("palos",0)+1
        )    
    def obtener_area_interaccion(self):

     if self.direccion == "arriba":
        return pygame.Rect(self.x, self.y - 20, 32, 20)

     elif self.direccion == "abajo":
        return pygame.Rect(self.x, self.y + 32, 32, 20)

     elif self.direccion == "izquierda":
        return pygame.Rect(self.x - 20, self.y, 20, 32)

     elif self.direccion == "derecha":
        return pygame.Rect(self.x + 32, self.y, 20, 32)

    def draw(self, pantalla, camara):

        pantalla.blit(
            self.imagen_actual,
            (
                self.x - camara.x,
                self.y - camara.y
            )
        )
    def ganar_experiencia(self, cantidad):
         self.experiencia += cantidad

         while self.experiencia >= 100:
          self.experiencia -= 100
          self.nivel += 1