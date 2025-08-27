import pygame
from Enemies import Enemies

class LevelBosses(Enemies):
    def __init__(self, x, y, width, height, health, element, img_path):
        super().__init__(x, y, width, height, health, img_path)
        self.element = element
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()  
        self.rect.center = (x, y)


    def hit(self, damage):
        self.health -= damage
        