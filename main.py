import pygame
import os

pygame.init()

ORIGINAL_RES = (560, 560)
font_path = os.path.join("assets", "fonts", "GohuFont14NerdFont-Regular.ttf")
pygame.display.set_caption("chawngkawr game a ni hrih...")
screen = pygame.display.set_mode(ORIGINAL_RES, pygame.SCALED)
clock = pygame.time.Clock()
running = True
dt = 0

font = pygame.font.Font(font_path, 30)
title_surf = font.render("", True, (255,215,0))
title_rect = title_surf.get_frect(center=(ORIGINAL_RES[0]//2, 30))

TILE_SIZE = 40
COLS = ORIGINAL_RES[0] // TILE_SIZE
ROWS = ORIGINAL_RES[1] // TILE_SIZE

PATTERN =    ("00000000000000"
              "01111101111110"
              "01101111110110"
              "01111110111110"
              "01111111011110"
              "01101111011110"
              "01101011111110"
              "01011111110110"
              "01111101111110"
              "01011111101110"
              "01111111111100"
              "01110111101110"
              "01111111110110"
              "00000000000000")

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
    def __init__(self, which_player, screen, color, x, y, dt, box, image_path=None):
        self.which_player = which_player
        self.screen = screen
        self.color = color
        self.dt = dt
        self.travel = TILE_SIZE
        self.box = box

        # load image or create a colored surface
        if image_path and os.path.exists(image_path):
            self.image = pygame.image.load(image_path).convert_alpha()
            # scale to tile size if needed
            self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        else:
            # create a colored rect as fallback
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
            self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

    def can_move_to(self, new_x, new_y):
        # check if the ball can move to the new position
        grid_x = new_x // TILE_SIZE
        grid_y = new_y // TILE_SIZE
        return not self.box.is_wall(grid_x, grid_y)

    def update(self):
        keys = pygame.key.get_just_pressed()
        new_x, new_y = self.rect.centerx, self.rect.centery
        match self.which_player:
            case 1:
                if keys[pygame.K_w]:
                    new_y -= self.travel
                elif keys[pygame.K_s]:
                    new_y += self.travel
                elif keys[pygame.K_a]:
                    new_x -= self.travel
                elif keys[pygame.K_d]:
                    new_x += self.travel
            case 2:
                if keys[pygame.K_i]:
                    new_y -= self.travel
                elif keys[pygame.K_k]:
                    new_y += self.travel
                elif keys[pygame.K_j]:
                    new_x -= self.travel
                elif keys[pygame.K_l]:
                    new_x += self.travel
        # only move if the new position is valid
        if new_x != self.rect.centerx or new_y != self.rect.centery:
            if self.can_move_to(new_x, new_y):
                self.rect.centerx = new_x
                self.rect.centery = new_y
    def draw(self):
        self.screen.blit(self.image, self.rect)
class Box():
    def __init__(self, pattern, screen, x, y, dt):
        self.pattern = pattern
        self.screen = screen
        self.x = x
        self.y = y
        self.dt = dt
        self.width = 14
        self.height = len(pattern) // self.width
    
    def is_wall(self, grid_x, grid_y):
        """Check if a grid position contains a wall"""
        if grid_x < 0 or grid_x >= self.width or grid_y < 0 or grid_y >= self.height:
            return True
        index = grid_y * self.width + grid_x
        return self.pattern[index] == '0'
    
    def draw(self):
        for i, char in enumerate(self.pattern):
            if char == '1':
                col = i % self.width
                row = i // self.width

                px = self.x + col * TILE_SIZE
                py = self.y + row * TILE_SIZE

                pygame.draw.rect(self.screen, (255, 182, 193), (px, py, TILE_SIZE, TILE_SIZE))


grid = Grid(COLS, ROWS, TILE_SIZE)
box = Box(PATTERN, screen, 0, 0, dt)

player1_png = os.path.join("assets", "images", "player1.png")
player2_png = os.path.join("assets", "images", "player2.png")

ball1 = Ball(1, screen, (4, 57, 21), 100, 100, dt, box, player1_png)
ball2 = Ball(2, screen, (255, 157, 0), 300, 300, dt, box, player2_png)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    ball1.update()
    ball2.update()
    screen.fill("cornflowerblue")


       

    grid.draw(screen)
    box.draw()
    screen.blit(title_surf, title_rect)
    ball1.draw()
    ball2.draw()
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

