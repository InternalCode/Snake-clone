import pygame, os, time

class Menu():
	def __init__(self, settings, ico):
		self.settings = settings
		self.rect = pygame.Rect(0,0, settings.screen_size, settings.screen_size)
		
		self.ico = pygame.transform.scale(ico, (256,256))
		self.ico_rect = self.ico.get_rect()
		self.ico_rect.centerx = self.settings.screen_size / 2
		self.ico_rect.top = 60
		
		
		self.font = pygame.font.Font(os.path.join('font', 'font.ttf'), 24)
		self.text_start = self.font.render('Press space to start', True, (250,250,250))
		self.text_start_rect = self.text_start.get_rect()
		self.text_start_rect.centerx = settings.screen_size / 2 
		self.text_start_rect.centery = settings.screen_size - 30 
		
		self.text_end = self.font.render('End.', True, (250,250,250))
		self.text_end_rect = self.text_end.get_rect()
		self.text_end_rect.centerx = settings.screen_size / 2 
		self.text_end_rect.centery = settings.screen_size - 30 
		
			
	def draw(self, screen, gamecontrol):
		if gamecontrol.active == False:
			screen.blit(self.text_end, self.text_end_rect)
			if gamecontrol.timer < round(time.time()):
				pygame.draw.rect(screen, (0,0,0, 50), self.rect)
				screen.blit(self.text_start, self.text_start_rect)
				screen.blit(self.ico, self.ico_rect)

