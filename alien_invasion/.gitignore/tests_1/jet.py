"""Document"""
import pygame

class Jet:
    """Documents"""
    def __init__(self, ai):
        """Documents"""

        # Get Screen rect
        self.screen = ai.screen
        self.settings = ai.settings
        self.screen_rect = ai.screen.get_rect()

        self.jet_image = pygame.image.load("images/download.png")
        self.jet_image_rect = self.jet_image.get_rect()

        self.jet_image_rect.midbottom = self.screen_rect.midbottom
        self.jet_image_rect.y -= 50

        # To make jet move right
        self.moving_right = False

        # To make jet move left
        self.moving_left = False

        # To make jet move up
        self.moving_up = False

        # To make jet move down
        self.moving_down = False

        self.x = float(self.jet_image_rect.x)
        self.y = float(self.jet_image_rect.y)

    def update(self):
        if self.moving_right and self.jet_image_rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.jet_image_rect.left > 0:
           self.x -= self.settings.ship_speed

        if self.moving_up and self.jet_image_rect.top > 0:
            self.y -= self.settings.ship_speed

        if self.moving_down and self.jet_image_rect.bottom + 50 < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.jet_image_rect.x = self.x
        self.jet_image_rect.y = self.y
    def blitme(self):
        """Document"""
        self.screen.blit(self.jet_image, self.jet_image_rect)
        
