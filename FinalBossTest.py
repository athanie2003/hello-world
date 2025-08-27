#TO BE DELETED LATER

import pygame
import FinalBossObjects
import random
#import FinalBossMap

#Start Pygame
pygame.init()

#SCREEN STUFF
clock = pygame.time.Clock()
bgImg = pygame.image.load('finalbossbg.png')
bgImgScaled = pygame.transform.scale(bgImg, (1280,720))
bgImg_rect = bgImgScaled.get_rect()
screen_x = 960
screen_y = 720
screen = pygame.display.set_mode((screen_x, screen_y))
screen_rect = screen.get_rect()
width = screen.get_width()
height = screen.get_height()

#FINAL BOSS SHIP
boss_x = screen_x / 2
boss_y = 50
boss_image_path = 'final-boss.png'
boss = FinalBossObjects.FinalBoss(boss_x, boss_y, 50, 50, 2, 150, '', boss_image_path)

#BOSS HP
boss_health = boss.health

#PLAYER SHIP
player_x = screen_x / 2
player_y = screen_y / 2 + 200
player_image_path = 'player-ship.png'
player_left_path = 'ship-left.png'
player_right_path = 'ship-right.png'
player = FinalBossObjects.PlayerShip(player_x, player_y, 50, 50, 3, 10, '', player_image_path)

#PLAYER HP 
player_health = player.health

#ASTEROIDS
a1_img = 'asteroid-01.png'
a2_img = 'asteroid-02.png'
a3_img = 'asteroid-03.png'
a4_img = 'asteroid-04.png'
a5_img = 'asteroid-05.png'
asteroids = []

#BULLETS
player_bullets = []
boss_bullets_middle = []
boss_bullets_left = []
boss_bullets_right = []

#FONT
font = pygame.font.Font('FORCED SQUARE.ttf', 24)



#RENDER SCREEN       
def render():
    #Blit bg
    screen.blit(bgImgScaled, bgImg_rect)

    #Blit boss
    screen.blit(boss.image, boss.rect)

    #Blit boss bullet in middle
    for boss_bullet_middle in boss_bullets_middle:
        screen.blit(boss_bullet_middle.image, boss_bullet_middle.rect)

    #Blit boss bullet in left
    for boss_bullet_left in boss_bullets_left:
        screen.blit(boss_bullet_left.image, boss_bullet_left.rect)
    
    #Blit boss bullet in right
    for boss_bullet_right in boss_bullets_right:
        screen.blit(boss_bullet_right.image, boss_bullet_right.rect)

    #Blit player bullet
    for player_bullet in player_bullets:
        screen.blit(player_bullet.image, player_bullet.rect)

    #Blit player
    player.updatePositionFB(keys_pressed, player_left_path, player_right_path, player_image_path, player_image_path) #updates pos of mc based on state of keys
    screen.blit(player.image, player.rect)

    #Blit Asteroid
    for asteroid in asteroids:
        screen.blit(asteroid.image, asteroid.rect)

    #Blit Texts
    health_text = font.render("Health: " + str(player_health) + "/10", True, (255, 255, 255))
    screen.blit(health_text, (50,screen_y-50))
    
    pygame.display.flip()


timer = 0
player_shoot_cd = 0
#GAME LOOP
running = True
while running:
    clock.tick(60) #60 FPS
    timer += 1
    player_shoot_cd += 1
    #KEYS PRESSED EVENT
    keys_pressed = pygame.key.get_pressed() # stores state of all keys

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else: 
            player.updatePositionFB(keys_pressed, player_left_path, player_right_path, player_image_path, player_image_path) #updates pos of mc based on state of keys
            

    if timer == 120:            
        #Boss Fires Bullets from middle
        bossbullet_image_path = 'bullet-boss.png'
        bb_spawnpoint_x = boss.rect.x + boss.rect.width/2
        bb_spawnpoint_y = 170
        boss_bullet_middle = FinalBossObjects.BossBullet(bb_spawnpoint_x, bb_spawnpoint_y, 10, 10, 5, 1, '', bossbullet_image_path, player.rect.x, player.rect.y)
        boss_bullets_middle.append(boss_bullet_middle)

        #Boss Fires Bullets from left
        bb_spawnpoint_x = boss.rect.x + boss.rect.width/2 - 112
        bb_spawnpoint_y = 145
        boss_bullet_left = FinalBossObjects.BossBullet(bb_spawnpoint_x, bb_spawnpoint_y, 10, 10, 3, 1, '', bossbullet_image_path, player.rect.x, player.rect.y)
        boss_bullets_left.append(boss_bullet_left)

        #Boss Fires Bullets from right
        bb_spawnpoint_x = boss.rect.x + boss.rect.width/2 + 112
        bb_spawnpoint_y = 145
        boss_bullet_right = FinalBossObjects.BossBullet(bb_spawnpoint_x, bb_spawnpoint_y, 10, 10, 3, 1, '', bossbullet_image_path, player.rect.x, player.rect.y)
        boss_bullets_right.append(boss_bullet_right)
        
        timer = 0

    if player_shoot_cd == 10:
        #Fire a bullet
        playerbullet_image_path = 'bullet-player.png'
        spawnpoint_x = player.rect.x + player.rect.width/2
        spawnpoint_y = player.rect.y
        player_bullet = FinalBossObjects.PlayerBullet(spawnpoint_x, spawnpoint_y, 10, 10, 10, 1, '', playerbullet_image_path)
        player_bullets.append(player_bullet) #Add bullet in bullets list
        player_shoot_cd = 0

    #Add asteroids
    if random.randint(1,60) == 30:
        x = random.randint(0, screen_x-40)
        i = random.randint(1,5)
        speed = random.randint(1,3)
        if i == 1:
            asteroid = FinalBossObjects.Asteroid(x, -50, 30, 30, speed, 1, '', a1_img)
        elif i == 2:
            asteroid = FinalBossObjects.Asteroid(x, -50, 30, 30, 2, speed, '', a2_img)
        elif i == 3:
            asteroid = FinalBossObjects.Asteroid(x, -50, 30, 30, 2, speed, '', a3_img)
        elif i == 4:
            asteroid = FinalBossObjects.Asteroid(x, -50, 30, 30, 2, speed, '', a4_img)
        elif i == 5:
            asteroid = FinalBossObjects.Asteroid(x, -50, 30, 30, 2, speed, '', a5_img)
        asteroids.append(asteroid)

    #Update the objects
    for player_bullet in player_bullets: #Player bullets
        player_bullet.update()
    for asteroid in asteroids: #Asteroids
        asteroid.update()
    for boss_bullet_middle in boss_bullets_middle: #Boss bullets in middle
        boss_bullet_middle.update()
    for boss_bullet_left in boss_bullets_left: #Boss bullets in left
        boss_bullet_left.update()
    for boss_bullet_right in boss_bullets_right: #Boss bullets in right
        boss_bullet_right.update()

    
    #COLLISIONS
    #Bullet and Asteroid collision
    for player_bullet in player_bullets:
        for asteroid in asteroids:
            if player_bullet.collide(asteroid.rect):
                asteroids.remove(asteroid)
                player_bullets.remove(player_bullet)
    #Bullet and boss collision
    for player_bullet in player_bullets:
        if player_bullet.collide(boss.rect):
            player_bullets.remove(player_bullet)
            boss_health -= 1
    #Asteroid and player collision
    for asteroid in asteroids:
        if asteroid.collide(player.rect):
            asteroids.remove(asteroid)
            player_health -= 1
    #Boss bullet and player collision
    for boss_bullet_left in boss_bullets_left:
        if boss_bullet_left.collide(player.rect):
            boss_bullets_left.remove(boss_bullet_left)
            player_health -= 1
    for boss_bullet_middle in boss_bullets_middle:
        if boss_bullet_middle.collide(player.rect):
            boss_bullets_middle.remove(boss_bullet_middle)
            player_health -= 1
    for boss_bullet_right in boss_bullets_right:
        if boss_bullet_right.collide(player.rect):
            boss_bullets_right.remove(boss_bullet_right)
            player_health -= 1

    #Player moves within screen
    if player.rect.x < 0:
        player.rect.x = 0
    if player.rect.x + player.rect.width > screen_x:
        player.rect.x = screen_x - player.rect.width 
    if player.rect.y + player.rect.height > screen_y:
        player.rect.y = screen_y-player.rect.height 
    if player.rect.y < boss.rect.height:
        player.rect.y = boss.rect.height 

    #Boss moves within screen
    boss.update()
    if boss.rect.x < 0:
        boss.x = 0
        boss.speed = boss.speed * (-1)
    if boss.rect.x + boss.rect.width > screen_x:
        boss.x = screen_x - boss.rect.width
        boss.speed = boss.speed * (-1)

    #If player reaches 0, close and print "Game over"
    if player_health == 0:
        running = False
        print('GAME OVER')
    
    #If boss reaches 0, close and print "You win"
    if boss_health == 0:
        running = False
        print('YOU WIN')


    render()
    pygame.display.update()
    
    

#Quit
pygame.quit()

