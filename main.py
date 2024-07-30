import pygame
from os.path import join as path, join

pygame.init()
running = True
clock = pygame.time.Clock()
icon = pygame.image.load(join(".", "assets", "icon.png"))
screen_size = 600, 700
player = pygame.image.load(path(".", "assets", "game", "PNG", "playerShip1_blue.png"))
player_rect = player.get_rect(center=(400, 300))
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption('Bluestroid')
pygame.display.set_icon(icon)
pygame.display.set_mode(screen_size)
screen.blit(player, player_rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
