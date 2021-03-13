import controller
import game

import pygame

class Snake(controller.Controller):

    def __init__(self):
        super().__init__()
        self.width = 20

    def set_position(self):
        Snake.__init__(self)

    def die(self):
        self.reset_movement_state()
        self.set_position()

    def grow(self, body):
        pass

    def shift_snake_body(self):
        pass

    def draw_snake(self):
        #for body in snake_body:
        pygame.draw.rect(game.game.screen, color=game.game.colors["green"], rect=[
            self.position.x, 
            self.position.y, 
            self.width, 
            self.width
        ])

