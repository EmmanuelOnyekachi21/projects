#!/usr/bin/python3
"""This is the main game file where the game would run from"""


import pygame


import sys
from time import sleep


from settings import Settings
from ship import Ship
from bullets import Bullet
from alien import Alien
from game_stats import Gamestats

class AlienInvasion():
    """Main class for the Alien Invasion game."""
    def __init__(self):
        """Initializes the game."""
        pygame.init()

        # Call and assign the Settings class
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        # Call and assign the Ship class
        self.bullets = pygame.sprite.Group()
        self.ship = Ship(self)
        self.alien = pygame.sprite.Group()
        self._create_fleets()
        self.stats = Gamestats(self)
        self.game_active = True



    def run_game(self):
        """Run the main game loop."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.alien.empty()

            # Create a new fleet and center the ship.
            self._create_fleets()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.alien.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _check_events(self):
        """Manages events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responds to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # get rid of the bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Resond to bullet-alien collision."""
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.alien, True, True)

        if not self.alien:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then updates positions."""
        self._check_fleet_edges()
        self.alien.update()

        if pygame.sprite.spritecollideany(self.ship, self.alien):
            self._ship_hit()

        self._check_aliens_bottom()

    def _create_fleets(self):
        """Create the fleets of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.alien.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.alien.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.alien.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):
        """Updates the contents of the screen and redraw everything."""
        self.screen.fill((self.settings.color))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.alien.draw(self.screen)
        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai_game = AlienInvasion()
    ai_game.run_game()

