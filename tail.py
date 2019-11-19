#python 3.7
import pygame, os

class Tail(pygame.sprite.Sprite):
	def __init__(self, settings):
		super(Tail, self). __init__()
		self.settings = settings
		self.tail_rect = list()

		self.image = pygame.image.load(os.path.join('graphics', 'tail', 'tail.png')).convert_alpha()
		self.image = pygame.transform.scale(self.image, (settings.size, settings.size))
		self.length = 0
		
	def update(self, head_rect):
		rect = pygame.Rect(head_rect)
		self.tail_rect.insert(0, rect)
		self.tail_rect = self.tail_rect[:self.length]
		
	def draw(self, screen):
		scale = self.settings.size
		for tail in self.tail_rect:
			if scale > 12:
				scale -= 2
			screen.blit(pygame.transform.scale(self.image, (scale, scale)),
							(tail.centerx - int(scale / 2), tail.centery - int(scale / 2)))
			




