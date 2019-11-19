import pygame, time, os

class Gamecontrol():
	def __init__(self, active = False):
		self.font = pygame.font.Font(os.path.join('font', 'font.ttf'), 24)
		self.active = active
		self.cleaning = False
		self.timer = int()
		self.score = 0
		
	def update(self, snake):
		if self.active == True:
			self.timer = round(time.time()) + 5
		if snake.end == True:
			self.score = 0
			self.active = False
			self.cleaning = True
			
	def draw(self, screen):
		text_score = self.font.render(str(self.score), True, (250,250,250))
		text_score_rect = text_score.get_rect()
		text_score_rect.x = 10
		text_score_rect.y = 5
		screen.blit(text_score, text_score_rect)
