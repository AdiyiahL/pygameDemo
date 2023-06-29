import pygame as pg
from settings import *
from support import *
import pyautogui
#################################################################Player
class Player(pg.sprite.Sprite):

    def __init__(self, pos, group, collision_sprites):
        super().__init__(group)
        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0

        # general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.z = LAYERS['main']

        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 130

        # collision
        self.hitbox = self.rect.copy().inflate((-12, -50))
        self.collision_sprites = collision_sprites

        self.key = 0
        self.sleep = False

        self.success = pygame.mixer.Sound('audio/success.wav')
        self.success.set_volume(1)

    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                           }
        # 'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
        # 'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
        # 'right_water': [], 'left_water': [], 'up_water': [], 'down_water': []
        for animation in self.animations.keys():
            full_path = 'graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):  # 到达最后一张图片后，index归零，回到第一张图片
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]  # 获取到某个状态下的某张图片，状态图片统一

    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pg.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

    def get_status(self):
        # idle
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'

        # # tool use
        # if self.timers['tool use'].active:
        #     self.status = self.status.split('_')[0] + '_' + self.selected_tool
    def update_monster(self):
        self.key +=1
        if self.key >=3:
            for sprite in self.collision_sprites.sprites():
                if hasattr(sprite, "monster"):
                    sprite.monster = 0
                    print(sprite.monster)

    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if hasattr(sprite,'question'):
                        # pyautogui.alert("Do you want to answer questions?")
                        print(sprite.question)
                        answer = pyautogui.confirm(text=sprite.questions,title="NPC-Questions",buttons=['yes','no','give up'])
                        if answer==sprite.answer:
                            self.update_monster()
                        print(self.key)
                    if hasattr(sprite,"monster") and sprite.monster==1:
                        pyautogui.alert("You don't have enough keys!")
                    if hasattr(sprite,"monster") and sprite.monster==0:
                        self.success.play()  # 音效
                        pyautogui.alert("Success!")
                        sprite.image = pygame.image.load('graphics/character/target_monster/1.png').convert_alpha()
                    if direction == 'horizontal':
                        if self.direction.x > 0: # moving right
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0: # moving left
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx

                    if direction == 'vertical':
                        if self.direction.y > 0: # moving down
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0: # moving up
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery

    def move(self,dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')

    def update(self, dt):
        self.input()
        self.move(dt)
        self.get_status()
        self.animate(dt)
################################################Player