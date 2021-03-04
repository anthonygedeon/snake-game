import sys
import math
import random

import pygame

pygame.init()

width = 500
height = 400
fps = 5

screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)

x = 240
y = 180

class Window:

    def __init__(self, window):
        self.window = window
    
    def get_window_dimension(self):
        return {
            "width":  self.window.display.get_surface().get_width(),
            "height": self.window.display.get_surface().get_height()
        }

class Physics:

    @staticmethod 
    def is_collision_detection(object1, object2):
        if object1.x > object2["width"]:
            return True
        elif object1.y > object2["height"]:
            return True
        elif object1.x < 0:
            return True
        elif object1.y < 0:
            return True

        return False

    def is_squares_colliding(square1, square2):
        if square1.x == square2.x and square1.y == square2.y:
            return True
        
        return False

    @staticmethod
    def __collision_detection(object1, object2):
        pass
        


class Controller:

    direction = {
        "right": False,
        "left": False,
        "up": False,
        "down": False
    }

    def reset_movement_state(self):
        self.direction["right"] = False
        self.direction["left"] = False
        self.direction["up"] = False
        self.direction["down"] = False

    def move_right(self):
        self.reset_movement_state()
        self.direction["right"] = True

    def move_left(self):
        self.reset_movement_state()
        self.direction["left"] = True

    def move_up(self):
        self.reset_movement_state()
        self.direction["up"] = True

    def move_down(self):
        self.reset_movement_state()
        self.direction["down"] = True

    def continous_movement(self):
        global x
        global y
        if self.direction["right"]:
            self.move_right()
            x += 20
        elif self.direction["left"]:
            self.move_left()
            x -= 20
        elif self.direction["up"]:
            self.move_up()
            y -= 20
        elif self.direction["down"]:
            self.move_down()
            y += 20

class Snake(Controller):

    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = width
    
    def set_position(self):
        global x
        global y
        x = 240 # middle x
        y = 180 # middle y

    def die(self):
        self.reset_movement_state()
        self.set_position()

    def eat(self):
        pass

    def grow(self):
        pass

    def draw_snake(self):
        pygame.draw.rect(screen, color=GREEN, rect=[
            self.x, 
            self.y, 
            self.width, 
            self.width
        ])

class Fruit:

    def __init__(self):

        self.x = random.randrange(0, width, 20)
        self.y = random.randrange(0, height, 20)

        self.color = RED
        self.width = 20
        self.pos = pygame.Vector2(self.x, self.y)

    def get_location(self):
        return self.pos

    def change_location(self):
        self.__init__() # TODO: update x, y coordinates without invoking the init method

    def draw_fruit(self):
        pygame.draw.rect(screen, color=self.color, rect=[
            self.pos.x, 
            self.pos.y, 
            self.width, 
            self.width
        ])

fruit = Fruit()

class Cell:
    
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = width

    def create_cell(self):
        return (
            self.x,
            self.y,
            self.width,
            self.height
        )

class Grid:
    
    def __init__(self, window):
        self.window = window
        self.grid = []
    
    def get_columns(self):
        return math.floor(self.window.get("width") / snake.width)

    def get_rows(self):
        return math.floor(self.window.get("height") / snake.width)

    def get_total_number_of_cells(self):
        return self.get_columns() * self.get_rows()
    
    def create_grid(self):
        for row in range(0, self.get_rows()):
            self.grid.append([])
            for col in range(0, self.get_columns()):
                self.grid[row].append(Cell(col * snake.width, row * snake.width, snake.width))

        return self.grid

    def draw_grid(self):
        matrix_grid = self.create_grid()

        for row in range(len(matrix_grid)):
            for col in range(len(matrix_grid[row])):
                pygame.draw.rect(screen, WHITE, matrix_grid[row][col].create_cell(), 1)

        return

running = True

window = Window(pygame)
grid = Grid(window.get_window_dimension())

while running:
    screen.fill(BLACK)
    clock.tick(fps)
    snake = Snake(x, y, 20)

    # User Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Control Sprite
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.move_right()

            if event.key == pygame.K_LEFT:
                snake.move_left()

            if event.key == pygame.K_UP:
                snake.move_up()

            if event.key == pygame.K_DOWN:
                snake.move_down()

    snake.draw_snake()

    fruit.draw_fruit()

    snake.continous_movement()

    # DEBUGGING METHOD
    grid.draw_grid()

    if Physics.is_collision_detection(snake, window.get_window_dimension()):
        snake.die()
    
    if Physics.is_squares_colliding(snake, fruit.get_location()):
        snake.grow()
        fruit.change_location()

    pygame.display.update()

pygame.quit()
sys.exit()