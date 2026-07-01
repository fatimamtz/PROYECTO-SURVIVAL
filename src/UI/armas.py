import pygame
class Armas:
    def __init__(self,nombre,material,danio,tipo):
        self.nombre=nombre
        self.tipo=tipo
        self.material=material
        self.danio=danio

        #espadas 
        ESPADA_MADERA= Armas("Espada de madera","espada","madera",15)
        ESPADA_PIEDRA=Armas("Espadad de piedra","espada","piedra",25)
        ESPADA_METAL=Armas("Espadad de metal","espada","metal",50)
        
        #hachas
        HACHA_MADERA=Armas("Hacha de madera","hacha","madera",15)
        HACHA_PIEDRA=Armas("Hacha de piedra","hacha","piedra",25)
        HACHA_METAL=Armas("Hacha de metal","hacha","metal",50)

        #picos
        PICO_MADERA=Armas("Pico de madrea","pico","madera",15)
        PICO_PIEDRA=Armas("Pico de piedra","pico","piedra",25)
        PICO_METAL=Armas("Pico de metal","pico","metal",50)

