import pygame, math
from Characters import Characters


class FinalBoss(Characters):
    def __init__(self, x, y, width, height, speed, health, element, img_path):   
        super().__init__(x, y, width, height, health, img_path)
        
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.element = element
        self.image_original = pygame.image.load(img_path)
        self.image = pygame.transform.scale2x(self.image_original)
        self.rect = self.image.get_rect(center = self.rect.center)
        self.rect_center = self.rect.centerx

    def collide(self, other):
        return self.rect.colliderect(other)
    
    def update(self):
        self.rect.x += self.speed



class PlayerShip(Characters):
    def __init__(self, x, y, width, height, speed, health, element, img_path):
        super().__init__(x, y, width, height, health, img_path)

        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.element = element
        self.image_original = pygame.image.load(img_path)
        self.image = pygame.transform.scale2x(self.image_original)
        self.rect = self.image.get_rect(center = self.rect.center)
        self.rect_center = self.rect.centerx

    def collide(self, other):
        return self.rect.colliderect(other)
    
    def updatePosition(self, keys_pressed):
        return super().updatePosition(keys_pressed)

class PlayerBullet(Characters):
    def __init__(self, x, y, width, height, speed, health, element, img_path):
        super().__init__(x, y, width, height, health, img_path)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.element = element
        self.image_original = pygame.image.load(img_path)
        self.image = pygame.transform.scale2x(self.image_original)
        self.rect = self.image.get_rect(center = self.rect.center)
        self.rect_center = self.rect.centerx

    def collide(self, other):
        return self.rect.colliderect(other)

    def update(self):
        self.rect.y -= self.speed

class BossBullet(Characters):
    def __init__(self, x, y, width, height, speed, health, element, img_path, targetx, targety):
        super().__init__(x, y, width, height, health, img_path)
        self.x = x
        self.y = y
        angle = math.atan2(targety-self.y, targetx-self.x)
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.element = element
        self.image_original = pygame.image.load(img_path)
        self.image = pygame.transform.scale2x(self.image_original)
        self.rect = self.image.get_rect(center = self.rect.center)
        self.rect_center = self.rect.centerx

    def collide(self, other):
        return self.rect.colliderect(other)

    
    def update(self):
        self.rect.y += self.speed
        self.rect.x += int(self.dx)

class Asteroid(Characters):
    def __init__(self, x, y, width, height, speed, health, element, img_path):
        super().__init__(x, y, width, height, health, img_path)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.element = element
        self.image_original = pygame.image.load(img_path)
        self.image = pygame.transform.scale2x(self.image_original)
        self.rect = self.image.get_rect(center = self.rect.center)
        self.rect_center = self.rect.centerx

    def collide(self, other):
        return self.rect.colliderect(other)

    def update(self):
        self.rect.y += self.speed