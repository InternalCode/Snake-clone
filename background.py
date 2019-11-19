import pygame, os

class Background():
	def __init__(self, settings):
		
		self.image = pygame.image.load(os.path.join('graphics', 'background', 'background.jpg')).convert()
		self.rect = self.image.get_rect()
		self.rect.centerx = settings.screen_size / 2
		self.rect.centery = settings.screen_size / 2
	
	def draw(self, screen):
		screen.blit(self.image, self.rect)
		
