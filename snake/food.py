import random

import game

from helper import find_availabe_spot

import pygame


class Food:
    def __init__(self):

        self.x = random.randrange(0, 500, 20)
        self.y = random.randrange(0, 400, 20)

        self.color = (255, 0, 0)
        self.width = 20
        self.position = pygame.Vector2(self.x, self.y)

    def get_location(self):
        return self.position

    def change_location(self):
        self.x, self.y = find_availabe_spot(game.taken_spots)
        self.position = pygame.Vector2(self.x, self.y)

    def draw_food(self):
        pygame.draw.rect(
            game.game.screen,
            color=self.color,
            rect=[self.position.x, self.position.y, self.width, self.width],
        )
