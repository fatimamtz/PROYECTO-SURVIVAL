import pygame
from src.config.configuracion import *

class Hud:

    def __init__(self):
        self.x = 10
        self.y = 10
        self.ancho = 200
        self.alto = 20
        self.fuente = pygame.font.SysFont(None, 18)

    def draw(self, pantalla, jugador):

        # Fondo de la barra (gris oscuro) y borde
        pygame.draw.rect(
            pantalla, (GRIS),
            (self.x - 2, self.y - 2, self.ancho + 4, self.alto + 4)
        )
        pygame.draw.rect(
            pantalla, (ROJO),
            (self.x, self.y, self.ancho, self.alto)
        )

        # Porcentaje de vida actual
        porcentaje = jugador.hp_actual / jugador.hp_max
        porcentaje = max(0, min(1, porcentaje))

        ancho_vida = int(self.ancho * porcentaje)
        pygame.draw.rect(
            pantalla, (VERDE),
            (self.x, self.y, ancho_vida, self.alto)
        )

        # Texto con el numero de HP encima de la barra
        texto = self.fuente.render(
            f"{int(jugador.hp_actual)} / {jugador.hp_max}",
            True, VERDE
        )
        texto_rect = texto.get_rect(
            center=(self.x + self.ancho // 2, self.y + self.alto // 2)
        )
        pantalla.blit(texto, texto_rect)