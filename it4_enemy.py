import pygame

class Enemy:    
    def __init__(self, path):
        self.path = path
        self.path_index = 0
        self.x = path[0][0]
        self.y = path[0][1]
        self.health = 100
        self.max_health = 100
        self.speed = 1
        self.reward = 10
        self.damage = 10
        self.size = 20
        self.image = pygame.image.load("assets/images/enemies/bad_enemy.png")
        self.image = pygame.transform.scale(self.image, (self.size * 2, self.size * 2))
        
    def move(self):
        if self.path_index < len(self.path) - 1:
            target_x, target_y = self.path[self.path_index + 1]
            
            dx = target_x - self.x
            dy = target_y - self.y
            
            if abs(dx) < self.speed and abs(dy) < self.speed:
                self.path_index += 1
            else:
                if dx != 0:
                    self.x += self.speed if dx > 0 else -self.speed
                if dy != 0:
                    self.y += self.speed if dy > 0 else -self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x - self.size, self.y - self.size))  
    
    def is_alive(self):
        return self.health > 0
    
    def reached_end(self):
        return self.path_index >= len(self.path) - 1