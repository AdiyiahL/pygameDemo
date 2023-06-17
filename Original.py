# Example file showing a circle moving on screen
import pygame as pg
import sys
from pygame.locals import *
import time
import random


# player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

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

class Player(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        x,y = 0,0
        self.image = pg.image.load("image/player1.png") # load player image
        self.surf = pg.Surface((80,153)) #define the surface of the player
        self.rect = self.surf.get_rect(left = 0,top =  Constant.SCREEN_HEIGHT/2-75) #get the surface of the player
        # 原始 pos :

    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            self.direction.y = -1
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pg.K_RIGHT]:
            self.direction.x = 1
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0


    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.top >=0:
            self.rect.move_ip(0,-5)
        if keys[pg.K_DOWN] and self.rect.bottom <=Constant.SCREEN_HEIGHT:
            self.rect.move_ip(0,5)
        if keys[pg.K_LEFT] and self.rect.left >=0:
            self.rect.move_ip(-5,0)
        if keys[pg.K_RIGHT] and self.rect.right <=Constant.SCREEN_WIDTH-5:
            self.rect.move_ip(5,0)

class Constant:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700
    #set color 定义颜色
    black = (0,0,0)

    running = True

    #图像刷新速率
    FPS = 60



class Game :
    def __init__(self):
        # pg setup
        pg.init()
        size = width,height = (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption("save your brain")
        self.clock = pg.time.Clock()
        self.background = pg.image.load("image/greengrass.jpg")
        # set font 设置字体
    def run(self):
        # BGM
        # pg.mixer.Sound("").play(-1)
        # define player and objects

        player = Player()
        #define object groups
        obs = pg.sprite.Group()
        #define #all sprite groups
        all_sprits = pg.sprite.Group()
        all_sprits.add(player)
        for i in range(3):
            leftob = int((i%2)*(Constant.SCREEN_WIDTH/2)+41)
            if(i<2):
                top =  100
            else:
                top = int((Constant.SCREEN_HEIGHT / 2) + 72)
            ob = Object(random.randint(leftob+150,leftob+Constant.SCREEN_WIDTH/2-182),random.randint(top+143,top+Constant.SCREEN_HEIGHT/2)-143)
            obs.add(ob)
            all_sprits.add(ob)

        while Constant.running:
            # fill the screen with a color to wipe away anything from last frame

            self.screen.blit(self.background, (0, 0))

            #draw all sprits
            for sprite in all_sprits:
                self.screen.blit(sprite.image,sprite.rect)
                sprite.move()

            #deal events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            #

            # flip() the display to put your work on screen
            pg.display.flip()
            pg.display.update()
            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            self.clock.tick(Constant.FPS)

        pg.quit()

if __name__ =='__main__':
    game = Game()
    game.run()