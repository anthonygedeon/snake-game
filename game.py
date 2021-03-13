import sys

import window
import fruit
import grid
import snake
import physics

import pygame

fruit = fruit.Fruit()
snake = snake.Snake()

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

            if physics.Physics.is_collision_detection(snake.position, window.get_window_dimension()):
                snake.die()
                fruit.change_location()
            
            if physics.Physics.is_squares_colliding(snake.position, fruit.get_location()):
                snake.grow(snake)
                fruit.change_location()

            pygame.display.update()

game = Game(500, 400, 5)

window = window.Window(pygame)
grid = grid.Grid(window.get_window_dimension())

game.game_loop()

pygame.quit()

sys.exit()