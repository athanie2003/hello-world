import pygame, Button, random, sys

class Battle():
    def __init__(self, total_health, attack_power, elemental_attack_power, mc, levelBoss, screen, color_light, color_dark, x, y, width, height, text1, text2, text3, text_color, font_name, font_size):
        self.total_health = total_health
        self.attack_power = attack_power
        self.elemental_attack_power = elemental_attack_power
        self.mc = mc
        self.mc.health = total_health
        self.mc.x = 200
        self.mc.y = screen.get_height() - mc.rect.height - 300
        self.levelBoss = levelBoss
        self.levelBoss.health = 25
        self.lbHealth = 25
        self.levelBoss.x = 945
        self.levelBoss.y = screen.get_height() - levelBoss.rect.height - 300
        self.screen = screen
        self.hit_sound = pygame.mixer.Sound('hitSound.wav')
        self.win_sound = pygame.mixer.Sound('explosion.wav')
        self.lose_sound = pygame.mixer.Sound('loss.wav')
        self.heal_sound = pygame.mixer.Sound('heal.wav')


        #title
        self.font = pygame.font.Font('FORCED SQUARE.ttf', 75)
        self.text = self.font.render('MINI BOSS BATTLE', True, (255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (screen.get_width()/2, screen.get_height()/2)
        #x and y locations
        self.text_x = self.text_rect.x
        self.text_y = self.text_rect.y-300

        #prompt user to choose options
        self.fontprompt = pygame.font.Font('FORCED SQUARE.ttf', 40)
        self.textprompt = self.fontprompt.render('What will you do?', True, (255,255,255))
        self.textprompt_rect = self.textprompt.get_rect()
        self.textprompt_rect.center = (screen.get_width()/2, screen.get_height()/2)
        #x and y locations
        self.textprompt_x = self.textprompt_rect.x
        self.textprompt_y = self.textprompt_rect.y+200

        #player health
        self.fonthealth = pygame.font.Font('FORCED SQUARE.ttf', 30)
        self.playertext = self.fonthealth.render('Health: '+str(self.mc.health)+'/'+f'{self.total_health}', True, (0,255,0))
        self.playertext_rect = self.playertext.get_rect()
        self.playertext_rect.center = (screen.get_width()/2, screen.get_height()/2)
        #x and y locations
        self.playertext_x = self.playertext_rect.x - 365
        self.playertext_y = self.playertext_rect.y - 100

        #enemy health
        self.enemytext = self.fonthealth.render('Health: '+str(self.levelBoss.health)+'/'+str(self.lbHealth), True, (0,255,0))
        self.enemytext_rect = self.enemytext.get_rect()
        self.enemytext_rect.center = (screen.get_width()/2, screen.get_height()/2)
        #x and y locations
        self.enemytext_x = self.enemytext_rect.x + 365
        self.enemytext_y = self.enemytext_rect.y - 100

        #buttons
        self.attackBtn = Button.Button(screen, color_light, color_dark, x, y, width, height, text1, text_color, font_name, font_size)
        self.healBtn = Button.Button(screen, color_light, color_dark, x+width+5, y, width, height, text2, text_color, font_name, font_size)
        self.elemental_attackBtn = Button.Button(screen, color_light, color_dark, x+width/4+15, y+height+5, width+50, height, text3, text_color, font_name, font_size)
        self.proceedBtn = Button.Button(screen, color_light, color_dark, x+width/4+15, y, width, height, 'Proceed', text_color, 'FORCED SQUARE.ttf', 35)
        self.retryBtn = Button.Button(screen, color_light, color_dark, x+width/4+15, y, width, height, 'Retry', text_color, 'FORCED SQUARE.ttf', 35)
        self.quitBtn = Button.Button(screen, color_light, color_dark, x+width/4+15, y+height+5, width, height, 'Quit', text_color, 'FORCED SQUARE.ttf', 35)

    #updates text
    def update(self, text):
        self.textprompt = self.fontprompt.render(text, True, (255,255,255))

    #attack option
    def attack(self, mouse):
        if self.attackBtn.is_clicked(mouse):
            self.hit_sound.play()
            self.update('Attacking Enemy')
            print("PLayer has attacked")
            self.levelBoss.hit(2+self.attack_power) #deduct health from mini boss

            if self.levelBoss.health <= 0:
                self.win_sound.play()
                self.levelBoss.health = 0
                self.update('You Win!')
                self.enemytext = self.fonthealth.render('Health: '+str(self.levelBoss.health)+'/'+str(self.lbHealth), True, (0,255,0))
            self.enemytext = self.fonthealth.render('Health: '+str(self.levelBoss.health)+'/'+str(self.lbHealth), True, (0,255,0))

    #elemental attack option
    def elemental_attack(self, mouse):            
        if self.elemental_attackBtn.is_clicked(mouse):
            self.hit_sound.play()
            #checks element
            if self.mc.element == 'fire' and self.levelBoss.element == 'earth' or self.mc.element == 'water' and self.levelBoss.element == 'fire' or self.mc.element == 'earth' and self.levelBoss.element == 'water':
                self.levelBoss.hit(3+self.elemental_attack_power) #stronger attack
                self.update('Elemental Attack: Strong')

            elif self.mc.element == 'fire' and self.levelBoss.element == 'water' or self.mc.element == 'water' and self.levelBoss.element == 'earth' or self.mc.element == 'earth' and self.levelBoss.element == 'fire':
                self.levelBoss.hit(1+self.elemental_attack_power) #weaker attack
                self.update('Elemental Attack: Weak')

            elif self.mc.element == 'fire' and self.levelBoss.element == 'fire' or self.mc.element == 'water' and self.levelBoss.element == 'water' or self.mc.element == 'earth' and self.levelBoss.element == 'earth':
                self.levelBoss.hit(2+self.elemental_attack_power) #normal attack
                self.update('Elemental Attack: Normal')

            if self.levelBoss.health <= 0:
                self.win_sound.play()
                self.levelBoss.health = 0
                self.update('You Win!')
                self.enemytext = self.fonthealth.render('Health: '+str(self.levelBoss.health)+'/'+str(self.lbHealth), True, (0,255,0))
            self.enemytext = self.fonthealth.render('Health: '+str(self.levelBoss.health)+'/'+str(self.lbHealth), True, (0,255,0))
    
    #heal option
    def heal(self, mouse):
        if self.healBtn.is_clicked(mouse):
            if self.mc.health >= self.total_health:
                self.mc.health = self.total_health
                self.update('Health is full!')
            else:
                self.heal_sound.play()
                self.mc.health += 3 #heal by 3 points
                if self.mc.health >= self.total_health:
                    self.mc.health = self.total_health
                    self.update('Health is full')
                else:
                    self.update('Healed')
                    print("Player was healed")
        self.playertext = self.fonthealth.render('Health: '+str(self.mc.health)+'/'+f'{self.total_health}', True, (0,255,0))

    #enemy turn
    def take_damage(self):
        self.hit_sound.play()
        self.mc.health -= random.randint(1, 4)
        self.playertext = self.fonthealth.render('Health: '+str(self.mc.health)+'/'+f'{self.total_health}', True, (0,255,0))
        self.update('Enemy Attacks')
        print("Player took damage")

        if self.mc.health <= 0:
            self.lose_sound.play()
            self.mc.health = 0
            self.playertext = self.fonthealth.render('Health: '+str(self.mc.health)+'/'+f'{self.total_health}', True, (255,0,0))
            self.update('You Lose!')

    #render battle
    def battle_render(self, screen, mouse, bgImgScaled, bgImg_rect):
        #health colour of player
        if self.mc.health <= 14 and self.mc.health > 9:
            self.playertext = self.fonthealth.render('Health: '+str(self.mc.health)+'/'+f'{self.total_health}', True, (255,193,0))

        elif self.mc.health <= 9 and self.mc.health > 5:
            self.playertext = self.fonthealth.render('Health: '+str(self.mc.health)+'/'+f'{self.total_health}', True, (255,116,0))

        elif self.mc.health <= 5:
            self.playertext = self.fonthealth.render('Health: '+str(self.mc.health)+'/'+f'{self.total_health}', True, (255,0,0))

        elif self.mc.health > 14:
            self.playertext = self.fonthealth.render('Health: '+str(self.mc.health)+'/'+f'{self.total_health}', True, (0,255,0))

        #health colour of mini boss
        if self.levelBoss.health <= 14 and self.levelBoss.health > 9:
            self.enemytext = self.fonthealth.render('Health: '+str(self.levelBoss.health)+'/'+str(self.lbHealth), True, (255,193,0))

        elif self.levelBoss.health <= 9 and self.levelBoss.health > 5:
            self.enemytext = self.fonthealth.render('Health: '+str(self.levelBoss.health)+'/'+str(self.lbHealth), True, (255,116,0))

        elif self.levelBoss.health <= 5:
            self.enemytext = self.fonthealth.render('Health: '+str(self.levelBoss.health)+'/'+str(self.lbHealth), True, (255,0,0))

        elif self.levelBoss.health > 14:
            self.enemytext = self.fonthealth.render('Health: '+str(self.levelBoss.health)+'/'+str(self.lbHealth), True, (0,255,0))

        screen.blit(bgImgScaled, bgImg_rect)
        self.attackBtn.draw(mouse)
        self.elemental_attackBtn.draw(mouse)
        self.healBtn.draw(mouse)
        screen.blit(self.mc.image, (self.mc.x, self.mc.y))
        screen.blit(self.levelBoss.image, (self.levelBoss.x, self.levelBoss.y))
        screen.blit(self.text, (self.text_x, self.text_y))
        screen.blit(self.textprompt, (self.textprompt_x, self.textprompt_y))
        screen.blit(self.playertext, (self.playertext_x, self.playertext_y))
        screen.blit(self.enemytext, (self.enemytext_x, self.enemytext_y))
        pygame.display.flip()

    #render battle win
    def battleWin_render(self, screen, mouse, bgImgScaled, bgImg_rect):
        screen.blit(bgImgScaled, bgImg_rect)
        screen.blit(self.mc.image, (self.mc.x, self.mc.y))
        screen.blit(self.textprompt, (self.textprompt_x+80, self.textprompt_y-300))
        screen.blit(self.text, (self.text_x, self.text_y))
        screen.blit(self.playertext, (self.playertext_x, self.playertext_y))
        self.proceedBtn.draw(mouse)
        pygame.display.flip()


    #render battleloss
    def battleLoss_render(self, screen, mouse, bgImgScaled, bgImg_rect):
        self.update('You Lose')
        screen.blit(bgImgScaled, bgImg_rect)
        screen.blit(self.levelBoss.image, (self.levelBoss.x, self.levelBoss.y))
        screen.blit(self.textprompt, (self.textprompt_x+80, self.textprompt_y-300))
        screen.blit(self.text, (self.text_x, self.text_y))
        screen.blit(self.enemytext, (self.enemytext_x, self.enemytext_y))
        self.retryBtn.draw(mouse)
        self.quitBtn.draw(mouse)
        pygame.display.flip()
        
    def battle_gameloop(self, mouse, bgImgScaled, bgImg_rect):
        running = True
        click = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    mouse = pygame.mouse.get_pos()
        
                    if self.attackBtn.is_clicked(mouse):
                            self.attack(mouse)
                            click = True
                    elif self.healBtn.is_clicked(mouse):
                            self.heal(mouse)
                            click = True
                    elif self.elemental_attackBtn.is_clicked(mouse):
                            self.elemental_attack(mouse)
                            click = True

                    if self.levelBoss.health <= 0:
                        running = False
                        click = False
                        
            
            self.battle_render(self.screen, mouse, bgImgScaled, bgImg_rect)
            pygame.display.update()

            #waits after button is clicked
            if click:
                check = pygame.time.get_ticks()
                while pygame.time.get_ticks() - check < 1000:
                    #1 second pause
                    pass
                self.take_damage()
                self.battle_render(self.screen, mouse, bgImgScaled, bgImg_rect)
                pygame.display.update()

                #asks user the question
                while pygame.time.get_ticks() - check < 2000:
                    #1 second pause
                    pass
                self.update('What will you do?')
                self.battle_render(self.screen, mouse, bgImgScaled, bgImg_rect)
                pygame.display.update()
                click = False
            if self.mc.health <= 0:
                    running = False


    def battleWin_gameloop(self, mouse, bgImgScaled, bgImg_rect):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if self.proceedBtn.is_clicked(mouse):
                        running = False
            self.battleWin_render(self.screen, mouse, bgImgScaled, bgImg_rect)


    def battleLoss_gameloop(self, mouse, bgImgScaled, bgImg_rect):
        running = True
        while running:
            keys_pressed = pygame.key.get_pressed() # stores state of all keys
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if self.retryBtn.is_clicked(mouse):
                        self.mc.health = 20
                        self.levelBoss.health = 20
                        running = False
                    elif self.quitBtn.is_clicked(mouse):
                        running = False
                        sys.exit()
            self.battleLoss_render(self.screen, mouse, bgImgScaled, bgImg_rect)
