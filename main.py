import pygame
import os

pygame.init()

ORIGINAL_RES = (720, 720)

screen = pygame.display.set_mode(ORIGINAL_RES)
clock = pygame.time.Clock()
running = True
dt = 0

font = pygame.font.Font(None, 50)
title_surf = font.render("tilte", True, (0, 0, 0))
title_rect = title_surf.get_frect(center=(360, 40))

TILE_SIZE = 40
COLS = ORIGINAL_RES[0] // TILE_SIZE
ROWS = ORIGINAL_RES[1] // TILE_SIZE

class Grid:
    def __init__(self, cols, rows, tile_size):
        self.cols = cols
        self.rows = rows
        self.tile_size = tile_size

    def to_pixel(self, cell):
        x, y = cell
        return x * self.tile_size, y * self.tile_size
    
    def draw(self, surf, color=(50, 50, 50)):
        for x in range(self.cols + 1):
            px = x * self.tile_size
            pygame.draw.line(surf, color, (px, 0), (px, self.rows*self.tile_size))
        for y in range(self.rows + 1):
            py = y * self.tile_size
            pygame.draw.line(surf, color, (0, py), (self.cols*self.tile_size, py))

grid = Grid(COLS, ROWS, TILE_SIZE)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("cornflowerblue")

    grid.draw(screen)

    screen.blit(title_surf, title_rect)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()