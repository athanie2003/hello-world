import pygame
from random import randint
from Enemies import State
from Enemies import Enemies


class EnemyAlien(Enemies):
    def __init__(self, direction, isDead, state, x, y, width, height, speed, health, element, img_path, screen_rect):
        
        self.img_path = img_path
        self.isDead = isDead
        self.state = state
        self.direction = direction
        self.health = health
        self.element = element

        #Enemies will be randomly implemented in the map
        self.x = x
        self.y = y
        

        super().__init__(direction, isDead, state, x, y, width, height, speed, health, element, img_path)

        #self.fireball_image = pygame.image.load("asteroid-04.png")
        #self.fireball_rect = self.fireball_image.get_rect()


    # def throwFireball(self):
    #     # Throw "fireballs" randomly
    #     if randint(0, 100) < 5:
    #         self.fireball_rect.center = (self.x + 50, self.y + 50) # Set the center of the fireball rect
    #         return self.fireball_rect # Return the rect object to add to the game
    #     return None

