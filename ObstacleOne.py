import utils
import pygame
import random



"""
this file contains the ObstacleOne class, used to project either or a cactus or a tube, depends on the game mode (dino or mario)
"""

#attributes
#@screen: area where the obstacle will be draw
#@speed: speed of the obstacle
#@imagen: path to the image
#@height: height of the screen
#@width:  width of the screen



class ObstacleOne(pygame.sprite.Sprite):
    def __init__(self,height,width,screen,imagen,speed=5,sizex=-1,sizey=-1):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.images,self.rect = utils.load_sprite_sheet(imagen,3,1,sizex,sizey,-1)
        self.rect.bottom = int(0.98*height)
        self.rect.left = width + self.rect.width
        self.image = self.images[random.randrange(0,3)]
        self.movement = [-1*speed,0]
        self.screen=screen
    def draw(self):
        self.screen.blit(self.image,self.rect)

    def update(self):#updates its position and image
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0: #if it already pass the left border of the screen
            self.kill()
