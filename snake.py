import sys
import math
import pprint

import pygame

pygame.init()

width = 500
height = 400

screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128 ,0)

x = 0
y = 0 

rectangle = (
    x,
    y,
    19,
    19
)

class Cell:
    
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = width

    def create_cell():
        pass

class Grid:
    
    def __init__(self, screen):
        self.screen = screen
        self.grid = []
    
    def get_columns(self):
        return math.floor(width / 20)

    def get_rows(self):
        return math.floor(height / 20)

    def get_total_number_of_cells(self):
        return self.get_columns() * self.get_rows()
    
    def create_grid(self):
        for row in range(0, self.get_rows()):
            self.grid.append([])
            for col in range(0, self.get_columns()):
                self.grid[row].append(Cell(col * 20, row * 20, 20))

        return self.grid

    def draw_grid(self):
        matrix_grid = self.create_grid()

        for row in range(len(matrix_grid)):
            for col in range(len(matrix_grid[row])):

                pygame.draw.rect(screen, WHITE, [
                    matrix_grid[row][col].x, 
                    matrix_grid[row][col].y, 
                    matrix_grid[row][col].width, 
                    matrix_grid[row][col].height], 1)

        return 0


running = True

grid = Grid(None)

grid.draw_grid()

while running:

    clock.tick(60)

    # USER INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Control Sprite
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pass

            if event.key == pygame.K_LEFT:
                pass

            if event.key == pygame.K_UP:
                pass

            if event.key == pygame.K_DOWN:
                pass

    pygame.draw.rect(screen, color=GREEN, rect=rectangle)

    # pygame.draw.rect(screen, WHITE, [0, 0, 20, 20], 1)

    # pygame.draw.rect(screen, WHITE, [20, 0, 20, 20], 1)

    # pygame.draw.rect(screen, WHITE, [20, 20, 20, 20], 1)

    pygame.display.flip()

pygame.quit()
sys.exit()