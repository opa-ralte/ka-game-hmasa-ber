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

class Ball():
    def __init__(self, screen, color, x, y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y

    def update(self):
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_w]:
            self.y-=TILE_SIZE/2
        elif keys[pygame.K_s]:
            self.y+=TILE_SIZE/2   
        elif keys[pygame.K_a]:
            self.x-=TILE_SIZE/2       
        elif keys[pygame.K_d]:
            self.x+=TILE_SIZE/2
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 20)

grid = Grid(COLS, ROWS, TILE_SIZE)

ball = Ball(screen, (100, 0, 0), 100, 100)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.fill("cornflowerblue")
    grid.draw(screen)
    screen.blit(title_surf, title_rect)
       
    ball.update()
    ball.draw()
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

