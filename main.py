import pygame
import os

pygame.init()

ORIGINAL_RES = (480, 480)

screen = pygame.display.set_mode(ORIGINAL_RES, pygame.SCALED)
clock = pygame.time.Clock()
running = True
dt = 0

font = pygame.font.Font(os.path.join("assets", "fonts", "GohuFont14NerdFont-Regular.ttf"), 30)
title_surf = font.render("chawngkawr game yeahhh!!!", True, (255,215,0))
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
    def __init__(self, which_player, screen, color, x, y, dt):
        self.which_player = which_player
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.dt = dt

    def update(self):
        keys = pygame.key.get_just_pressed()
        match self.which_player:
            case 1:
                if keys[pygame.K_w]:
                    self.y-=TILE_SIZE/2 + self.dt
                elif keys[pygame.K_s]:
                    self.y+=TILE_SIZE/2 + self.dt  
                elif keys[pygame.K_a]:
                    self.x-=TILE_SIZE/2 + self.dt      
                elif keys[pygame.K_d]:
                    self.x+=TILE_SIZE/2 + self.dt
            case 2:
                if keys[pygame.K_i]:
                    self.y-=TILE_SIZE/2 + self.dt
                elif keys[pygame.K_k]:
                    self.y+=TILE_SIZE/2 + self.dt  
                elif keys[pygame.K_j]:
                    self.x-=TILE_SIZE/2 + self.dt     
                elif keys[pygame.K_l]:
                    self.x+=TILE_SIZE/2 + self.dt
                
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 20)

grid = Grid(COLS, ROWS, TILE_SIZE)

ball1 = Ball(1, screen, (100, 0, 0), 100, 100, dt)
ball2 = Ball(2, screen, (0, 0, 100), 300, 300, dt)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.fill("cornflowerblue")
    grid.draw(screen)
    screen.blit(title_surf, title_rect)
       
    ball1.update()
    ball2.update()

    ball1.draw()
    ball2.draw()
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

