import pygame
from os.path import join as path

pygame.init()
clock = pygame.time.Clock()
icon = path(".", "assets", "icon.png")
running = True

pygame.display.set_caption('Bluestroid')
pygame.display.set_icon(icon)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
