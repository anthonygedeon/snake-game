import random

import pygame

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