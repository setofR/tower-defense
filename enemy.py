import pygame
from pygame.math import Vector2
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self, keyframes, image):
        pygame.sprite.Sprite.__init__(self)
        self.keyframes = keyframes
        self.pos = Vector2(self.keyframes[0])
        self.target_keyframe = 1
        self.speed = 2
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.move()

    def move(self):
        # define target keyframe
        if self.target_keyframe < len(self.keyframes):
            self.target = Vector2(self.keyframes[self.target_keyframe])
            self.movement = self.target - self.pos
        else:
            # enemy has reached end of path
            self.kill()

        # calculate distance to target
        distance = self.movement.length()
        # checks if remaining distance is greater than the enemy speed
        if distance >= self.speed:
            self.pos += (
                self.movement.normalize() * self.speed
            )  # normalise calculates pixel distance between next keyframe
        else:
            if distance != 0:
                self.pos += self.movement.normalize() * distance
            self.target_keyframe += 1

        self.rect.center = self.pos
