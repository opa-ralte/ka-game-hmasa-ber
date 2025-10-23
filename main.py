import pygame
import os

pygame.init()

ORIGINAL_RES = (1280, 720)

screen = pygame.display.set_mode(ORIGINAL_RES)
clock = pygame.time.Clock()
running = True
dt = 0

font = pygame.font.Font(None, 50)
title_surf = font.render("tilte", True, (200, 50, 225))
title_rect = title_surf.get_frect(center=(500, 500))

class Entity(pygame.sprite.Sprite):
    def __init__(self, type, name, position, direction, speed):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.name = name
        self.position = position
        self.direction = direction
        self.speed = speed

    def update():
        pass



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("cornflowerblue")

    screen.blit(title_surf, title_rect)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()