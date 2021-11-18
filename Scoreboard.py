import utils
import pygame

"""
This file contains the scoreboard classs, used to show the score on real time and to show the highest
"""
#@imagen: path to the image
#@height: height of the screen
#@width:  width of the screen



class Scoreboard():
    def __init__(self,imagen,height,width,screen,x=-1,y=-1):
        self.score = 0
        self.tempimages,self.temprect = utils.load_sprite_sheet(imagen,12,1,11,int(11*6/5),-1)
        self.image = pygame.Surface((55,int(11*6/5)))
        self.rect = self.image.get_rect()
        self.screen=screen
        if x == -1:
            self.rect.left = width*0.89
        else:
            self.rect.left = x
        if y == -1:
            self.rect.top = height*0.1
        else:
            self.rect.top = y


    def draw(self):
         self.screen.blit(self.image,self.rect)

    #updates the scoreboard using and image for every digit
    def update(self,score):
        score_digits = self.extractDigits(score)
        self.image.fill((235,235,235))
        for s in score_digits:
            self.image.blit(self.tempimages[s],self.temprect)
            self.temprect.left += self.temprect.width
        self.temprect.left = 0

    #extract the digits of a number 
    def extractDigits(self,number):
      if number > -1:
        digits = []
        while(number/10 != 0):
            digits.append(number%10)
            number = int(number/10)
        digits.append(number%10)
        for i in range(len(digits),5):
            digits.append(0)
        digits.reverse()
        return digits
