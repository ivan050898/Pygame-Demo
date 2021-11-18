import utils
import pygame

"""
Contains the caracter class, used to display Mario or the Dino
"""
#attributes
#@screen: area where the obstacle will be draw
#@imagen: path to the image
#@height: height of the screen
#@width:  width of the screen
#@image1: Image for the movement
#@image2: image for when the caracter is ducking
#@sizex: how far from the left will be
#@sizey:  how far from the top will be


class Caracter():
    def __init__(self,height,width,screen,gravity,image1,image2,sizex=-1,sizey=-1):
        self.images,self.rect = utils.load_sprite_sheet(image1,5,1,sizex,sizey,-1)
        self.images1,self.rect1 = utils.load_sprite_sheet(image2,2,1,59,sizey,-1)
        self.rect.bottom = int(0.98*height)
        self.rect.left = width/15
        self.image = self.images[0]
        self.index = 0
        self.counter = 0
        self.score = 0
        self.isJumping = False
        self.isDead = False
        self.isDucking = False
        self.isBlinking = False
        self.movement = [0,0]
        self.jumpSpeed = 11.5
        self.screen=screen
        self.stand_pos_width = self.rect.width
        self.duck_pos_width = self.rect1.width
        self.height=height
        self.width=width
        self.gravity=gravity
        
    def draw(self):
        self.screen.blit(self.image,self.rect)
    #check if its jumping
    def checkbounds(self):
        if self.rect.bottom > int(0.98*self.height):
            self.rect.bottom = int(0.98*self.height)
            self.isJumping = False

    def update(self):
        if self.isJumping:
            self.movement[1] = self.movement[1] + self.gravity

        if self.isJumping:
            self.index = 0 #if its jumping uses the first image of the sprite
        elif self.isBlinking:
            if self.index == 0:
                if self.counter % 400 == 399:
                    self.index = (self.index + 1)%2

            else:
                if self.counter % 20 == 19:
                   self.index = (self.index + 1)%2

        elif self.isDucking: #if its ducking switches between the images
            if self.counter % 5 == 0:
                self.index = (self.index + 1)%2
        else:
            if self.counter % 5 == 0:
                self.index = (self.index + 1)%2 + 2

        if self.isDead:
           self.index = 4

        if not self.isDucking:
            self.image = self.images[self.index]
            self.rect.width = self.stand_pos_width
        else:
            self.image = self.images1[(self.index)%2]
            self.rect.width = self.duck_pos_width

        self.rect = self.rect.move(self.movement)
        self.checkbounds()
        self.counter = (self.counter + 1)

    def CheckCounter(self):
        if not self.isDead and self.counter % 7 == 6 and self.isBlinking == False:
                self.score += 1
                if self.score % 100 == 0 and self.score != 0:
                    return True
        return False
