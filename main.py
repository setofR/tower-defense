# Importing the required modules
import pygame
from sys import exit

# Initalising the pygame module
pygame.init()

# Game window properties
canvas = pygame.display.set_mode((800, 500), pygame.RESIZABLE)
pygame.display.set_caption("Tower Defense")

# Game clock
clock = pygame.time.Clock()
while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Elements
    canvas.fill("black")

    # Update
    pygame.display.update()
    clock.tick(60)
