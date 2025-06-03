import pygame
from it4_enemy import Enemy

class Game:
    def __init__(self):
        self.grid_size = 40
        self.cols = 18
        self.rows = 18
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.path = []
        self.enemies = []
        self.base_health = 100
        self.currency = 100
        self.setup_path()
        
    def setup_path(self):
        path_tiles = [
            (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9),
            (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15),
            (9, 15), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (16, 15), (17, 15)
        ]
        
        for x, y in path_tiles:
            self.grid[y][x] = 1
            self.path.append((x * self.grid_size + self.grid_size // 2, 
                            y * self.grid_size + self.grid_size // 2))
    
    def get_grid_pos(self, mouse_pos):
        x = mouse_pos[0] // self.grid_size
        y = mouse_pos[1] // self.grid_size
        if 0 <= x < self.cols and 0 <= y < self.rows:
            return (x, y)
        return None
    
    def can_place_tower(self, grid_pos):
        if grid_pos is None:
            return False
        x, y = grid_pos
        return self.grid[y][x] == 0
    
    def spawn_enemy(self):
        enemy = Enemy(self.path)
        self.enemies.append(enemy)
    
    def update(self):
        for enemy in self.enemies[:]:
            enemy.move()
            
            if enemy.reached_end():
                self.base_health -= enemy.damage
                self.enemies.remove(enemy)
            elif not enemy.is_alive():
                self.currency += enemy.reward
                self.enemies.remove(enemy)
    
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.grid_size
                y = row * self.grid_size
                
                if self.grid[row][col] == 1:
                    color = "sandybrown"
                else:
                    color = "forestgreen"
                
                pygame.draw.rect(screen, color, (x, y, self.grid_size, self.grid_size))
                pygame.draw.rect(screen, "black", (x, y, self.grid_size, self.grid_size), 1)
        
        base_x, base_y = self.path[-1]
        pygame.draw.rect(screen, "blue", (base_x - 20, base_y - 20, 40, 40))
        
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def draw_ui(self, screen, font):
        currency_text = font.render(f"Gold: ${self.currency}", True, "gold")
        screen.blit(currency_text, (10, 10))
        
        health_text = font.render(f"Base Health: {self.base_health}", True, "white")
        screen.blit(health_text, (10, 40))
        
        if self.base_health <= 0:
            game_over_text = font.render("GAME OVER", True, "red")
            text_rect = game_over_text.get_rect(center=(400, 400))
            screen.blit(game_over_text, text_rect)