import pygame
import utils

"""
This class  contains the button class

Class attribute  :

   @x: integer to signal how many pixels of space will be between the left border of the screen
   and the image
   
   @y: integer to signal how many pixels of space will be between the upper border of the screen
   and the image

   
   @screen :Object that pygame.display.set_mode(ScreenSize) this is the screen area
   
   @image: path of the image


"""
class button():
    def __init__(self, x,y,screen,image):
        self.x = x
        self.y = y
        self.screen=screen
        self.image,self.rect = utils.load_image(image,-1,-1,-1)#check the utils file for the info of thi function

    #draws the image and the rectangle on the screen
    def draw(self):
        self.rect.bottom=self.y
        self.rect.left=self.x 
        self.screen.blit(self.image,self.rect)
    
