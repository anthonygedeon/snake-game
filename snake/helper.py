import random


def random_vector(x_range, y_range):
    x_start, x_stop, x_step = x_range
    y_start, y_stop, y_step = y_range
    x = random.randrange(x_start, x_stop, x_step)
    y = random.randrange(y_start, y_stop, y_step)
    return x, y


def find_availabe_spot(coordinate_list):
    while True:
        x, y = random_vector((0, 500, 20), (0, 400, 20))
        for coordinate in coordinate_list:
            if coordinate.x is not x and coordinate.y is not y:
                return x, y
