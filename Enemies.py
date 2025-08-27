import pygame
from enum import Enum
from Characters import Characters

class State(Enum):
    ALIVE = 1
    HIT = 2
    DEAD = 3

class Enemies(Characters):
    def __init__(self, x, y, width, height, health, img_path, direction=None, isDead=False, state=State.ALIVE):
        super().__init__(x, y, width, height, health, img_path)
        self.direction = direction
        self.isDead = isDead
        self.state = state

    def move(self, dx, dy):
        self.updatePosition()  # Call updatePosition() from superclass
        self.x += dx
        self.y += dy
        self.rect.x = self.x
        self.rect.y = self.y
        
    def detectCollision(self):
        self.state = State(self.state.value + 1)

    def die(self):
        self.isDead = True
        self.img_path = ''  # Remove the image path
        print("Defeated!")