
class Settings():
    ''' Stores all settings for Galactic War '''

    def __init__(self):
        ''' Init the game's settings '''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed_factor = 5

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 3
