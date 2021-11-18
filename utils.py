import os
import pygame
from pygame.constants import RLEACCEL

"""
this file contains 2 methods for image manipulation with pygame

"""


#@fullname : path of the image
#@sizex: scale of width
#@sizey: scale of height
#@colorkey: colorkey to be set

def load_image(fullname,sizex=-1, sizey=-1,colorkey=None):
    image = pygame.image.load(fullname)
    image = image.convert() #creates a copy  in memory that shows quicker on screen
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    if sizex != -1 or sizey != -1:
        image = pygame.transform.scale(image, (sizex, sizey))

    return (image, image.get_rect())

#@fullname : path of the image
#@scalex: scale of width
#@scaley: scale of height
#@colorkey: colorkey to be set
#@nx: number of horizontal cuts to be made
#@ny: number vertical cuts to be made

def load_sprite_sheet(fullname,nx,ny,scalex = -1,scaley = -1,colorkey = None):
    sheet = pygame.image.load(fullname)
    sheet = sheet.convert() #creates a copy in memory that shows quicker on screen
    sheet_rect = sheet.get_rect()

    sprites = []

    sizex = sheet_rect.width/nx
    sizey = sheet_rect.height/ny

    for i in range(0,ny):
        for j in range(0,nx):
            rect = pygame.Rect((j*sizex,i*sizey,sizex,sizey))
            image = pygame.Surface(rect.size)
            image = image.convert()
            image.blit(sheet,(0,0),rect)

            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey,RLEACCEL)

            if scalex != -1 or scaley != -1:
                image = pygame.transform.scale(image,(scalex,scaley))

            sprites.append(image)

    sprite_rect = sprites[0].get_rect()

    return sprites,sprite_rect
