import sys
import math

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

x = 0
y = 0

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
    def collision_detection(object1, object2):
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

    def __init__(self, width):
        self.width = width
        self.height = width
    
    def set_position(self):
        global x
        global y
        x = 50
        y = 50

    def die(self):
        pass

    def eat(self):
        pass

    def grow(self):
        pass

    def draw_snake(self):
        pygame.draw.rect(screen, color=GREEN, rect=[x, y, self.width, self.width])

snake = Snake(20)

class Fruit:

    def __init__(self, color):
        self.color = color

    def get_position(self):
        pass

    def set_position(self):
        pass

    def draw_fruit(self):
        pass


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

    snake.continous_movement()

    # DEBUGGING METHOD
    grid.draw_grid()
    
    pygame.display.update()

pygame.quit()
sys.exit()