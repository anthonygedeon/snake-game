import controller
import game

import pygame

coordinate_list = []


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
        snake_body.insert(0, SnakeBody())

    def draw_snake(self):
        pygame.draw.rect(
            game.game.screen,
            color=game.game.colors["green"],
            rect=[self.position.x, self.position.y, self.width, self.width],
        )
        self._continous_movement()
        coordinate_list.append(self.position)


class SnakeBody:
    def __init__(self):
        self.position = pygame.Vector2(0, 0)
        self.width = 20

    def _delay_snake_movement(self, whole_snake):
        for i in range(1, len(whole_snake)):
            self.position = pygame.Vector2(coordinate_list[-i].x, coordinate_list[-i].y)
            whole_snake[-i].position = pygame.Vector2(
                coordinate_list[-i].x, coordinate_list[-i].y
            )

    def draw_snake_body(self):
        pygame.draw.rect(
            game.game.screen,
            color=game.game.colors["green"],
            rect=[self.position.x, self.position.y, self.width, self.width],
        )

        self._delay_snake_movement(game.snakes)
