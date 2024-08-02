import pygame
import math
from os.path import join as path
from components.debug import *

# Initialize Pygame & Font
pygame.init()
pygame.font.init()

# Setup
screen_size = (600, 700)
title = 'Bluestroid'
debugMode = True
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(title)
icon = pygame.image.load(path(".", "assets", "icon.png"))
pygame.display.set_icon(icon)

# Load assets
player_image = pygame.image.load(path(".", "assets", "game", "PNG", "playerShip1_blue.png"))
fire_image = pygame.image.load(path(".", "assets", "game", "PNG", "Effects", "fire01.png"))
background_image = pygame.image.load(path(".", "assets", "game", "Backgrounds", "blue.png"))
enemy_image = pygame.image.load(path(".", "assets", "game", "PNG", "playerShip2_red.png"))

print(f"{title} ☄️")
print("-----------------------------------------\n")

# Debug If Loop
if debugMode:
    print(f"{title} Debug Mode has been Activated ☄️\n")
    print(f"SDL Version is {sdl}")
    print(f"SDL Font Loader Version is {sdlfont}")
    print(f"Font is {font}")

# Resize background image to fit the screen
background_image = pygame.transform.scale(background_image, screen_size)

# Set up player
player_rect = player_image.get_rect(center=(300, 350))  # Adjusted to be within the screen boundaries

# Physics variables
gravity = 0.01
friction = 0.99
thrust = 0.1
velocity = pygame.Vector2(0, 0)

# Turning parameters
angle = 0
turn_speed = 5  # Speed of rotation

def rotate_image(image, angle):
    """Rotate the image while keeping its center and size."""
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=player_rect.center)
    return rotated_image, rotated_rect

def draw_fire_effect(surface, image, position, angle):
    """Draw fire effects at the specified positions."""
    rad_angle = math.radians(angle)
    offset = pygame.Vector2(0, 40).rotate(angle)  # Adjust offset for fire position to bottom of the ship
    fire_pos = position - offset
    fire_rect = image.get_rect(center=fire_pos)
    surface.blit(image, fire_rect.topleft)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle += turn_speed
    if keys[pygame.K_RIGHT]:
        angle -= turn_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        rad_angle = math.radians(angle)
        force = pygame.Vector2(math.cos(rad_angle) * thrust, math.sin(rad_angle) * thrust)
        velocity -= force
    if keys[pygame.K_DOWN]:
        rad_angle = math.radians(angle)
        force = pygame.Vector2(-math.cos(rad_angle) * thrust, -math.sin(rad_angle) * thrust)
        velocity += force

    # Apply gravity
    velocity.y += gravity

    # Apply friction
    velocity *= friction

    # Update player position
    player_rect.centerx += int(velocity.x)
    player_rect.centery += int(velocity.y)

    # Keep the player within the screen boundaries
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > screen_size[0]:
        player_rect.right = screen_size[0]
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > screen_size[1]:
        player_rect.bottom = screen_size[1]

    # Clear screen
    screen.blit(background_image, (0, 0))  # Draw background image

    # Rotate and draw player
    rotated_image, rotated_rect = rotate_image(player_image, angle)
    screen.blit(rotated_image, rotated_rect.topleft)

    # Draw fire effects
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        draw_fire_effect(screen, fire_image, rotated_rect.center, angle)

    # Draw enemies (example using the enemy_image from sample.png)
    enemy_rect = enemy_image.get_rect(center=(300, 100))
    screen.blit(enemy_image, enemy_rect.topleft)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
