from collections import namedtuple
from typing import Tuple, Optional, Union, Set, Dict, Any
import enum
import random
import numpy as np
import pygame


pygame.init()
SPEED = 5
BLACK = [0, 0, 0]
RED = [255, 0, 0]
WHITE = [255, 255, 255]
LIME = [0, 255, 0]
GOLD = [255, 215, 0]
BLOCK_SIZE = 30





class Point:
	__slots__ = ('x', 'y')
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

	def copy(self) -> 'Point':
		x = self.x
		y = self.y
		return Point(x, y)

	def __eq__(self, other):
		if isinstance(other, Point):
			return self.x == other.x and self.y == other.y

class Direction(enum.Enum):
	LEFT = 0
	UP = 1
	RIGHT = 2
	DOWN = 3



class Snake:
	def __init__(self, weights = None):
		start_pos = Point(5, 5)
		self.board_size = (20, 20)
		self._init_snake(start_pos)
		self._generate_apple()
		self.score = 0
		self.lifetime = 0


		# init snake
		# generate apple
	def _within_wall(self, position: 'Point'):
		return 0 <= position.x < self.board_size[0] and 0 <= position.y < self.board_size[1]
	def _is_body_location(self, position: Point):
		return position in self.snake_array
	def _is_apple_location(self, position):
		return position == self.apple_location

	def _init_snake(self, start_pos: Point) -> None:
		self.head = start_pos
		self.snake_array = [self.head, 
								 Point(self.head.x - 1, self.head.y), 
								 Point(self.head.x - 2, self.head.y)]
		self.is_alive = True


	def _generate_apple(self):
		width = self.board_size[0]
		height = self.board_size[1]

		possibilities = [divmod(i, height) for i in range(width * height) if divmod(i, height) not in self.snake_array] # OPTIMIZATION NEEDED
		if possibilities:
			loc = random.choice(possibilities)
			self.apple_location = Point(loc[0], loc[1])
		else:

			pass


	def _move(self, action) -> None:

		if action == Direction.LEFT.value:
			next_pos = Point(self.head.x - 1, self.head.y)
		elif action == Direction.UP.value:
			next_pos = Point(self.head.x, self.head.y - 1)
		elif action == Direction.RIGHT.value:
			next_pos = Point(self.head.x + 1, self.head.y)
		elif action == Direction.DOWN.value:
			next_pos = Point(self.head.x, self.head.y + 1)
		if self._within_wall(next_pos) and next_pos not in self.snake_array:
				self.snake_array.insert(0, next_pos)
				self.head = next_pos
				if self.head == self.apple_location:
					self._generate_apple()
					self.score += 1
					return
				self.snake_array.pop()
				return
		else:
			self.is_alive = False

			

	def play_step(self, action: int) -> None:
		# keyboard input
#		action = self.network.feed_forward(vision_array)

		self._move(action)
		self.lifetime += 1




class GameScreen:
	def __init__(self, width : int = 700, height : int = 700):
		self.run = True
		self.width = width
		self.height = height
		self.display = pygame.display.set_mode((self.width, self.height))
		self.draw = pygame.draw
		pygame.display.set_caption("Snake")
		self.clock = pygame.time.Clock()
	

	def rungame(self):
		while self.run:
			self.action = Direction.RIGHT.value
			self.snake = Snake()
			while self.snake.is_alive:
				self.update()


	def update(self):
		self.display.fill(WHITE)
		self.draw.rect(self.display, BLACK, (50, 50, BLOCK_SIZE * self.snake.board_size[0], BLOCK_SIZE * self.snake.board_size[1]))
		for position in self.snake.snake_array:
			self.draw.rect(self.display, LIME, (50 + position.x * BLOCK_SIZE, 50 + position.y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1)) # draw full snake
		self.draw.rect(self.display, GOLD, (50 + self.snake.head.x * BLOCK_SIZE, 50 + self.snake.head.y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1)) # draw just head with diff colour
		self.draw.rect(self.display, RED, (50 + self.snake.apple_location.x * BLOCK_SIZE, 50 + self.snake.apple_location.y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1)) # draw apple
		pygame.display.flip()
		pygame.time.delay(int(1000 / SPEED))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					self.action = Direction.LEFT.value
				elif event.key == pygame.K_w:
					self.action = Direction.UP.value
				elif event.key == pygame.K_d:
					self.action = Direction.RIGHT.value
				elif event.key == pygame.K_s:
					self.action = Direction.DOWN.value

		self.snake.play_step(self.action)





screen = GameScreen()
screen.rungame()





