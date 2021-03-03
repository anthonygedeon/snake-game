import sys
import math

import pygame

pygame.init()

width = 500
height = 400

screen = pygame.display.set_mode([width, height])

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128 ,0)

x = 0
y = 0 

rectangle = (
    x,
    y,
    20,
    20
)

class Grid:
    
    grid = []

    def __init__(self, screen):
        self.screen = screen
        

    def get_columns(self):
        return math.floor(self.screen.width / 50)

    def get_rows(self):
        return math.floor(self.screen.height / 40)

    def get_total_number_of_cells(self):
        return self.get_columns * self.get_rows
    
    def create_grid(self):
        
        for row in self.get_rows():
            for col in self.get_columns():
                pass

    

class Cell:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def create_cell():
        pass

running = True

while running:

    screen.fill((0, 0, 0))

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

    pygame.display.flip()

pygame.quit()
sys.exit()