import ObstacleTwo
import ObstacleOne
import Caracter
import Cloud
import pygame
import os
import Ground
import Scoreboard
import Button as bt
import utils
from pathlib import Path
import random
import time


#Menu window variables 
ScreenSize = (width,height) = (600,300)
screen = pygame.display.set_mode(ScreenSize) #setting the screen area





#Game variables and stuff starts here
pygame.mixer.pre_init(44100, -16, 2, 2048) #Load the sound mixer
pygame.init()
FPS = 65         #using 65 frames per second prevents it from  being to laggy
Gravity = 0.5    #defines how far  the dino will jump
black = (0,0,0)
white = (255,255,255)
sky = (177, 218, 234)
clock = pygame.time.Clock() #setting the clock

background_color= (235,235,235)
global high_score,ChosenIndex
high_score=0
ScriptsPath=Path(os.path.dirname(os.path.abspath(__file__))) #gets the current script path
ParentPath=ScriptsPath.parent #current parent path of Main
AudiosPath=os.path.join(ParentPath,"Audios") #Audios path
ImagesPath=os.path.join(ParentPath,"Images") #Images path
Groud1pat=os.path.join(ImagesPath,"ground1.png")
startImage=os.path.join(ImagesPath,"startbutton.png")
startImage1=os.path.join(ImagesPath,"start.png")
counter=0
jump_sound = pygame.mixer.Sound(os.path.join(AudiosPath,"jump.wav"))
checkPoint_sound = pygame.mixer.Sound(os.path.join(AudiosPath,"checkPoint.wav"))
die_sound=pygame.mixer.Sound(os.path.join(AudiosPath,"die.wav"))
Mariojump_sound = pygame.mixer.Sound(os.path.join(AudiosPath,"MarioJump.wav"))
MariocheckPoint_sound = pygame.mixer.Sound(os.path.join(AudiosPath,"MarioCheckpoint.wav"))
Mariodie_sound=pygame.mixer.Sound(os.path.join(AudiosPath,"MarioDie.wav"))
ImageArray=[["Run1.png","Ducking1.png","ground1.png","Cloud1.png","Wall1.png","Bird1.png"],["Run2.png","Ducking2.png","Ground2.png","Cloud2.png","Wall2.png","Bird2.png"]]
sounds=[[jump_sound,checkPoint_sound,die_sound],[Mariojump_sound,MariocheckPoint_sound,Mariodie_sound]]
ChosenIndex=1

#read the highest score from a txt file
def ReadFile():
    global high_score
    try:
        file = open("config.txt", "r")
        high_score= int(file.readline())
        file.close()
    except:
        high_score=0

#reads the highest score from a txt file

def WriteFile(number):
    file = open("config.txt", "w")
    file.write(str(number))
    file.close()

#intro screen and functionality
def intro():
    ScreenSize = (width,height) = (600,300)
    screen = pygame.display.set_mode(ScreenSize) #setting the screen area
    global high_score,ChosenIndex
    ReadFile()
    gamespeed = 3

    #Creating Ground objects and setting the y position
    GameGroundMario= Ground.Ground(-1*gamespeed,screen,os.path.join(ImagesPath,ImageArray[1][2]),height)
    GameGroundMario.rect.bottom=300
    GameGroundMario.rect1.bottom=300
    GameGroundDino= Ground.Ground(-1*gamespeed,screen,os.path.join(ImagesPath,ImageArray[0][2]),height)
    GameGroundDino.rect.bottom=150
    GameGroundDino.rect1.bottom=150

    #Creating Ground objects and setting the y position
    Mario = Caracter.Caracter(height,width,screen,Gravity,os.path.join(ImagesPath,ImageArray[1][0]),os.path.join(ImagesPath,ImageArray[ChosenIndex][1]),44,47)
    Dino = Caracter.Caracter(height,width,screen,Gravity,os.path.join(ImagesPath,ImageArray[0][0]),os.path.join(ImagesPath,ImageArray[ChosenIndex][1]),44,47)
    Dino.rect1.bottom=150
    Dino.rect.bottom=150
    #creating the buttons
    BtnStartMario=bt.button(230,225,screen,startImage)
    BtnStartDino=bt.button(230,85,screen,startImage)

    GameInit=False
    pygame.display.set_caption("Run")
    
    while not GameInit:
      GameGroundMario.update()
      GameGroundDino.update()
      Mario.update()
      Dino.update()
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            exit(1)
         if event.type == pygame.MOUSEBUTTONDOWN:
             if pygame.mouse.get_pressed()[0]: #if the left click is being pressed
                 if event.pos[0]>=237 and event.pos[0]<=367 and event.pos[1]>=13  and event.pos[1]<=81: #if this area is clicked
                     ChosenIndex=0#enables the Dino skin theme
                     GameInit=True
                 elif event.pos[0]>=237 and event.pos[0]<=367 and event.pos[1]>=154  and event.pos[1]<=218: #if this area is clicked
                     ChosenIndex=1#enables the Mario skin theme
                     GameInit=True

            
      if pygame.display.get_surface() != None:
          screen.fill(black)
          BtnStartMario.draw()
          BtnStartDino.draw()
          GameGroundMario.draw()
          GameGroundDino.draw()
          Mario.draw()
          Dino.draw()
          pygame.display.update()
      clock.tick(FPS)
      pygame.display.flip()
      if GameInit:
          break
    gameplay()

def gameplay():
    global high_score
    ScreenSize = (width,height) = (600,150)

    screen = pygame.display.set_mode(ScreenSize) #setting the screen area
    pygame.display.set_caption("Run")
    pygame.fastevent.init()

    gamespeed = 3
    GameGround= Ground.Ground(-1*gamespeed,screen,os.path.join(ImagesPath,ImageArray[ChosenIndex][2]),height)

    startMenu = False
    gameOver = False
    gameQuit = False
    counter = 0
    scb = Scoreboard.Scoreboard(os.path.join(ImagesPath,"numbers.png"),height,width,screen)#scoreboard object
    
    highsc = Scoreboard.Scoreboard(os.path.join(ImagesPath,"numbers.png"),height,width,screen,width*0.78)#scoreboard object

    #image containers
    clouds = pygame.sprite.Group()
    Ones = pygame.sprite.Group()
    Twos = pygame.sprite.Group()
    last_obstacle = pygame.sprite.Group()

    Cloud.Cloud.containers = clouds #enables the container for the cloud
    ObstacleOne.ObstacleOne.containers=Ones
    ObstacleTwo.ObstacleTwo.containers=Twos

    #Creates the caracter object
    Player = Caracter.Caracter(height,width,screen,Gravity,os.path.join(ImagesPath,ImageArray[ChosenIndex][0]),os.path.join(ImagesPath,ImageArray[ChosenIndex][1]),44,47)
    
    temp_images,temp_rect = utils.load_sprite_sheet(os.path.join(ImagesPath,"numbers.png"),12,1,11,int(11*6/5),-1)

    #makes the surface for the scoreboards and draws it
    HI_image = pygame.Surface((22,int(11*6/5)))
    HI_rect = HI_image.get_rect()
    HI_image.fill(background_color)
    HI_image.blit(temp_images[10],temp_rect)
    temp_rect.left += temp_rect.width
    HI_image.blit(temp_images[11],temp_rect)
    HI_rect.top = height*0.1
    HI_rect.left = width*0.73
    #images and rects for the game over and replay images
    retbutton_image,retbutton_rect = utils.load_image(os.path.join(ImagesPath,'replay_button.png'),35,31,-1)
    gameover_image,gameover_rect =  utils.load_image(os.path.join(ImagesPath,'game_over.png'),190,11,-1)

    while not gameQuit:
        while not gameOver:
            for event in pygame.fastevent.get():
                if event.type == pygame.QUIT:
                   gameQuit = True
                   gameOver = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                            if Player.rect.bottom == int(0.98*height):
                                Player.isJumping = True
                                if pygame.mixer.get_init() != None:
                                    sounds[ChosenIndex][0].play()
                                Player.movement[1] = -1*Player.jumpSpeed

                if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_DOWN:
                       if not (Player.isJumping and Player.isDead):
                           Player.isDucking = True

                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            Player.isDucking = False

            for O in Ones:#for each one of the cactus or tubes
                O.movement[0] = -1*gamespeed
                if pygame.sprite.collide_mask(Player,O): #checks if it collide with the Player
                    Player.isDead = True
                    if pygame.mixer.get_init() != None:
                        sounds[ChosenIndex][2].play()
                        gameQuit=False
                        gameOver=True
                        CheckScore(Player.score)

            for T in Twos: #for each one of the birds or flying fishes
                T.movement[0] = -1*gamespeed
                if pygame.sprite.collide_mask(Player,T): #checks if it collide with the Player
                    Player.isDead = True  
                    if pygame.mixer.get_init() != None:
                        sounds[ChosenIndex][2].play() #plays the audio when the player dies
                        gameQuit=True
                        gameOver=True
                        if(CheckScore(Player.score)):
                           highsc.update(Player.score)

            if len(Ones) < 2: # it can only be 2 obstacle of type 1 at same time 
                if len(Ones) == 0:
                    last_obstacle.empty()
                    obstacle=ObstacleOne.ObstacleOne(height,width,screen,os.path.join(ImagesPath,ImageArray[ChosenIndex][4]),gamespeed,40,40)
                    last_obstacle.add(obstacle)
                else:
                    for l in last_obstacle:
                        if l.rect.right < width*0.7 and random.randrange(0,50) == 10:
                            last_obstacle.empty()
                            obstacle=ObstacleOne.ObstacleOne(height,width,screen,os.path.join(ImagesPath,ImageArray[ChosenIndex][4]),gamespeed,40,40)
                            last_obstacle.add(obstacle)
            if len(Twos) == 0 and random.randrange(0,100) == 10 and counter > 500: # obstacles of the type 2 appears when 100 points are reached 
                for l in last_obstacle:
                    if l.rect.right < width*0.8:
                        last_obstacle.empty()
                        obstacle=ObstacleTwo.ObstacleTwo(height,width,screen,os.path.join(ImagesPath,ImageArray[ChosenIndex][5]),gamespeed,42,38)
                        last_obstacle.add(obstacle)

            pygame.event.get()
            clouds.update()
            GameGround.update()
            scb.update(Player.score)
            Player.update()
            screen.blit(HI_image,HI_rect)
            Ones.update()
            Twos.update()
            
            if(CheckScore(Player.score)):#checks the score , if its the new highest score it updates it
                highsc.update(high_score)
            highsc.update(high_score)
            if(Player.CheckCounter()):
               sounds[ChosenIndex][1].play()
            if len(clouds) < 5 and random.randrange(1,300)==1:# maximun 4 clouds , the random is just for random spawning  time
                Cloud.Cloud(width,random.randrange(height/5,height/2),screen,os.path.join(ImagesPath,ImageArray[ChosenIndex][3]))
            if pygame.display.get_surface() != None:#draws all the screen elements here
                screen.fill(black)
                GameGround.draw()
                clouds.draw(screen)
                scb.draw()
                highsc.draw()
                screen.blit(HI_image,HI_rect)

                Player.draw()
                Ones.draw(screen)
                Twos.draw(screen)
                pygame.display.update()
            clock.tick(FPS)
            pygame.display.flip()
            if counter%700 == 699: # Every 6999999 cicles  the speed increase
                GameGround.speed -= 1
                gamespeed += 0.5

            counter = (counter + 1)

        if gameQuit:
            pygame.quit()
            exit(1)
        if gameOver:
            break
        
            
    while gameOver:#if the game is over
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                gameQuit = True
                gameOver = False
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         pygame.quit()
                         exit(1)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            gameQuit = True
                            gameOver = False
                            intro() #goes back to the intro
                        
            highsc.update(high_score)
            if pygame.display.get_surface() != None:
                disp_gameOver_msg(retbutton_image,gameover_image)
                if high_score != 0:
                    highsc.draw()
                    screen.blit(HI_image,HI_rect)
                pygame.display.update()
            clock.tick(FPS)
            pygame.display.flip()
    
#displays the game over image
def disp_gameOver_msg(retbutton_image,gameover_image):
    retbutton_rect = retbutton_image.get_rect()
    retbutton_rect.centerx = width / 2
    retbutton_rect.top = height*0.52
    gameover_rect = gameover_image.get_rect()
    gameover_rect.centerx = width / 2
    gameover_rect.centery = height*0.35
    screen.blit(retbutton_image, retbutton_rect)
    screen.blit(gameover_image, gameover_rect)

#check for the new highest score
def CheckScore(NewScore):
    global high_score
    if NewScore>=high_score:
        high_score=NewScore
        WriteFile(high_score)
intro()
