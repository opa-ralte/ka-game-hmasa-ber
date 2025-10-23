import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

font = pygame.font.Font(None, 64)
text_surf = font.render("Hello, yeahh!!", True, (255, 255, 255))
text_rect = text_surf.get_rect(center=(640, 260))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("cornflowerblue")


    screen.blit(text_surf, text_rect)
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()