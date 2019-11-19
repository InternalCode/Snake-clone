import pygame, os, random

class Snack(pygame.sprite.Sprite):
	def __init__(self, settings):
		super(Snack, self). __init__()
		
		self.settings = settings
		#graphics
		self.image = pygame.image.load(os.path.join('graphics', 'snack', 'snack.png')).convert_alpha()
		self.image = pygame.transform.scale(self.image, (settings.size, settings.size))
		self.rect = self.image.get_rect()

		self.rect.x = (random.randint(1, (self.settings.screen_size / self.settings.size)) - 1) * self.settings.size
		self.rect.y = (random.randint(1, (self.settings.screen_size / self.settings.size)) - 1) * self.settings.size
		self.exists = True
		
	def update(self, snake, tail):
		
		while self.exists == False:
			collide_head = False
			collide_tail = False
			self.rect.x = (random.randint(1, (self.settings.screen_size / self.settings.size)) - 1) * self.settings.size
			self.rect.y = (random.randint(1, (self.settings.screen_size / self.settings.size)) - 1) * self.settings.size
			if self.rect.colliderect(snake):
				collide_head = True
			for i in range(len(tail.tail_rect)):
				if self.rect.colliderect(tail.tail_rect[i]):
					collide_tail = True
			if collide_head == False and collide_tail == False:
				self.exists = True
			# ~ else:
				# ~ collide_head = False
				# ~ collide_tail = False


	def draw(self, screen):
		screen.blit(self.image, self.rect)
		

















