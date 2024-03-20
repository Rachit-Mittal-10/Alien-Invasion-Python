class Settings():
    """Class to store settings of multiple components"""
    def __init__(self):
        """Initialise the statis settings for game."""
        # Screen Settings
        self.bg_color = (230,230,230)
        self.width = 1500
        self.height = 900
        
        #Bullet Settings
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = (60,60,60)
        
        # Alien Settings
        self.fleet_drop_speed = 5

        #Ship Setting
        self.ship_limit = 3

        # How Quickly game speeds up
        self.speed_up_scale = 1.2
        self.speed_down_scale = 0.8
        self.initialise_dynamic_settings()

    def getSize(self):
        return (self.width,self.height)
    
    def initialise_dynamic_settings(self):
        """Initialise the settings that change throughout the game."""
        self.ship_speed = 1.25
        self.bullet_speed_factor = 7
        self.alien_speed_factor = 0.8
        self.fleet_direction  = 1
    
    def increase_speed(self):
        """Increase Speed Settings."""
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale

    def decrease_speed(self):
        """Decrease Speed Settings."""
        self.ship_speed *= self.speed_down_scale
        self.alien_speed_factor *= self.speed_down_scale
        self.bullet_speed_factor *= self.speed_down_scale