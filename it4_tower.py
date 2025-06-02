import pygame
import math

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.damage = 10
        self.range = 100
        self.fire_rate = 1000
        self.last_shot = 0
        self.cost = 50
        self.color = "blue"
        
    def draw(self, screen):
        center_x = self.x + 20
        center_y = self.y + 20
        pygame.draw.circle(screen, self.color, (center_x, center_y), 15)
        pygame.draw.circle(screen, "darkblue", (center_x, center_y), 15, 2)
        
    def draw_range(self, screen):
        center_x = self.x + 20
        center_y = self.y + 20
        pygame.draw.circle(screen, (0, 0, 255, 50), (center_x, center_y), self.range, 1)
        
    def can_shoot(self, current_time):
        return current_time - self.last_shot >= self.fire_rate
        
    def shoot(self, current_time):
        self.last_shot = current_time
        
    def get_center(self):
        return (self.x + 20, self.y + 20)