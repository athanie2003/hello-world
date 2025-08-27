import pygame

from Characters import Characters
from MainCharacter import MainCharacter as MC
from Button import *
from Start import *
from LevelBosses import LevelBosses as LB
from Battle import *
from random import randint

map_Displayed = False

#BG image
bg_img = pygame.image.load('progression map.png')
bg_rect = bg_img.get_rect()
#Screen
screen = pygame.display.set_mode((bg_rect.width, bg_rect.height))
screen_rect = screen.get_rect()

screen_width = screen.get_width()
screen_height = screen.get_height()

screen = pygame.display.set_mode((bg_rect.width, bg_rect.height))
screen_rect = screen.get_rect()
#Close Button
color = (255,255,255) #Color rgb code
closeBtnX = 100
closeBtnY = 100

#Import font and add text
pygame.font.init()
font = pygame.font.Font('FORCED SQUARE.ttf', 50) #Font and font size

#MC LOCATION SETTER
stage = 1

#MAIN CHARACTER
mc = MC(screen_rect.centerx, screen_rect.centery, 50, 50, 5, 20, '','astronaut.png')

#CLOSE BUTTON
button_width = 0.2 * screen_width
button_height = 0.1 * screen_height
button_x = (screen_width - button_width) / 2 + 505
button_y = (screen_height - button_height) / 2 + 315
color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
closeBtn = Button.Button(screen, color_light, color_dark, button_x, button_y, button_width, button_height, 'CLOSE', color, 'FORCED SQUARE.ttf', 35)

#TITLE TEXT
smallFont = pygame.font.Font('FORCED SQUARE.ttf', 100)
text = smallFont.render('PROGRESSION MAP', True, (255,45,115))
text_rect = text.get_rect()
text_rect.center = (screen_width/2, screen_height/2) #set center of text
#x and y locations
text_x = 10
text_y = 0

#Mouse Info
clicked = False

#MC LOCATION SETTER
stage = 1
if stage == 1:
    mc_x = 70
    mc_y = 350
elif stage == 2:
    mc_x = 315
    mc_y = 200
elif stage == 3:
    mc_x = 595
    mc_y = 350


def IsMapDisplayed():
    if map_Displayed:
        return True



def render():
    mouse = pygame.mouse.get_pos()
    screen.blit(bg_img, bg_rect)
    
    #draws button only when it is not clicked
    if(not clicked):
        closeBtn.draw(mouse)
        screen.blit(text, (text_x,text_y))

    #Display the character's location
    screen.blit(mc.image, (mc_x, mc_y))

    pygame.display.flip()

render()

def display():
    map_Displayed = True
    if map_Displayed:
        pygame.init()
        render()
        running = True
        while running:
            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if closeBtn.is_clicked(mouse):
                        running = False
                        
        pygame.display.update()

render()


#Running the progression map
display()


pygame.quit()