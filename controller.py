class Controller:
    
    direction = {
        "right": False,
        "left": False,
        "up": False,
        "down": False
    }

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

    def continous_movement(self):
        global x
        global y
        if self.direction["right"]:
            self.move_right()
            x += 20
        elif self.direction["left"]:
            self.move_left()
            x -= 20
        elif self.direction["up"]:
            self.move_up()
            y -= 20
        elif self.direction["down"]:
            self.move_down()
            y += 20