import pygame, sys

from Characters import Characters
from MainCharacter import MainCharacter
from Button import *
from FinalBoss import *



class VictoryScreen:
  
    def vScreenLoop(called):

        bgImg = pygame.image.load('victory-screen.png')
        bgImgScaled = pygame.transform.scale(bgImg, (1280,720))
        bgImg_rect = bgImgScaled.get_rect()

        screen = pygame.display.set_mode((bgImg_rect.width, bgImg_rect.height))
        screen_rect = screen.get_rect()

        width = screen.get_width()
        height = screen.get_height()


        button_width = 0.2 * width
        button_height = 0.1 * height
        button_x = (width - button_width) / 2
        button_y = (height - button_height) / 2 + 200
        color = (255,255,255)
        color_light = (170,170,170)
        color_dark = (100,100,100)

        quitBtn = Button(screen, color_light, color_dark, button_x, button_y, button_width, button_height, 'Quit', color, 'FORCED SQUARE.ttf', 35)



        smallFont = pygame.font.Font('FORCED SQUARE.ttf', 100)
        #text = smallFont.render('HELLO WORLD', True, (255,45,115))
        #text_rect = text.get_rect()
        #text_rect.center = (width/2, height/2) #set center of text
        #x and y locations
        #text_x = text_rect.x
        #text_y = text_rect.y-200

        clicked = False


        def render():
            screen.blit(bgImgScaled, bgImg_rect)
            mouse = pygame.mouse.get_pos() 

            if called is True:
                if(not clicked):
                    
                    quitBtn.draw(mouse)
                    #screen.blit(text, (text_x,text_y))
    
            pygame.display.flip()


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()

                        if quitBtn.is_clicked(mouse):
                            sys.exit()
            render()
            pygame.display.update()   

    pygame.quit()


