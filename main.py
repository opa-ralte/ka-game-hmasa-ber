import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

random = pygame.font.Font(filename="random.txt")

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("cornflowerblue")

    # I wanna draw a line
    pygame.draw.line(screen, (200, 0, 0), (100, 100), (500, 500), 50)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()