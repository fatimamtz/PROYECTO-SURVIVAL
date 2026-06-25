import pygame

class Inventario:

    def __init__(self):
        self.abierto = False
        self.fuente = pygame.font.SysFont(None, 30)

    def toggle(self):
        self.abierto = not self.abierto

    def draw(self, pantalla, items):

        if not self.abierto:
            return

        pygame.draw.rect(
            pantalla,
            (40, 40, 40),
            (150, 80, 500, 400)
        )

        titulo = self.fuente.render(
            "Inventario",
            True,
            (255, 255, 255)
        )

        pantalla.blit(titulo, (330, 100))

        y = 150

        for item in items:
            texto = self.fuente.render(
                item,
                True,
                (255, 255, 255)
            )

            pantalla.blit(texto, (200, y))
            y += 30