class Settings():
    """ A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initialise game settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (192, 192, 192)

        # ship settings
        self.ship_speed_factor = 2.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3


