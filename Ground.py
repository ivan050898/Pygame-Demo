import utils

"""
contains the Ground class, used to display ground on the game
"""
#attributes
#@screen: area where the obstacle will be draw
#@speed: speed of the ground
#@imagen: path to the image
#@height: height of the screen

class Ground():
    def __init__(self,speed,screen,image,height):
        self.image,self.rect = utils.load_image(image,-1,-1,-1)
        self.image1,self.rect1 =  utils.load_image(image,-1,-1,-1)#uses the same image for the two rects
        self.rect.bottom = height
        self.rect1.bottom = height
        self.rect1.left = self.rect.right
        self.speed = speed
        self.screen=screen

    def draw(self):
        self.screen.blit(self.image,self.rect)
        self.screen.blit(self.image1,self.rect1)

    def update(self):
        self.rect.left += self.speed
        self.rect1.left += self.speed

        if self.rect.right < 0: #if the first image  reaches the left border
            self.rect.left = self.rect1.right #will be replace with second one

        if self.rect1.right < 0:#if the second image  reaches the left border

            self.rect1.left = self.rect.right #will be replace with first one

