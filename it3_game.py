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
        path_coords = [
            (0, 2),
            (1, 2),
            (2, 2),
            (3, 2),
            (4, 2),
            (4, 3),
            (4, 4),
            (4, 5),
            (4, 6),
            (4, 7),
            (4, 8),
            (5, 8),
            (6, 8),
            (7, 8),
            (8, 8),
            (9, 8),
            (9, 7),
            (9, 6),
            (9, 5),
            (9, 4),
            (9, 3),
            (9, 2),
            (10, 2),
            (11, 2),
            (12, 2),
            (13, 2),
            (14, 2),
            (14, 3),
            (14, 4),
            (14, 5),
            (14, 6),
            (14, 7),
            (14, 8),
            (14, 9),
            (14, 10),
            (14, 11),
            (14, 12),
            (13, 12),
            (12, 12),
            (11, 12),
            (10, 12),
            (9, 12),
            (8, 12),
            (7, 12),
            (6, 12),
            (5, 12),
            (4, 12),
            (4, 13),
            (4, 14),
            (4, 15),
            (4, 16),
            (5, 16),
            (6, 16),
            (7, 16),
            (8, 16),
            (9, 16),
            (10, 16),
            (11, 16),
            (12, 16),
            (13, 16),
            (14, 16),
            (15, 16),
            (16, 16),
            (17, 16),
            (18, 16),
            (19, 16),
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
                    pygame.draw.rect(
                        screen, "white", (x, y, self.grid_size, self.grid_size)
                    )
                else:
                    pygame.draw.rect(
                        screen, "brown", (x, y, self.grid_size, self.grid_size)
                    )

                pygame.draw.rect(
                    screen, "black", (x, y, self.grid_size, self.grid_size), 1
                )

    def get_grid_pos(self, mouse_pos):
        x = mouse_pos[0] // self.grid_size
        y = mouse_pos[1] // self.grid_size
        return (x, y) if 0 <= x < self.cols and 0 <= y < self.rows else None

    def can_place_tower(self, grid_pos):
        if grid_pos is None:
            return False
        x, y = grid_pos
        return self.grid[y][x] == 0
