import pygame
from os.path import join as path
import math

# Initialize Pygame
pygame.init()

# Setup
screen_size = (600, 700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Bluestroid')
icon = pygame.image.load(path(".", "assets", "icon.png"))
pygame.display.set_icon(icon)

# Load assets
player_image = pygame.image.load(path(".", "assets", "game", "PNG", "playerShip1_blue.png"))
fire_image = pygame.image.load(path(".", "assets", "game", "PNG", "Effects", "fire01.png"))
background_image = pygame.image.load(path(".", "assets", "game", "Backgrounds", "blue.png"))

# Resize background image to fit the screen
background_image = pygame.transform.scale(background_image, screen_size)

# Set up player
player_rect = player_image.get_rect(center=(400, 300))

# Physics variables
gravity = 0.01
friction = 0.99
thrust = 0.5
velocity = pygame.Vector2(0, 0)

# Turning parameters
angle = 0
turn_speed = 5  # Speed of rotation
rotation_speed = 5  # Rotation speed for smooth turning

def rotate_image(image, angle):
    """Rotate the image while keeping its center and size."""
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=player_rect.center)
    return rotated_image, rotated_rect

def draw_fire_effect(surface, image, positions):
    """Draw fire effects at the specified positions."""
    for pos in positions:
        fire_rect = image.get_rect(center=pos)
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
        angle += rotation_speed
        velocity.x -= thrust
    if keys[pygame.K_RIGHT]:
        angle -= rotation_speed
        velocity.x += thrust
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        velocity.y -= thrust
    if keys[pygame.K_DOWN]:
        velocity.y += thrust
    if keys[pygame.K_a]:
        velocity.x -= thrust
    if keys[pygame.K_s]:
        velocity.y += thrust
    if keys[pygame.K_d]:
        velocity.x += thrust

    # Apply gravity
    velocity.y += gravity

    # Apply friction
    velocity *= friction

    # Update player position
    player_rect.x += int(velocity.x)
    player_rect.y += int(velocity.y)

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

    # Determine fire effect positions
    fire_positions = []
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        fire_positions.append((player_rect.centerx, player_rect.bottom))
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        fire_positions.append((player_rect.centerx, player_rect.bottom + 10))

    # Draw fire effects
    draw_fire_effect(screen, fire_image, fire_positions)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
