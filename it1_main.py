# Importing modules
import pygame
from sys import exit

pygame.init()

# Creating the game window
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tower Defense")

# Game clock
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
