class Enemigos():
    def __init__(self,x , y, vida, danio):
        self.x = x
        self.y = y

        self.hp_max = vida
        self.hp_actual = vida

        self.danio = danio

        self.size = 20

        self.drop = []

        distacia_jugador = 

    def mover():
        pass

    def atacar(self, jugador):
        if jugador.x > self.x:
            self.x += 1
        elif jugador.x < self.x:
            self.x -= 1
        if jugador.y > self.y:
            self.y += 1
        elif jugador.y < self.y:
            self.y -= 1

    def recibir_dano(self, dano):
        self.hp_actual -= dano

        if self.hp_actual <= 0:
            self.morir()

    def morir(self):
        print("Enemigo eliminado")

    def morir():
        pass
    pass

class Zombies(Enemigos):
        
    def __init__(self, vida, danio):
         super().__init__(vida, danio)

    
    def morir():
        pass

class Humanos(Enemigos):
    pass

class Animales(Enemigos):
    pass