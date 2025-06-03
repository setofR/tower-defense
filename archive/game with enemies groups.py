# Importing the required modules
import pygame
from archive.enemy import Enemy
from sys import exit

# Initalising the pygame module
pygame.init()

# Creating the game's window
screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE)
pygame.display.set_caption("Tower Defense")


# load images
enemy_image = pygame.image.load("assets/images/enemies/bad_enemy.png").convert_alpha()

# create groups
enemy_group = pygame.sprite.Group()

keyframes = [(100, 100), (300, 150), (300, 100), (200, 100)]

enemy = Enemy(keyframes, enemy_image)
enemy_group.add(enemy)

# Game clock
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw all our elements
    screen.fill("grey100")
    enemy_group.draw(screen)

    # draw enemy path
    pygame.draw.lines(screen, "grey0", False, keyframes)
    # update everything
    pygame.display.update()
    clock.tick(60)

    enemy_group.update()
