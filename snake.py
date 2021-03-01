import sys
import math

import pygame

pygame.init()

width = 500
height = 400
screen = pygame.display.set_mode([width, height])

green = (0, 128 ,0)

x = 0
y = 0 

rectangle = (
    x,
    y,
    20,
    20
)

running = True

colNumber = 0
rowNumber = 0

while running:

    screen.fill((0, 0, 0))

    # USER INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                
                x += 10

            if event.key == pygame.K_LEFT:
                x -= 10

            if event.key == pygame.K_UP:
                y += 10

            if event.key == pygame.K_DOWN:
                y -= 10

    for col in range(1, int(width / 20)):

        colNumber += 20
        pygame.draw.line(screen, (255, 255, 255), [colNumber, 0], [colNumber, height], 1)

    for row in range(0, int(height / 20)):

        rowNumber += 20

        pygame.draw.line(screen, (255, 255, 255), (0, rowNumber), (0 + width * math.cos(0), rowNumber + width * math.sin(0)), 1)

    pygame.draw.rect(screen, color=green, rect=rectangle)

    pygame.display.flip()

pygame.quit()
sys.exit()