import pygame
from os.path import join as path

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

# Hover effect parameters
hover_effect_intensity = 15
angle = 0

def rotate_image(image, angle):
    """Rotate the image while keeping its center and size."""
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image.get_rect(center=(player_rect.x, player_rect.y)).center)
    return rotated_image, rotated_rect

def draw_glow(surface, image, position, glow_color=(255, 255, 0)):
    """Draw a glow effect around the image."""
    glow_surface = pygame.Surface((image.get_width() + hover_effect_intensity * 2, image.get_height() + hover_effect_intensity * 2), pygame.SRCALPHA)
    pygame.draw.ellipse(glow_surface, glow_color + (128,), glow_surface.get_rect(), width=0)
    glow_surface.blit(image, (hover_effect_intensity, hover_effect_intensity), special_flags=pygame.BLEND_RGBA_ADD)
    surface.blit(glow_surface, (position[0] - hover_effect_intensity, position[1] - hover_effect_intensity))

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
        velocity.x -= thrust
        angle += 10  # Faster rotation
    if keys[pygame.K_RIGHT]:
        velocity.x += thrust
        angle -= 10  # Faster rotation
    if keys[pygame.K_UP]:
        velocity.y -= thrust
    if keys[pygame.K_DOWN]:
        velocity.y += thrust
    if keys[pygame.K_w]:
        velocity.y -= thrust
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

    # Clear screen
    screen.blit(background_image, (0, 0))  # Draw background image

    # Rotate and draw player
    rotated_image, rotated_rect = rotate_image(player_image, angle)
    screen.blit(rotated_image, rotated_rect.topleft)

    # Draw fire effect
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        fire_rect = fire_image.get_rect(midbottom=(player_rect.centerx, player_rect.top))
        screen.blit(fire_image, fire_rect.topleft)
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        fire_rect = fire_image.get_rect(midbottom=(player_rect.centerx, player_rect.bottom))
        screen.blit(fire_image, fire_rect.topleft)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
