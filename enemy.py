import pygame as pg
from settings import *
from support import *
############################################Objects
class Object(pg.sprite.Sprite):
    def __init__(self,xinit,yinit):
        super(Object,self).__init__()
        x,y = xinit,yinit
        # (random.randint(10, 900), random.randint(10, 690))
        self.image = pg.image.load("image/object1.png")
        self.surf = pg.Surface((82,143)) #定义边缘位置
        self.rect = self.surf.get_rect(center = (x, y)) #在窗口中的位置
        self.state = 0

    def move(self):
        pass

