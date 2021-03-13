import random

import game

import pygame

class Fruit:
    
    def __init__(self):

        self.x = random.randrange(0, 500, 20)
        self.y = random.randrange(0, 400, 20)

        self.color = (255, 0, 0)
        self.width = 20
        self.position = pygame.Vector2(self.x, self.y)

    def get_location(self):
        return self.position

    def change_location(self):
        self.__init__() # TODO: update x, y coordinates without invoking the init method

    def draw_fruit(self):
        pygame.draw.rect(game.game.screen, color=self.color, rect=[
            self.position.x, 
            self.position.y, 
            self.width, 
            self.width
        ])