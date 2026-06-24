from src.entities.zombies import Enemigos 
import pygame
class Zombie(Enemigos):
 def __init__(self, x, y):
  imagen=pygame.image.load("img/entidades/zombie.png").convert_alpha()
  imagen=pygame.transform.scale(imagen,(40,40))
  super().__init__(
   x=x,
   y=y,
   vida=100,
   danio=10,
   velocidad=1,
   imagen=imagen
 )
