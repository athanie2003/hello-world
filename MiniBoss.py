import pygame, sys 
from Enemies import Enemies as MB



class MiniBoss(MB):
    def __init__(self, x, y, width, height, health, img_path, bg_path):
        self.bgImg = pygame.image.load(bg_path)
        self.bgImgScaled = pygame.transform.scale(self.bgImg, (1280,720))
        self.bgImg_rect = self.bgImgScaled.get_rect()

        self.screen = pygame.display.set_mode((self.bgImg_rect.width, self.bgImg_rect.height))
        self.screen_rect = self.screen.get_rect()
        self.check = 0


        super().__init__(x, y, width, height, health, img_path)
        self.MiniBoss_image = pygame.image.load(img_path).convert_alpha()
        self.MiniBoss_image = pygame.transform.scale(self.MiniBoss_image, (width,height))
        self.MiniBoss_rect = self.MiniBoss_image.get_rect()
        self.MiniBoss_rect.x = x
        self.MiniBoss_rect.y = y
        self.MiniBoss_rect.center = (x, y)

        self.font = pygame.font.SysFont("corbeli.ttf", 30)
        self.isDead = False
    
    def dialogue (self, statement):
        text_surface = self.font.render(f"{statement}", True, (255, 255, 255)) 

        self.screen.blit(text_surface, (self.MiniBoss_rect.centerx - text_surface.get_width()//2, self.MiniBoss_rect.y + self.MiniBoss_rect.height)) 
    
        pygame.display.flip()

    def interact(self, mainCharacter_rect, statement, mc):
        if self.MiniBoss_rect.colliderect(mainCharacter_rect):
            
            # textprompt_surface = self.font.render(f"Click spacebar to interact", True, (255, 255, 255))
            # self.screen.blit(textprompt_surface, (self.MiniBoss_rect.centerx - textprompt_surface.get_width()//2, self.MiniBoss_rect.y - textprompt_surface.get_height()))
          
            self.check += 1
    
    def collide(self, other):
        return self.rect.colliderect(other)

    def draw(self, screen, imageLeft, imageRight, imageUp, imageDown, mc):
        screen.blit(self.MiniBoss_image, self.MiniBoss_rect)
        screen.blit(mc.image, mc.rect)
        mc.updatePosition(pygame.key.get_pressed(), imageLeft, imageRight, imageUp, imageDown)
        self.interact(mc.rect, 'Here take this!', mc)

    def path_loop(self, imageLeft, imageRight, imageUp, imageDown, mc):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
       
            if self.check > 0:
                    running = False

            self.screen.blit(self.bgImgScaled, self.bgImg_rect)

            self.draw(self.screen, imageLeft, imageRight, imageUp, imageDown, mc)

            pygame.display.flip()