import pygame
from settings import *
from random import randint, choice


class Generic(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups, z = LAYERS['main']):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(bottomleft = pos)
		self.z = z
		self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)

class Objects(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups, player_add,questions,answer,z = LAYERS['main'] ):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(center = pos)
		self.z = z
		self.question = 1
		self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)
		self.player_add = player_add  # 声明player_add属性
		self.questions = questions
		self.answer = answer

class stones(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups, z = LAYERS['main']):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(bottomleft = pos)
		self.z = z
		self.hitbox = self.rect.copy()

class target_monster(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups, z = LAYERS['main']):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(bottomleft = pos)
		self.monster = 1
		self.z = z
		self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)
