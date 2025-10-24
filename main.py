import pygame
import os

pygame.init()

ORIGINAL_RES = (480, 480)

screen = pygame.display.set_mode(ORIGINAL_RES, pygame.SCALED)
clock = pygame.time.Clock()
running = True
dt = 0

font = pygame.font.Font(None, 50)
title_surf = font.render("chawngkawr game yeahhh!!!", True, (150, 0, 100, 0.6))
title_rect = title_surf.get_frect(center=(ORIGINAL_RES[0]//2, 30))

TILE_SIZE = 40
COLS = ORIGINAL_RES[0] // TILE_SIZE
ROWS = ORIGINAL_RES[1] // TILE_SIZE

class Grid():
    def __init__(self, cols, rows, tile_size):
        self.cols = cols
        self.rows = rows
        self.tile_size = tile_size

    def to_pixel(self, cell):
        x, y = cell
        return x * self.tile_size, y * self.tile_size
    
    def draw(self, surf, color=(50, 50, 50)):
        for x in range(1, self.cols + 1):
            px = x * self.tile_size
            pygame.draw.line(surf, color, (px, 0), (px, self.rows*self.tile_size))
        for y in range(1, self.rows + 1):
            py = y * self.tile_size
            pygame.draw.line(surf, color, (0, py), (self.cols*self.tile_size, py))

grid = Grid(COLS, ROWS, TILE_SIZE)

x, y = ORIGINAL_RES[0]//2, ORIGINAL_RES[1]//2
last_movement = (x, y)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.fill("cornflowerblue")
    grid.draw(screen)
    screen.blit(title_surf, title_rect)

    pygame.draw.circle(screen, (255, 161, 246), (x, y), 20, 0)

    # I want to sustain the last movement
    if last_movement == (0, -1):
        y -= TILE_SIZE
    elif last_movement == (0, 1):
        y += TILE_SIZE
    elif last_movement == (1, 0):
        x += TILE_SIZE
    elif last_movement == (-1, 0):
        x -= TILE_SIZE
    pygame.time.delay(200)

    keys = pygame.key.get_just_pressed()
    if keys[pygame.K_UP]:
        y-=TILE_SIZE
        last_movement = (0, -1)
    elif keys[pygame.K_DOWN]:
        y+=TILE_SIZE
        last_movement = (0, 1)
    elif keys[pygame.K_RIGHT]:
        x+=TILE_SIZE
        last_movement = (1, 0)
    elif keys[pygame.K_LEFT]:
        x-=TILE_SIZE
        last_movement = (-1, 0)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

