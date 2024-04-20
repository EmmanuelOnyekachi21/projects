"""This is the settings module."""

class Settings:
    """A class to hold all configurations of the game."""
    def __init__(self):
        """Initialize the game settings."""
        self.color = (230, 230, 230)
        self.screen_height = 800
        self.screen_width = 1200

        # Ship settings
        self.ship_speed = 2.0
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_height = 15
        self.bullet_width = 300
        self.bullet_speed = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 10
        self.fleet_drop_speed = 50
        
        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
