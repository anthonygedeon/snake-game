import pygame


class Controller:

    direction = {"right": False, "left": False, "up": False, "down": False}

    def __init__(self):
        self.position = pygame.Vector2(240, 180)

    def reset_movement_state(self):
        self.direction["right"] = False
        self.direction["left"] = False
        self.direction["up"] = False
        self.direction["down"] = False

    def move_right(self):
        self.reset_movement_state()
        self.direction["right"] = True

    def move_left(self):
        self.reset_movement_state()
        self.direction["left"] = True

    def move_up(self):
        self.reset_movement_state()
        self.direction["up"] = True

    def move_down(self):
        self.reset_movement_state()
        self.direction["down"] = True

    def _continous_movement(self):
        if self.direction["right"]:
            self.move_right()
            self.position.x += 20
        elif self.direction["left"]:
            self.move_left()
            self.position.x -= 20
        elif self.direction["up"]:
            self.move_up()
            self.position.y -= 20
        elif self.direction["down"]:
            self.move_down()
            self.position.y += 20
