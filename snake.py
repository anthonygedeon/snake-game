import controller
import game

import pygame

class Snake(controller.Controller):

    def __init__(self):
        super().__init__()
        self.width = 20

    def set_position(self, x, y):
        self.position = pygame.Vector2(x, y)

    def get_position(self):
        return self.position

    def die(self, snake_body):
        self.reset_movement_state()
        self.set_position(240, 180)
        if len(snake_body) > 1:
            return [snake_body[-1]]
        else:
            return snake_body

    def grow(self, snake_body):
        snake_body.insert(0, self)

    def shift_snake_body(self):
        pass

    def draw_snake(self):
        pygame.draw.rect(game.game.screen, color=game.game.colors["green"], rect=[
            self.position.x, 
            self.position.y, 
            self.width, 
            self.width
        ])

