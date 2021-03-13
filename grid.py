import math

import snake

import pygame

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
        return math.floor(self.window.get("width") / snake.snake.width.width)

    def get_rows(self):
        return math.floor(self.window.get("height") / snake.snake.width.width)

    def get_total_number_of_cells(self):
        return self.get_columns() * self.get_rows()
    
    def create_grid(self):
        for row in range(0, self.get_rows()):
            self.grid.append([])
            for col in range(0, self.get_columns()):
                self.grid[row].append(Cell(col * snake.snake.width.width, row * snake.snake.width.width, snake.snake.width.width))

        return self.grid

    def draw_grid(self):
        matrix_grid = self.create_grid()

        for row in range(len(matrix_grid)):
            for col in range(len(matrix_grid[row])):
                pygame.draw.rect(snake.game.screen, snake.game.colors["white"], matrix_grid[row][col].create_cell(), 1)

        return