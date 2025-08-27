import pygame

from Characters import Characters
from MainCharacter import MainCharacter as MC
from Button import *
from Start import *
from LevelBosses import LevelBosses as LB
from Battle import Battle as B
from ChoosePlayer import *
from FriendlyAlien import FriendlyAlien as FA
from Intro import *
import random
from MiniBoss import MiniBoss as MB
from FinalBoss import *
from VictoryScreen import *
from LoseScreen import *
from EngineCutscene import *


pygame.init()
pygame.display.set_caption("Hello World")

#Initializations
screen = pygame.display.set_mode((1280, 720))
screen_rect = screen.get_rect()

#Create instance of FriendlyAlien class
friendly_alien = FA(460, 460, 60, 60, 0, "friendlyAlien.png", "First level.png")

#battle scene background

bgImg = pygame.image.load('ForestBattleScene.png')
bgImgScaled = pygame.transform.scale(bgImg, (1280,720))
bgImg_rect = bgImgScaled.get_rect()

# lavabgImg = pygame.image.load('LavaBattleScene.png')
# lavabgImgScaled = pygame.transform.scale(lavabgImg, (1280,720))
# lavabgImg_rect = lavabgImgScaled.get_rect()

# oceanbgImg = pygame.image.load('OceanBattleScene.png')
# oceanbgImgScaled = pygame.transform.scale(oceanbgImg, (1280,720))
# oceanbgImg_rect = oceanbgImgScaled.get_rect()


width = screen.get_width()
height = screen.get_height()

#button colours
color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)

#mini bosses
fire_elemental = LB(screen_rect.centerx, screen_rect.centery, 50, 50, 15, 'fire', 'fireElemental.png')
water_elemental = LB(screen_rect.centerx, screen_rect.centery, 50, 50, 15, 'water', 'waterElemental.png')
earth_elemental = LB(screen_rect.centerx, screen_rect.centery, 50, 50, 15, 'earth', 'earthElemental.png')

#Start Screen
Start.menuLoop(called = True)

#Intro to Game
intro = Intro('space-background.png')
intro.intro_loop()

#Choosing Player
player = ChoosePlayer()
player.choose_loop()

mc = MC(-50, 60, 133, 100, 1, 20, '', player.imageFile)
elementList = ['earth', 'fire', 'water']
random.shuffle(elementList)

attack_power = 0
elemental_attack_power = 0

if player.imageFile == 'CharYellowFrontView.png':
    imageLeft = 'CharYellowWalkingLeft.png'
    imageRight = 'CharYellowWalkingRight.png'
    imageUp = 'CharYellowBackView.png'
    imageDown = 'CharYellowFrontView.png'
    mc.health += 2
    print("User has chosen yellow character")
    print("The total HP of the character has increased by 2")
    
elif player.imageFile == 'CharOrngFrontView.png':
    imageLeft = 'CharOrngWalkingLeft.png'
    imageRight = 'CharOrngWalkingRight.png'
    imageUp = 'CharOrngBackView.png'
    imageDown = 'CharOrngFrontView.png'
    attack_power += 2
    print("User has chosen Orange character")
    print("The total attack power of the character has increased by 2")

elif player.imageFile == 'CharGreenFrontView.png':
    imageLeft = 'CharGreenWalkingLeft.png'
    imageRight = 'CharGreenWalkingRight.png'
    imageUp = 'CharGreenBackView.png'
    imageDown = 'CharGreenFrontView.png'
    elemental_attack_power += 2
    print("User has chosen Green character")
    print("The total elemental attack power of the character has increased by 2")

total_health = mc.health

#battle scenes
battle1 = B(total_health, attack_power, elemental_attack_power, mc, earth_elemental,screen, color_light, color_dark, 485, 580, 150, 50, 'Attack', 'Heal', 'Elemental', color, 'FORCED SQUARE.ttf', 35)
battle2 = B(total_health, attack_power, elemental_attack_power, mc, fire_elemental, screen,color_light, color_dark, 485, 580, 150, 50, 'Attack', 'Heal', 'Elemental', color, 'FORCED SQUARE.ttf', 35)
battle3 = B(total_health, attack_power, elemental_attack_power, mc, water_elemental,screen, color_light, color_dark, 485, 580, 150, 50, 'Attack', 'Heal', 'Elemental', color, 'FORCED SQUARE.ttf', 35)

#Final boss scene
fB = FinalBoss()
mouse = pygame.mouse.get_pos()
startBattle = pygame.mixer.Sound('startBattle.wav')

#restart loop when mc loses
def restart_battle(battle):
    battle.battleLoss_render(screen, mouse, bgImgScaled, bgImg_rect)
    battle.battleLoss_gameloop(mouse, bgImgScaled, bgImg_rect)
    mc.health = total_health
    print(mc.health)
    print(mc.element)
    battle.textprompt = battle.fontprompt.render('What will you do?', True, (255,255,255))
    battle.battle_render(screen, mouse, bgImgScaled, bgImg_rect)
    battle.battle_gameloop(mouse, bgImgScaled, bgImg_rect)
    if battle.levelBoss.health <= 0:
        battle.battleWin_render(screen, mouse, bgImgScaled, bgImg_rect)
        battle.battleWin_gameloop(mouse, bgImgScaled, bgImg_rect)
        print("User has won the battle")
    elif battle.mc.health <= 0:
        print("User has lost the battle and restarted")
        restart_battle(battle)
        

#restart final boss when player ship loses
def restart_boss():
    if fB.boss.health == 0:
        vScreen = VictoryScreen()
        vScreen.vScreenLoop()
    elif fB.player.health == 0:
        lScreen = LoseScreen()
        lScreen.lScreenLoop()
    fB.gameLoop()
    restart_boss()

#gives first element
mc.element = elementList[0]
del elementList[0]

#level 1
mc.rect.x = -50
mc.rect.y = 250
friendly_alien.path_loop(imageLeft, imageRight, imageUp, imageDown, mc)


mc.rect.x = -50
mc.rect.y = 250
grassMiniBoss = MB(1100,300,200,200,10,"earthElemental.png", "First level.png")
grassMiniBoss.path_loop(imageLeft, imageRight, imageUp, imageDown, mc)


#mini boss battle 1
startBattle.set_volume(0.1)
startBattle.play()
mc.health = total_health
print(mc.health)
print(mc.element)
mc.image = pygame.image.load(player.imageFile)
battle1.battle_render(screen, mouse, bgImg, bgImg_rect)
battle1.battle_gameloop(mouse, bgImgScaled, bgImg_rect)
if battle1.levelBoss.health <= 0:
    battle1.battleWin_render(screen, mouse, bgImgScaled, bgImg_rect)
    battle1.battleWin_gameloop(mouse, bgImgScaled, bgImg_rect)
    print("User has won the battle")
elif battle1.mc.health <= 0:
    print("User has lost the battle and restarted")
    restart_battle(battle1)



#gives second element
mc.element = elementList[0]
del elementList[0]

#level 2
mc.rect.x = -50
mc.rect.y = 250
mc.speed = 5
friendly_alien = FA(460, 460, 60, 60, 0, "friendlyAlien.png", "Second Level.png")
friendly_alien.path_loop(imageLeft, imageRight, imageUp, imageDown, mc)

mc.rect.x = -50
mc.rect.y = 250
miniBoss = MB(1100,300,200,200,10, "fireElemental.png", "Second Level.png")
miniBoss.path_loop(imageLeft, imageRight, imageUp, imageDown, mc)

bgImg = pygame.image.load("LavaBattleScene.png")
bgImgScaled = pygame.transform.scale(bgImg, (1280,720))
bgImg_rect = bgImgScaled.get_rect()

#mini boss battle 2
startBattle.set_volume(0.1)
startBattle.play()
mc.health = total_health
mc.image = pygame.image.load(player.imageFile)
print(mc.health)
print(mc.element)
battle2.battle_render(screen, mouse, bgImgScaled, bgImg_rect)
battle2.battle_gameloop(mouse, bgImgScaled, bgImg_rect)
if battle2.levelBoss.health <= 0:
    battle2.battleWin_render(screen, mouse, bgImgScaled, bgImg_rect)
    battle2.battleWin_gameloop(mouse, bgImgScaled, bgImg_rect)
    print("User has won the battle")
elif battle2.mc.health <= 0:
    print("User has lost the battle and restarted")
    restart_battle(battle2)

#gives third element
mc.element = elementList[0]
del elementList[0]

#level 3
mc.rect.x = -50
mc.rect.y = 250
friendly_alien = FA(460, 460, 60, 60, 0, "friendlyAlien.png", "Third Level.png")
friendly_alien.path_loop(imageLeft, imageRight, imageUp, imageDown, mc)

mc.rect.x = -50
mc.rect.y = 250
miniBoss = MB(1100,300,200,200,10, "waterElemental.png", "Third Level.png")
miniBoss.path_loop(imageLeft, imageRight, imageUp, imageDown, mc)

bgImg = pygame.image.load("OceanBattleScene.png")
bgImgScaled = pygame.transform.scale(bgImg, (1280,720))
bgImg_rect = bgImgScaled.get_rect()

#mini boss battle 3
startBattle.set_volume(0.1)
startBattle.play()
mc.health = total_health
print(mc.health)
print(mc.element)
mc.image = pygame.image.load(player.imageFile)
battle3.battle_render(screen, mouse, bgImgScaled, bgImg_rect)
battle3.battle_gameloop(mouse, bgImgScaled, bgImg_rect)
if battle3.levelBoss.health <= 0:
    battle3.battleWin_render(screen, mouse, bgImgScaled, bgImg_rect)
    battle3.battleWin_gameloop(mouse, bgImgScaled, bgImg_rect)
    print("User has won the battle")
elif battle3.mc.health <= 0:
    print("User has lost the battle and restarted")
    restart_battle(battle3)

#engine cutscene
cutscene = EngineCutscene('space-background.png')
cutscene.cutscene_loop()

#final boss battle
FinalBoss.gameLoop(called = True)


pygame.quit()