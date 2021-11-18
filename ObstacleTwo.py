import utils
import pygame

"""
this file contains the ObstacleTwo class, used to project either or a terodactyle or a flyng fish, depends on the game mode (dino or mario)
"""

#attributes
#@screen: area where the obstacle will be draw
#@speed: speed of the obstacle
#@imagen: path to the image
#@height: height of the screen
#@width:  width of the screen




class ObstacleTwo(pygame.sprite.Sprite):#inheritance from Sprite
    def __init__(self,height,width,screen,imagen,speed=5,sizex=-1,sizey=-1):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.images,self.rect = utils.load_sprite_sheet(imagen,2,1,sizex,sizey,-1)
        self.ptera_height = height*0.60
        self.rect.centery =  self.ptera_height
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1*speed,0]
        self.index = 0
        self.counter = 0
        self.screen=screen

    def draw(self):
        self.screen.blit(self.image,self.rect)

    def update(self):#updates its position and image
        if self.counter % 10 == 0:
            self.index = (self.index+1)%2
        self.image = self.images[self.index]
        self.rect = self.rect.move(self.movement)
        self.counter = (self.counter + 1) 
        if self.rect.right < 0: #if it already pass the left border of the screen
            self.kill()
