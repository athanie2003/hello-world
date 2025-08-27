import pygame

#A class that takes the x position, y postion, width, height and speed of the character
class Characters(): 
    def __init__(self, x, y, width, height, health, img_path):
        self.image = pygame.image.load(img_path)
        self.health = health
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height  
        self.rect.center = (x, y)
    
    #the movement of the character (left, right, up, down)
    def updatePosition(self, keys_pressed, imageLeft, imageRight, imageUp, imageDown):
        if keys_pressed[pygame.K_LEFT]:
            self.image = pygame.image.load(imageLeft)
            self.rect.x -= self.speed    #left
            print("User is moving left")
            print("Image left")
            if self.rect.x < -55:
                self.rect.x = -55
        if keys_pressed[pygame.K_RIGHT]:   
            self.image = pygame.image.load(imageRight) 
            self.rect.x += self.speed    #right
            print("User is moving right")
            print("Image right")
            if self.rect.x > 1200:
                self.rect.x = 1200
        if keys_pressed[pygame.K_UP]:
            self.image = pygame.image.load(imageUp)
            self.rect.y -= self.speed    #up
            print("User is moving up")
            print("Image up")
            if self.rect.y < 238:
                self.rect.y = 238
                print("reached end of Y bounds")
        if keys_pressed[pygame.K_DOWN]:
            self.image = pygame.image.load(imageDown)
            self.rect.y += self.speed    #down
            print("User is moving down")
            print("Image down")
            if self.rect.y > 366:
                self.rect.y = 366
                print("reached end of Y bounds")


    def getRect(self):
        # Create a Rect object for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return self.rect
    
        #the movement of the character (left, right, up, down)
    def updatePositionFB(self, keys_pressed, imageLeft, imageRight, imageUp, imageDown):
        self.image_original = pygame.image.load(imageDown)
        self.image = pygame.transform.scale2x(self.image_original)
        if keys_pressed[pygame.K_LEFT]:
            self.image_original = pygame.image.load(imageLeft)
            self.image = pygame.transform.scale2x(self.image_original)
            self.rect.x -= self.speed    #left
        if keys_pressed[pygame.K_RIGHT]:   
            self.image_original = pygame.image.load(imageRight)
            self.image = pygame.transform.scale2x(self.image_original)
            self.rect.x += self.speed    #right
        if keys_pressed[pygame.K_UP]:
            self.image_original = pygame.image.load(imageUp)
            self.image = pygame.transform.scale2x(self.image_original)
            self.rect.y -= self.speed    #up
        if keys_pressed[pygame.K_DOWN]:
            self.image_original = pygame.image.load(imageDown)
            self.image = pygame.transform.scale2x(self.image_original)
            self.rect.y += self.speed    #down
            
