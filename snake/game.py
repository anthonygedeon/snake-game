import sys

import window
import food
import grid
import snake as player
import physics

import pygame

food = food.Food()
snakes = [player.Snake()]
taken_spots = None


class Game:
    def __init__(self, width, height, frame_per_second):

        pygame.init()

        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = frame_per_second
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.colors = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "red": (255, 0, 0),
            "green": (0, 128, 0),
        }

    def game_loop(self):
        global snakes
        global taken_spots
        while self.running:

            self.screen.fill(self.colors["black"])

            # User Input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

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

            for snake in snakes:

                taken_spots = [coordinate.position for coordinate in snakes]

                if isinstance(snake, player.Snake):
                    snake.draw_snake()

                    if physics.Physics.is_collision_detection(
                        snake.position, window.get_window_dimension()
                    ):
                        snakes = snake.die(snakes)
                        food.change_location()

                    if physics.Physics.is_squares_colliding(
                        snake.position, food.get_location()
                    ):
                        snake.grow(snakes)
                        food.change_location()

                elif isinstance(snake, player.SnakeBody):
                    snake.draw_snake_body()

            food.draw_food()

            self.clock.tick(self.fps)

            pygame.display.update()


game = Game(500, 400, 10)

window = window.Window(pygame)
grid = grid.Grid(window.get_window_dimension())

game.game_loop()

pygame.quit()

sys.exit()
