import pygame
from Characters import Characters as Char


class MainCharacter(Char):
    #constructor
    def __init__(self, x, y, width, height, speed, health, element, img_path):   
        super().__init__(x, y, width, height, health, img_path)
        
        # self.width = width
        # self.height = height
        self.speed = speed
        # self.health = health
        self.element = element
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center = self.rect.center)
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height

    def dead(self, screen):
        image = pygame.image.load("StartMenuBackground.jpg")
        screen.blit(image, (0, 0))
        pygame.display.flip()

#location of character after screen change
    def pos_display(self, x_pos, y_pos):
        self.width = x_pos
        self.height = y_pos