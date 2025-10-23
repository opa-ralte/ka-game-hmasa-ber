import pygame
import os

pygame.init()

ORIGINAL_RES = (1280, 720)

screen = pygame.display.set_mode(ORIGINAL_RES)
clock = pygame.time.Clock()
running = True



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("cornflowerblue")

    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()