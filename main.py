import pygame
import os

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

file_path = os.path.join(os.path.dirname(__file__), "random.txt")
try:
    with open(file_path, "r", encoding="utf-8") as f:
        file_text = f.read()
except Exception as e:
    file_text = f"Error reading {file_path}:\n{e}"

font = pygame.font.Font(None, 48)

lines = file_text.splitlines() or [""]
render_surfaces = [font.render(line, True, (255, 255, 255)) for line in lines]

padding_x = 40
padding_y = 40
line_spacing = 6

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("cornflowerblue")


    y = padding_y
    for surf in render_surfaces:
        screen.blit(surf, (padding_x, y))
        y += surf.get_height() + line_spacing
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()