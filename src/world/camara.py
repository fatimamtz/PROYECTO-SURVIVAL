class Camara:

    def __init__(self):

        self.x = 0
        self.y = 0

        # Margen antes de mover la cámara
        self.margen_x = 200
        self.margen_y = 150

    def actualizar(self, jugador):

        pantalla_x = jugador.x - self.x
        pantalla_y = jugador.y - self.y

        # Derecha
        if pantalla_x > 800 - self.margen_x:
            self.x = jugador.x - (800 - self.margen_x)

        # Izquierda
        elif pantalla_x < self.margen_x:
            self.x = jugador.x - self.margen_x

        # Abajo
        if pantalla_y > 600 - self.margen_y:
            self.y = jugador.y - (600 - self.margen_y)

        # Arriba
        elif pantalla_y < self.margen_y:
            self.y = jugador.y - self.margen_y