import sys, pygame
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()


class Sprite():
	position = (0,0)
	def __init__(self):
		pass

	def blit(self, win):
		pass

	def isColliding(self):
		print(self.position)

class Window():
	def __init__(self, width, height):
		self.size = (width, height)
		self.screen = pygame.display.set_mode(self.size)

class Tank(Sprite):
	def __init__(self):
		self.__sprites__ = {
			'up':pygame.image.load('sprites/tank_up.bmp'),
			'down':pygame.image.load('sprites/tank_down.bmp'),
			'left':pygame.image.load('sprites/tank_left.bmp'),
			'right':pygame.image.load('sprites/tank_right.bmp')
		}
		self.sprite = self.__sprites__['up']
		self.position = (400, 300)
		self.direction = (0,-1)
		self.gun_position = (400+32, 300)

	def move(self):
		self.position = (
			self.position[0]+self.direction[0],
			self.position[1]+self.direction[1],
			)
		dir_vector = {-1: 0, 0: 16, 1: 32}
		self.gun_position = (self.position[0]+dir_vector[self.direction[0]], self.position[1]+dir_vector[self.direction[1]])

	def turn(self, direction):
		if direction == 'left':
			self.direction = (-1, 0)
		elif direction == 'right':
			self.direction = (1, 0)
		elif direction == 'up':
			self.direction = (0, -1)
		elif direction == 'down':
			self.direction = (0, 1)
		self.sprite = self.__sprites__[direction]

	def blit(self, win):
		win.screen.blit(self.sprite, self.position)


class Bullet(Sprite):
	def __init__(self, position=(400, 300), direction=(0,-1)):
		self.position = position
		self.direction = direction
		self.color = pygame.Color(255,100,0)
		self.speed = 4

	def move(self):
		self.position = (
			self.position[0]+(self.direction[0]*self.speed),
			self.position[1]+(self.direction[1]*self.speed),
			)

	def blit(self, win):
		win_size = win.size
		if (self.position[0] > 0) and \
				(self.position[0] < win_size[0]) and \
				(self.position[1] > 0) and \
				(self.position[1]< win_size[1]):
			pygame.draw.circle(win.screen, self.color, self.position, 3, 0)


width, height = 800, 600

win = Window(width, height)
tank = Tank()

black = 0, 0, 0

bullets = []

while True:
    win.screen.fill(black)
    tank.move()
    tank.blit(win)
    for bullet in bullets:
    	bullet.move()
    	bullet.blit(win)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
        	if event.key == K_UP:
        		tank.turn('up')
        	elif event.key == K_DOWN:
        		tank.turn('down')
        	elif event.key == K_LEFT:
        		tank.turn('left')
        	elif event.key == K_RIGHT:
        		tank.turn('right')
        	elif event.key == K_SPACE:
        		bullets.append(Bullet(tank.gun_position, tank.direction))
        		tank.isColliding()


    pygame.display.update()
    fpsClock.tick(30)

