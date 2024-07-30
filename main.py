import pygame
from os.path import join 

pygame.init()
clock = pygame.time.Clock
icon = join(".", "assets", "icon.png")
pygame.display.set_caption('Bluestroid')
pygame.display.set_icon(icon)