import pygame, sys
from Button import *

class EngineCutscene:
    def __init__(self, bg_path):
                # Set up Pygame window
        self.bgImg = pygame.image.load(bg_path)
        self.bgImgScaled = pygame.transform.scale(self.bgImg, (1280,720))
        self.bgImg_rect = self.bgImgScaled.get_rect()

        self.screen = pygame.display.set_mode((self.bgImg_rect.width, self.bgImg_rect.height))
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.SysFont('corbeli.ttf', 25)
        self.paragraph = 'You found the Engine Reactor! Time to face the final boss and finally go home!'
        self.text = self.font.render(self.paragraph, True, (255,255,255)) 
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.screen.get_width()/2, self.screen.get_height()/2)
        #x and y locations
        self.text_x = self.text_rect.x
        self.text_y = self.text_rect.y

        #prompt continue
        self.textprompt = self.font.render('[Press spacebar to face the Final Boss]', True, (255,255,255)) 
        self.textprompt_rect = self.textprompt.get_rect()
        self.textprompt_rect.center = (self.screen.get_width()/2, self.screen.get_height()/2)
        #x and y locations
        self.textprompt_x = self.textprompt_rect.x
        self.textprompt_y = self.textprompt_rect.y


        #splitting paragraphs into multiple lines
        self.words = self.paragraph.split()
        self.lines = [""]
        for word in self.words:
            if self.font.size(self.lines[-1] + word)[0] < self.screen.get_width()-500:
                self.lines[-1] += f" {word}"
            else:
                self.lines.append(word)
                
        self.rendered_lines = [self.font.render(line.strip(), True, (255, 255, 255)) for line in self.lines]
        
        #Engine reactor image
        self.engine_image = pygame.image.load('EnginePart.png')
        self.engine_image_rect = self.engine_image.get_rect()

        #attributes for fade in
        self.alpha = 0
        self.alpha_values = [0 for a in range(len(self.lines))]

    #fade in text
    def fade_in(self):
        if self.alpha < 255:
                self.alpha += 1
                for i, surface in enumerate(self.rendered_lines):
                    self.alpha_values[i] += 1
                    surface.set_alpha(self.alpha_values[i])

                self.screen.blit(self.bgImgScaled, self.bgImg_rect)
                text_y = 160
                for surface in self.rendered_lines:
                    self.screen.blit(surface, (250, text_y))
                    text_y += surface.get_height() + 10
                pygame.display.update()

        else:
            #Draw the background image and text
            self.screen.blit(self.bgImgScaled, self.bgImg_rect)
            text_y = 160
            for i, surface in enumerate(self.rendered_lines):
                surface.set_alpha(self.alpha_values[i])
                self.screen.blit(surface, (250, text_y))
                text_y += surface.get_height() + 10
            self.screen.blit(self.textprompt, (self.textprompt_rect.centerx - 110, 550))
            self.screen.blit(self.engine_image, (640, 360))

       

    def cutscene_loop(self):
        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
            
            self.fade_in()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                running = False
            
            #Update display
            pygame.display.flip()