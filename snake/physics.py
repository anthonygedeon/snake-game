class Physics:
    @staticmethod
    def is_collision_detection(object1, object2):
        if int(object1.x) > int(object2["width"]):
            return True
        elif int(object1.y) > int(object2["height"]):
            return True
        elif object1.x < 0:
            return True
        elif object1.y < 0:
            return True

        return False

    @staticmethod
    def is_squares_colliding(square1, square2):
        if square1.x == square2.x and square1.y == square2.y:
            return True

        return False

    @staticmethod
    def is_snakehead_colliding_with_body(head, body):
        pass
