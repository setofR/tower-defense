import pygame
import math

class Game:
    def __init__(self):
        self.grid_size = 40
        self.cols = 20
        self.rows = 20
        self.path = []
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.setup_path()
        
    def setup_path(self):
        # Simple L-shaped path
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
        return self.grid[y][x] == 0