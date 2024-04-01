#!/usr/bin/python3


"""Documents"""

import pygame
import sys

from settings import Settings
from jet import Jet

class BlueSky:
    """Document"""
    def __init__(self):
        """Document"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.set_height, self.settings.set_width))
        pygame.display.set_caption("Blue Sky")
        
        self.jet = Jet(self)
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_event()
            self.jet.update()
            self._update_screen()
            

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # Check for a keydown event
        if event.key == pygame.K_RIGHT:
            self.jet.moving_right = True

        if event.key == pygame.K_LEFT:
            self.jet.moving_left = True

        if event.key == pygame.K_UP:
            self.jet.moving_up = True
        if event.key == pygame.K_DOWN:
            self.jet.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.jet.moving_right = False

        if event.key == pygame.K_LEFT:
            self.jet.moving_left = False

        if event.key == pygame.K_UP:
            self.jet.moving_up = False

        if event.key == pygame.K_DOWN:
            self.jet.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.jet.blitme()

        pygame.display.flip()

if __name__ == "__main__":
    ai = BlueSky()
    ai.run_game()


