import pygame, sys
from Enemies import Enemies as Enemy



class FriendlyAlien(Enemy):
    def __init__(self, x, y, width, height, health, img_path, bg_path):
        # Set up the Pygame window
        self.bg_path = bg_path
        self.bgImg = pygame.image.load(self.bg_path)
        self.bgImgScaled = pygame.transform.scale(self.bgImg, (1280,720))
        self.bgImg_rect = self.bgImgScaled.get_rect()

        self.screen = pygame.display.set_mode((self.bgImg_rect.width, self.bgImg_rect.height))
        self.screen_rect = self.screen.get_rect()
        self.check = 0
        
        super().__init__(x, y, width, height, health, img_path)
        self.friendlyAlien_image = pygame.image.load(img_path).convert_alpha()
        self.friendlyAlien_image = pygame.transform.scale(self.friendlyAlien_image, (width,height))
        self.friendlyAlien_rect = self.friendlyAlien_image.get_rect()
        self.friendlyAlien_rect.x = x
        self.friendlyAlien_rect.y = y
        self.friendlyAlien_rect.center = (x, y)

        # choose the font and size you want to use
        self.font = pygame.font.SysFont("corbeli.ttf", 30)
        self.isDead = False

        self.pickup = pygame.mixer.Sound('pickup.wav')
    
    def dialogue(self, statement):
        text_surface = self.font.render(f"{statement}", True, (255, 255, 255)) # choose the color you want to use

        # blit the text surface onto the screen
        self.screen.blit(text_surface, (self.friendlyAlien_rect.centerx - text_surface.get_width()//2, self.friendlyAlien_rect.y + self.friendlyAlien_rect.height)) #centers the text above the FriendlyAlien sprite
    
    
        # update the display
        pygame.display.flip()

    def interact(self, mainCharacter_rect, statement):
        if self.friendlyAlien_rect.colliderect(mainCharacter_rect):
            textprompt_surface = self.font.render(f"Hold spacebar to interact", True, (255, 255, 255))
            self.screen.blit(textprompt_surface, (self.friendlyAlien_rect.centerx - textprompt_surface.get_width()//2, self.friendlyAlien_rect.y - textprompt_surface.get_height()))
          
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                #friendly alien says any statement of choice 
                self.dialogue(statement)
                if self.check < 1:
                    print("NPC has been interacted with")
                    self.pickup.set_volume(0.5)
                    self.pickup.play()

                self.check += 1

    def draw(self, screen, imageLeft, imageRight, imageUp, imageDown, mc):
        screen.blit(self.friendlyAlien_image, self.friendlyAlien_rect)
        screen.blit(mc.image, mc.rect)
        mc.updatePosition(pygame.key.get_pressed(), imageLeft, imageRight, imageUp, imageDown)
        self.interact(mc.rect, 'I give you this element: '+f"{mc.element}")
    


    def path_loop(self, imageLeft, imageRight, imageUp, imageDown, mc):
        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
       
            if mc.rect.x == 1200 and self.check > 0:
                    running = False

            # Draw the background image
            self.screen.blit(self.bgImgScaled, self.bgImg_rect)

            # Draw the friendly alien on the screen
            self.draw(self.screen, imageLeft, imageRight, imageUp, imageDown, mc)

            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_m]:
                mapImg = pygame.image.load('progression map.png')
                mapImg = pygame.transform.scale(mapImg, (640, 360))
                mapImg_rect = mapImg.get_rect()
                self.screen.blit(mapImg, (self.screen_rect.width-mapImg_rect.width, mapImg_rect.y))
                mcImg = mc.image
                if self.bg_path == 'First level.png':
                    self.screen.blit(mcImg, (640, 150))
                elif self.bg_path == 'Second Level.png':
                    self.screen.blit(mcImg, (765, 80))
                elif self.bg_path == 'Third Level.png':
                    self.screen.blit(mcImg, (900, 150))

            # Update the display
            pygame.display.flip()