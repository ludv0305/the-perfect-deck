import pygame
import sys

WIDTH, HEIGHT = 400, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("deck hunter")

BG_COLOUR = 72, 205, 51

enemy_1_colour = 255, 0, 0

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, height, width, health = 100):
		self.x = x
		self.y = y
		self.health = health
		self.height = height
		self.width = width
		self.lasers = []
		self.cool_down_counter = 0

	def draw(self, WIN, height, width):
		pygame.draw.rect(WIN, (255, 255, 255), (self.x, self.y, width, height))


class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y, size, health = 100):
		self.x = x
		self.y = y
		self.health = health
		self.size = size
		self.lasers = []
		self.cool_down_counter = 0

	def draw(self, WIN, colour, size):
		pygame.draw.circle(WIN, colour, [self.x, self.y], size)


def main():
	run = True
	FPS = 60
	vel = 4

	player = Player(200, 500, 50, 30)

	enemy_1 = Enemy(50, 50, 25)
	enemy_2 = Enemy(200, 50, 25)
	enemy_3 = Enemy(350, 50, 25)

	def detectCollisions(player_x, player_y, player_height, player_width, enemy_y, enemy_x, enemy_height, enemy_width):
		if (enemy_x + enemy_width >= player_x >= enemy_x and enemy_y + enemy_height >= player_y >= enemy_y):
			return True

		elif (enemy_x + enemy_width >= player_x + player_width and enemy_y + enemy_height >= player_y >= enemy_x):
			return True

		elif (enemy_x + enemy_width >= player_x >= enemy_x and enemy_y + enemy_height >= player_y + player_height >= enemy_y):
			return True

		elif (enemy_x + enemy_width >= player_x + player_width and enemy_y + enemy_height >= player_y + player_height >= enemy_x):
			return True

		else:
			return False



	def reddrawwindow():
		WIN.fill((BG_COLOUR))
		
		player.draw(WIN, 50, 30)

		enemy_1.draw(WIN, enemy_1_colour, 25)
		enemy_2.draw(WIN, enemy_1_colour, 25)
		enemy_3.draw(WIN, enemy_1_colour, 25)

		enemy_1.y += 1
		enemy_2.y += 1
		enemy_3.y += 1

		pygame.display.update()

	clock = pygame.time.Clock()

	while run:

		clock.tick(FPS)
		reddrawwindow()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		key = pygame.key.get_pressed()

		if key[pygame.K_RIGHT]:
			player.x += vel
		if key[pygame.K_LEFT]:
			player.x -= vel

		collission_1 = detectCollisions(player.x, player.y, player.height, player.width, enemy_1.y, enemy_1.x, enemy_1.size, enemy_1.size)
		collission_2 = detectCollisions(player.x, player.y, player.height, player.width, enemy_2.y, enemy_2.x, enemy_2.size, enemy_2.size)
		collission_3 = detectCollisions(player.x, player.y, player.height, player.width, enemy_3.y, enemy_3.x, enemy_3.size, enemy_3.size)
		if (collission_1 == True) or (collission_2 == True) or (collission_3 == True):
			run = False


main()
