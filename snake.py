import sys
import math

import pygame

pygame.init()

width = 500
height = 400
screen = pygame.display.set_mode([width, height])

green = (0, 128 ,0)

x = width / 2
y = height / 2

rectangle = (
    x,
    y,
    10,
    10
)

colNumber = 0
rowNumber = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(screen, color=green, rect=rectangle)

    # Draw grid

    for col in range(1, int(width / 10)):

        pygame.draw.line(screen, (255, 255, 255), [colNumber, 0], [colNumber, height], 1)

        colNumber += 10        

        for row in range(0, int(height / 10)):
            # pygame.draw.line(screen, (255, 255, 255), [0, rowNumber], [rowNumber, math.sin(math.radians(270)) * height], 1)

            rowNumber += 10

    pygame.display.flip()

pygame.quit()