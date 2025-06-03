import pygame
import math

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 20
        self.range = 120
        self.fire_rate = 1000
        self.last_shot = 0
        self.cost = 50
        self.size = 15
        self.color = "darkblue"
        
    def draw(self, screen):
        center_x = self.x + 20
        center_y = self.y + 20
        pygame.draw.circle(screen, self.color, (center_x, center_y), self.size)
        pygame.draw.circle(screen, "black", (center_x, center_y), self.size, 2)
    
    def draw_range(self, screen):
        center_x = self.x + 20
        center_y = self.y + 20
        range_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA)
        pygame.draw.circle(range_surface, (0, 0, 255, 50), (self.range, self.range), self.range)
        screen.blit(range_surface, (center_x - self.range, center_y - self.range))
    
    def get_center(self):
        return (self.x + 20, self.y + 20)
    
    def can_attack(self, enemy):
        center_x, center_y = self.get_center()
        distance = math.sqrt((enemy.x - center_x)**2 + (enemy.y - center_y)**2)
        return distance <= self.range
    
    def find_target(self, enemies):
        for enemy in enemies:
            if self.can_attack(enemy):
                return enemy
        return None
    
    def shoot(self, enemy, current_time):
        if current_time - self.last_shot >= self.fire_rate:
            enemy.health -= self.damage
            self.last_shot = current_time
            return True
        return False