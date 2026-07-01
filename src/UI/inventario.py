import pygame

# Nos aseguramos de que las fuentes funcionen si este archivo se ejecuta o importa
pygame.font.init()

class Inventario:
    def __init__(self):
        self.abierto = False

        # Posición
        self.x = 70
        self.y = 40

        # Tamaño
        self.ancho = 700
        self.alto = 440

        # Slots
        self.slot = 64
        self.espacio = 8
        self.filas = 5
        self.columnas = 8

        self.fuente = pygame.font.SysFont("Arial", 22)

        # Iconos
        self.iconos = {
            "madera": pygame.image.load("img/items/madera.png"),
            "piedra": pygame.image.load("img/items/piedra.png"),
            "metal": pygame.image.load("img/items/metal.png"),
            "palos": pygame.image.load("img/items/palos.png")
        }

        # Nivel
        self.nivel = 1
        self.exp = 0
        self.exp_max = 100

    def toggle(self):
        self.abierto = not self.abierto

    def ganar_exp(self, cantidad):
        self.exp += cantidad
        while self.exp >= self.exp_max:
            self.exp -= self.exp_max
            self.nivel += 1

    def draw(self, pantalla, jugador):
        if not self.abierto:
            return

        fondo = pygame.Surface((self.ancho, self.alto))
        fondo.set_alpha(230)
        fondo.fill((30, 30, 30))
        pantalla.blit(fondo, (self.x, self.y))

        pygame.draw.rect(
            pantalla,
            (120, 90, 60),
            (self.x, self.y, self.ancho, self.alto),
            5
        )

        titulo = self.fuente.render("INVENTARIO", True, (255, 255, 255))
        pantalla.blit(titulo, (self.x + 470, self.y + 10))

        self.draw_slots(pantalla, jugador.inventario)
        self.draw_nivel(pantalla)

    def draw_slots(self, pantalla, inventario):
        inicio_x = self.x + 30
        inicio_y = self.y + 70

        # Convertimos el diccionario a una lista de tuplas [('madera', 5), ('piedra', 2)]
        objetos = list(inventario.items())
        contador = 0

        for fila in range(self.filas):
            for columna in range(self.columnas):
                rect = pygame.Rect(
                    inicio_x + columna * (self.slot + self.espacio),
                    inicio_y + fila * (self.slot + self.espacio),
                    self.slot,
                    self.slot
                )

                pygame.draw.rect(pantalla, (55, 55, 55), rect)
                pygame.draw.rect(pantalla, (150, 150, 150), rect, 2)

                # CORRECCIÓN: Validamos si aún hay objetos para mostrar en este slot
                if contador < len(objetos):
                    # CORRECCIÓN: Accedemos directamente al elemento actual de la lista
                    nombre, cantidad = objetos[contador]

                    if nombre in self.iconos:
                        imagen = pygame.transform.scale(self.iconos[nombre], (48, 48))
                        pantalla.blit(imagen, (rect.x + 8, rect.y + 8))
                        
                        # CORRECCIÓN: Se cambió '.rende' por '.render'
                        texto = self.fuente.render(f"x{cantidad}", True, (255, 255, 255))
                        pantalla.blit(texto, (rect.x + 30, rect.y + 42))

                contador += 1

    def draw_nivel(self, pantalla):
        panel = pygame.Rect(self.x + 760, self.y + 70, 330, 180)

        pygame.draw.rect(pantalla, (45, 45, 45), panel)
        pygame.draw.rect(pantalla, (120, 90, 60), panel, 4)

        texto = self.fuente.render(f"Nivel {self.nivel}", True, (255, 255, 255))
        pantalla.blit(texto, (panel.x + 95, panel.y + 20))

        pygame.draw.rect(pantalla, (70, 70, 70), (panel.x + 25, panel.y + 80, 280, 22))

        progreso = int((self.exp / self.exp_max) * 280)
        pygame.draw.rect(pantalla, (40, 180, 255), (panel.x + 25, panel.y + 80, progreso, 22))

        texto2 = self.fuente.render(f"{self.exp}/{self.exp_max} EXP", True, (255, 255, 255))
        pantalla.blit(texto2, (panel.x + 80, panel.y + 120))