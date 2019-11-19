import logging, pygame, sys

def update_elements(settings, snake, tail, snack, gamecontrol):
	snake.update(tail, snack, gamecontrol)
	snack.update(snake, tail)

def update_draw_on_screen(screen, snake, tail, snack, background, menu, gamecontrol):
	if gamecontrol.active:
		background.draw(screen)
		snake.draw(screen)
		tail.draw(screen)
		snack.draw(screen)
		gamecontrol.draw(screen)
	else:
		menu.draw(screen, gamecontrol)
	
def gamecontrol_update(gamecontrol, snake):
	gamecontrol.update(snake)

def key_control(snake, gamecontrol):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
				sys.exit()
			if event.key == pygame.K_UP:
				snake.direction = 'up'
			if event.key == pygame.K_DOWN:
				snake.direction = 'down'
			if event.key == pygame.K_LEFT:
				snake.direction = 'left'
			if event.key == pygame.K_RIGHT:
				snake.direction = 'right'
			if event.key == pygame.K_SPACE:
				gamecontrol.active = True
