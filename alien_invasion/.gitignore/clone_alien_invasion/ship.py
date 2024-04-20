""" This is the ship module."""
import pygame


class Ship:
    """This houses the ship and its positioning."""
    def __init__(self, ai_game):
        """Initializes the ship with resources from ai_game."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        self.ship = pygame.image.load('images/ship.png')
        self.rect = self.ship.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 80

        # Store a float for the ship's exact horizontal position."""
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left >= self.screen_rect.left: 
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 80
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draws the ship to the screen"""
        self.screen.blit(self.ship, self.rect)
