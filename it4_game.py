import pygame
from it4_tower import Tower

class Game:
    def __init__(self):
        self.grid_size = 40
        self.cols = 20
        self.rows = 20
        self.path = []
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.towers = []
        self.currency = 200
        self.selected_tower = None
        self.setup_path()
        
    def setup_path(self):
        path_coords = [
            (0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10),
            (6, 10), (7, 10), (8, 10), (9, 10), (10, 10),
            (10, 11), (10, 12), (10, 13), (10, 14), (10, 15),
            (11, 15), (12, 15), (13, 15), (14, 15), (15, 15),
            (16, 15), (17, 15), (18, 15), (19, 15)
        ]
        
        for x, y in path_coords:
            self.grid[y][x] = 1
            self.path.append((x * self.grid_size, y * self.grid_size))
    
    def draw_grid(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.grid_size
                y = row * self.grid_size
                
                if self.grid[row][col] == 1:
                    pygame.draw.rect(screen, "tan", (x, y, self.grid_size, self.grid_size))
                else:
                    pygame.draw.rect(screen, "darkgreen", (x, y, self.grid_size, self.grid_size))
                
                pygame.draw.rect(screen, "black", (x, y, self.grid_size, self.grid_size), 1)
    
    def get_grid_pos(self, mouse_pos):
        x = mouse_pos[0] // self.grid_size
        y = mouse_pos[1] // self.grid_size
        return (x, y) if 0 <= x < self.cols and 0 <= y < self.rows else None
    
    def can_place_tower(self, grid_pos):
        if grid_pos is None:
            return False
        x, y = grid_pos
        if self.grid[y][x] != 0:
            return False
        for tower in self.towers:
            if tower.x == x * self.grid_size and tower.y == y * self.grid_size:
                return False
        return True
    
    def place_tower(self, grid_pos):
        if self.can_place_tower(grid_pos) and self.currency >= 50:
            x, y = grid_pos
            tower = Tower(x * self.grid_size, y * self.grid_size)
            self.towers.append(tower)
            self.currency -= tower.cost
            return True
        return False
    
    def draw_towers(self, screen):
        for tower in self.towers:
            tower.draw(screen)
            if tower == self.selected_tower:
                tower.draw_range(screen)
    
    def get_tower_at(self, grid_pos):
        if grid_pos is None:
            return None
        x, y = grid_pos
        pixel_x = x * self.grid_size
        pixel_y = y * self.grid_size
        for tower in self.towers:
            if tower.x == pixel_x and tower.y == pixel_y:
                return tower
        return None
    
    def draw_ui(self, screen, font):
        currency_text = font.render(f"Bank: ${self.currency}", True, "white")
        screen.blit(currency_text, (10, 10))