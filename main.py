#python 3.7
import logging, pygame, os
import functions
from snake import Snake
from settings import Settings
from tail import Tail
from snack import Snack
from background import Background
from menu import Menu
from gamecontrol import Gamecontrol

def start():
	pygame.display.init()
	pygame.font.init()
	ico = pygame.image.load(os.path.join('graphics', 'ico', 'ico.png'))
	pygame.display.set_icon(ico)
	pygame.display.set_caption('Snake')
	settings = Settings()
	screen = pygame.display.set_mode(size = (settings.screen_size, settings.screen_size),
			flags = pygame.DOUBLEBUF, depth = 16)
	fps_clock = pygame.time.Clock()
	tail = Tail(settings)
	snake = Snake(settings)
	snack = Snack(settings)
	background = Background(settings)
	gamecontrol = Gamecontrol()
	menu = Menu(settings, ico)
	
	while True:
		if gamecontrol.cleaning:
			del snake
			del snack
			del tail			
			snake = Snake(settings)
			tail = Tail(settings)
			snack = Snack(settings)
			gamecontrol.cleaning = False
		functions.key_control(snake, gamecontrol)
		functions.gamecontrol_update(gamecontrol, snake)
		functions.update_draw_on_screen(screen, snake, tail, snack, background, menu, gamecontrol)
		if gamecontrol.active:
			functions.update_elements(settings, snake, tail, snack, gamecontrol)
		pygame.display.flip()
		fps_clock.tick(settings.fps)

if __name__ == '__main__':
	logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
	start()
