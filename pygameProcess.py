# Example file showing a circle moving on screen
import pygame as pg
import sys
from constant import Constant
from level import Level



class Game :
    def __init__(self):
        # pg setup
        pg.init()
        size = width,height = (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption("rescue little monster")
        self.clock = pg.time.Clock()
        # self.background = pg.image.load("image/greengrass.jpg")
        # set font 设置字体
        self.level = Level()


    def run(self):
        while Constant.running:

            #deal events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            # fill the screen with a color to wipe away anything from last frame
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pg.display.update()

        pg.quit()

if __name__ =='__main__':
    game = Game()
    game.run()