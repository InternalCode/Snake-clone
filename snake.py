import pygame, random, os

class Snake(pygame.sprite.Sprite):
	def __init__(self, settings):
		super(Snake, self). __init__()
		self.settings = settings
		#graphics head
		self.image = pygame.image.load(os.path.join('graphics', 'head', 'head.png')).convert_alpha()
		self.image = pygame.transform.scale(self.image, (self.settings.size, self.settings.size))
		self.rect = self.image.get_rect()
		self.rect.x = settings.screen_size / 2
		self.rect.y = settings.screen_size / 2
		#flags
		
		self.end = False

		#direction and random start
		self.direction = random.choice(['up', 'down', ' left', 'right'])
		self.course = ''

	def draw(self, screen):
		screen.blit(self.image, self.rect)

	def update(self, tail, snack, gamecontrol):
		#print tail
		tail.update(self.rect)
		# ~ print('direction :', self.direction)
		# ~ print('course    :', self.course)
		self.update_direction()
		self.check_for_edges()
		self.check_for_snack(tail, snack, gamecontrol)
		self.check_for_tail(tail)

		
	def check_for_edges(self):
		# ~ if self.rect.left < 0 or\
			# ~ self.rect.top < 0 or\
			# ~ self.rect.right > self.settings.screen_size or\
			# ~ self.rect.bottom > self.settings.screen_size:
				# ~ print('snake reach screen limit')

		# pass to opposite site
		if self.rect.left < 0:
			self.rect.right = self.settings.screen_size
		if self.rect.top < 0:
			self.rect.bottom = self.settings.screen_size
		if self.rect.right > self.settings.screen_size:
			self.rect.left = 0
		if self.rect.bottom > self.settings.screen_size:
			self.rect.top = 0
	
	def check_for_tail(self, tail):
		for tail in tail.tail_rect:
			if self.rect.colliderect(tail):
				self.end = True


	def check_for_snack(self, tail, snack, gamecontrol):
		if self.rect.colliderect(snack.rect):
			tail.length += 1
			gamecontrol.score += 1
			snack.exists = False

	def update_direction(self):
		#backflow limit 
		if self.course == 'up' and self.direction == 'down':
			self.direction = 'up'
			
		if self.course == 'down' and self.direction == 'up':
			self.direction = 'down'
		
		if self.course == 'left' and self.direction == 'right':
			self.direction = 'left'

		if self.course == 'right' and self.direction == 'left':
			self.direction = 'right'

		#changing directions
		if self.direction == 'up':
			self.rect.y -= self.settings.size
			self.course = 'up'

		if self.direction == 'down':
			self.rect.y += self.settings.size
			self.course = 'down'
			
		if self.direction == 'left':
			self.rect.x -= self.settings.size
			self.course = 'left'
			
		if self.direction == 'right':
			self.rect.x += self.settings.size
			self.course = 'right'
