import sys

from window import Window
from grid import Grid
from physics import Physics
from controller import Controller
from fruit import Fruit

import pygame

window = Window(pygame)
grid = Grid(window.get_window_dimension())
fruit = Fruit()

class Game:

    def __init__(self, 
    width, 
    height, 
    frame_per_second):

        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = frame_per_second
        self.width = width
        self.height = height
        self.screen =  pygame.display.set_mode([self.width, self.height])
        self.colors = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "red": (255, 0, 0),
            "green": (0, 128, 0)
        }

    def game_loop(self):
        while self.running:

            self.screen.fill(self.colors["black"])
            self.clock.tick(self.fps)
        
            snake = Snake(x, y, 20)
            # print(snake_body)

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

            snake.draw_snake()

            fruit.draw_fruit()

            snake.continous_movement()

            # DEBUGGING METHOD
            # grid.draw_grid()

            if Physics.is_collision_detection(snake, window.get_window_dimension()):
                snake.die()
                fruit.change_location()
            
            if Physics.is_squares_colliding(snake, fruit.get_location()):
                snake.grow(snake)
                fruit.change_location()

            pygame.display.update()


class Snake(Controller):

    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.pos = pygame.Vector2(x, y);
        self.width = width
    
    def set_position(self):
        global x
        global y
        x = 240 # middle x
        y = 180 # middle y

    def die(self):
        self.reset_movement_state()
        self.set_position()

    def grow(self, body):
        # print(snake_body)
        # snake_body.insert(1, body)
        pass

    def shift_snake_body(self):
        pass

    def draw_snake(self):
        #for body in snake_body:
        pygame.draw.rect(screen, color=GREEN, rect=[
            self.x, 
            self.y, 
            self.width, 
            self.width
        ])

game = Game(500, 400, 5)

game.game_loop()

pygame.quit()

sys.exit()