import pygame

class Jugador:

    def __init__(self, x, y):

        # Posición
        self.x = x
        self.y = y

        # Atributos
        self.vida = 100
        self.energia = 100
        self.nivel = 1
        self.experiencia = 0

        self.velocidad = 2
        self.danio = 10

        #Sistema de combate
        #self.contador_golpes = 0
        #self.golpes_critico = 4
        #self.danio_critico = 25

        self.inventario = []

        # Tamaño
        self.size = 32
        self.rect = pygame.Rect(self.x, self.y, self.size,self.size)

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

        self.rect.x = self.x
        self.rect.y = self.y

    def per_rect(self, dx, dy):
        return pygame.Rect(
            self.x + dx,
            self.y + dy,
            self.size,
            self.size
        )

    def correr(self):
        if self.energia > 0:
            self.energia -= 0.1
            return self.velocidad * 1
        return self.velocidad

    def recuperar_energia(self):
        self.energia = min(
            100,
            self.energia + 0.05
        )

    #def atacar(self, enemigo):
     #   self.contador_golpes += 1
     #   if self.contador_golpes >= self.golpes_critico:
      #      enemigo.recibir_dano(self.danio_critico)
      #      self.contador_golpes = 0
       # else:
        #    enemigo.recibir_dano(self.danio)

    def recibir_dano(self, dano):
        self.vida -= dano

    def talar_arbol(self, arbol):
        self.energia -= 5
        self.experiencia += 10

    def picar_piedra(self, roca):
        self.energia -= 5
        self.experiencia += 10

    def draw(self, pantalla, camara):

        pantalla.blit(
            self.imagen_actual,
            (
                self.x - camara.x,
                self.y - camara.y
            )
        )