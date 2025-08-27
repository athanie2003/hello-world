import pygame, random


class TerrainObject(pygame.sprite.Sprite):
    def __init__(self,x,y,img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        #image_scaled = pygame.transform.scale_by(self.image, (3,3))
        self.rect = self.image.get_rect()  
        self.rect.center = (x,y)

class Tree1(TerrainObject):
    def __init__(self):
        super().__init__("tree-1.png")
        
class Tree2(TerrainObject):
    def __init__(self):
        super().__init__("tree-2.png")
        
class Rock1(TerrainObject):
    def __init__(self, screen_rect):
        rand_x = random.randint(0,screen_rect.width)
        rand_y = random.randint(0,screen_rect.height)
        super().__init__(rand_x, rand_y,"rock-1.png")
        
class Rock2(TerrainObject):
    def __init__(self, screen_rect):
        rand_x = random.randint(0,screen_rect.width)
        rand_y = random.randint(0,screen_rect.height)
        super().__init__(rand_x, rand_y, "rock-2.png")
        
class Bush1(TerrainObject):
    def __init__(self, screen_rect):
        rand_x = random.randint(0,screen_rect.width)
        rand_y = random.randint(0,screen_rect.height)
        super().__init__(rand_x, rand_y, "bush-1.png")

class Bush2(TerrainObject):
    def __init__(self, screen_rect):
        rand_x = random.randint(0,screen_rect.width)
        rand_y = random.randint(0,screen_rect.height)
        super().__init__(rand_x, rand_y,"bush-2.png")

class TreeCluster(TerrainObject):
    def __init__(self):
        super().__init__("tree-cluster.png")
        