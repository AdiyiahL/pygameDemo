import pygame
from settings import *
from player import Player
from constant import Constant
from sprites import *

class Level:
	def __init__(self):

		# get the display surface
		self.display_surface = pygame.display.get_surface()
		# sprite groups
		# self.all_sprites = pygame.sprite.Group()
		self.all_sprites = CameraGroup()
		#collision
		self.collision_sprites = pygame.sprite.Group()
		self.setup()
		#music
		# self.success = pygame.mixer.Sound('../audio/success.wav')
		# self.success.set_volume(0.3)
		self.music = pygame.mixer.Sound('audio/music.mp3')
		self.music.set_volume(0.3)
		self.music.play(loops=-1)

	def setup(self):

		self.player = Player((0,100), self.all_sprites, self.collision_sprites)
		#实例化Generic对象，引入背景图片Constant.SCREEN_HEIGHT/2-75
		self.background = Generic(
			pos=(-Constant.SCREEN_WIDTH/2, Constant.SCREEN_HEIGHT/2+120),
			surf=pygame.image.load('image/forestl2.png').convert_alpha(),
			groups=self.all_sprites,
			z=LAYERS['ground'])
		self.ob1 = Objects(
			pos=(Constant.SCREEN_WIDTH/2-400, -40),
			surf=pygame.image.load('image/object1.png').convert_alpha(),
			groups=[self.all_sprites, self.collision_sprites],
			player_add=self.player_add,  # 声明player_add属性
			questions="Is Tokenization one key feature of Spacy?",
			answer="yes",
			z=LAYERS['objects'])
		self.ob2 = Objects(
			pos=(Constant.SCREEN_WIDTH/2+180, -30),
			surf=pygame.image.load('image/object1.png').convert_alpha(),
			groups=[self.all_sprites, self.collision_sprites],
			player_add=self.player_add,  # 声明player_add属性
			questions="Does Part-of-speech tagging belong toSpacy?",
			answer="no",
			z=LAYERS['objects'])
		self.ob3 = Objects(
			pos=(Constant.SCREEN_WIDTH/2*3, 20),
			surf=pygame.image.load('image/object1.png').convert_alpha(),
			groups=[self.all_sprites, self.collision_sprites],
			player_add=self.player_add,    # 声明player_add属性
			questions="Is Named entity recognition related toSpacy?",
			answer="yes",
			z=LAYERS['objects'])
		self.stone = stones(
			pos=(Constant.SCREEN_WIDTH/2+280, 160),
			surf=pygame.image.load('image/stone.png').convert_alpha(),
			groups=[self.all_sprites, self.collision_sprites],
			z=LAYERS['stone'])
		self.target_monster = target_monster(
			pos=(Constant.SCREEN_WIDTH-50,20),
			surf=pygame.image.load('graphics/character/target_monster/0.png').convert_alpha(),
			groups=[self.all_sprites, self.collision_sprites],
			z=LAYERS['main'])

	def player_add(self): # 链接玩家的库存和其他精灵比如树、苹果，玩家打一个苹果库存就增加一个苹果

		self.player.key += 1
		# self.success.play()

	def run(self,dt):
		# self.all_sprites.draw(self.display_surface)
		max_x = -Constant.SCREEN_WIDTH/2
		max_y = Constant.SCREEN_HEIGHT/2+110
		self.all_sprites.custom_draw(self.player)

		self.all_sprites.update(dt)

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2()

	def custom_draw(self, player):
		self.offset.x = player.rect.centerx - Constant.SCREEN_WIDTH / 2
		self.offset.y = player.rect.centery - Constant.SCREEN_HEIGHT / 2

		for layer in LAYERS.values():
			for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
				if sprite.z == layer:
					offset_rect = sprite.rect.copy()
					offset_rect.center -= self.offset
					self.display_surface.blit(sprite.image, offset_rect)
