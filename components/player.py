import pygame
from os.path import join as path

class Player:
    def __init__(self, screen):
        # Initialize player properties
        self.screen = screen
        self.image = pygame.image.load(path(".", "assets", "game", "PNG", "playerShip1_blue.png"))
        self.rect = self.image.get_rect(center=(400, 300))
        self.velocity = pygame.Vector2(0, 0)
        self.gravity = 0.1
        self.friction = 0.99
        self.thrust = 0.5

    def update(self):
        # Key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x -= self.thrust
        if keys[pygame.K_RIGHT]:
            self.velocity.x += self.thrust
        if keys[pygame.K_UP]:
            self.velocity.y -= self.thrust
        if keys[pygame.K_DOWN]:
            self.velocity.y += self.thrust

        # Apply gravity
        self.velocity.y += self.gravity

        # Apply friction
        self.velocity *= self.friction

        # Update player position
        self.rect.x += int(self.velocity.x)
        self.rect.y += int(self.velocity.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)
