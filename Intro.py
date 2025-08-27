import pygame, sys
from Button import *

class Intro:
    def __init__(self, bg_path):
                # Set up Pygame window
        self.bgImg = pygame.image.load(bg_path)
        self.bgImgScaled = pygame.transform.scale(self.bgImg, (1280,720))
        self.bgImg_rect = self.bgImgScaled.get_rect()

        self.screen = pygame.display.set_mode((self.bgImg_rect.width, self.bgImg_rect.height))
        self.screen_rect = self.screen.get_rect()

        

        self.font = pygame.font.SysFont('corbeli.ttf', 25)
        self.paragraph = 'Welcome to your space mission. Your mission is to research the surrounding planets for more efficient forms of energy that you can bring back to your planet. As you navigate through space, your ship is suddenly struck by a meteorite, causing it to spiral out of control and crash onto an unidentified planet. You wake up to find yourself alone, stranded on an unknown world with a damaged spaceship. The only way to repair your ship and return home is to find the missing engine reactor that was somehow lost in the crash. However, the planet you\'ve crashed on is full of mystery and potential danger. You must use all your skills and knowledge to navigate through the unknown world, facing various obstacles and challenges along the way. As you embark on your adventure, you\'ll discover the secrets of the planets and unravel the mysteries that lie within. Your survival instincts will be put to the test as you encounter new creatures, unexpected terrain, and treacherous weather conditions. Do you have what it takes to find the missing parts, repair your ship, and make it back home safely? The fate of your space mission is in your hands... (Use arrow keys to move and \'m\' to view map)'
        self.text = self.font.render(self.paragraph, True, (255,255,255)) 
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.screen.get_width()/2, self.screen.get_height()/2)
        #x and y locations
        self.text_x = self.text_rect.x
        self.text_y = self.text_rect.y

        #prompt continue
        self.textprompt = self.font.render('[Press spacebar to continue]', True, (255,255,255)) 
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
        
       

    def intro_loop(self):
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