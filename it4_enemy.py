import pygame

class Enemy:    
    def __init__(self, path):
        self.path = path
        self.path_index = 0
        self.x = path[0][0]
        self.y = path[0][1]
        self.health = 100
        self.max_health = 100
        self.speed = 5
        self.reward = 20
        self.damage = 10
        self.size = 20
        self.image = pygame.image.load("assets/images/enemies/angry_enemy_v2.png")
        self.image = pygame.transform.scale(self.image, (self.size * 2, self.size * 2))
        
    def move(self):
        if self.path_index < len(self.path) - 1:
            target_x, target_y = self.path[self.path_index + 1]
            
            dx = target_x - self.x
            dy = target_y - self.y
            distance = (dx**2 + dy**2)**0.5
            
            if distance < self.speed:
                self.path_index += 1
                if self.path_index < len(self.path):
                    self.x, self.y = self.path[self.path_index]
            else:
                self.x += (dx / distance) * self.speed
                self.y += (dy / distance) * self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x - self.size, self.y - self.size))
    
    def is_alive(self):
        return self.health > 0
    
    def reached_end(self):
        return self.path_index >= len(self.path) - 1