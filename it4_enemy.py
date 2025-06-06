import pygame

class Enemy:    
    def __init__(self, path):
        self.path = path
        self.path_index = 0
        self.x = path[0][0]
        self.y = path[0][1]
        self.health = 100
        self.max_health = 100
        self.speed = 2
        self.reward = 20
        self.damage = 10
        self.size = 15
        
        # Load and scale enemy image
        self.image = pygame.image.load("assets/images/enemies/angry_enemy.png")
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
        # Draw image centered on enemy position
        screen.blit(self.image, (self.x - self.size, self.y - self.size))
        
        # Health bar
        bar_width = 30
        bar_height = 5
        bar_x = self.x - bar_width // 2
        bar_y = self.y - self.size - 10
        
        # Background (red)
        pygame.draw.rect(screen, "red", (bar_x, bar_y, bar_width, bar_height))
        # Health (green)
        health_percentage = self.health / self.max_health
        pygame.draw.rect(screen, "green", (bar_x, bar_y, bar_width * health_percentage, bar_height))
        # Border
        pygame.draw.rect(screen, "black", (bar_x, bar_y, bar_width, bar_height), 1)
    
    def is_alive(self):
        return self.health > 0
    
    def reached_end(self):
        return self.path_index >= len(self.path) - 1