import pygame

#class that pauses or un-pauses the game
class Paused:
    #constructor (initially not paused)
    def __init__(self): 
        self.paused = False
    #method that set the game to pause
    def currentlyPaused(self):
        self.paused = True
        #while paused...
        while self.paused: 
            for event in pygame.event.get():
                #...you can quit the game or...
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #...press the spacebar to un-pause the game
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.paused = False
