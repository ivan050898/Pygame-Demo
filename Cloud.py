import utils
import pygame


"""
this file contains the Cloud class
"""
#attributes

#x: how many pixel from the left will be between the image and the left border of the screen
#y how many pixel from the top will be between the image and the top border of the screen
#@imagen: path to the image

class Cloud(pygame.sprite.Sprite):#inheritance from Sprite
    def __init__(self,x,y,screen,imagen):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image,self.rect = utils.load_image(imagen,int(90*30/42),30,-1)
        self.speed = 1
        self.rect.left = x
        self.rect.top = y
        self.movement = [-1*self.speed,0]
        self.screen=screen

    def draw(self):
        screen.blit(self.image,self.rect)

    def update(self):#updates its position and image
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:#if it already pass the left border of the screen
            self.kill()
    
