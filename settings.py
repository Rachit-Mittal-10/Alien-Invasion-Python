class Settings():
    """Class to store settings of multiple components"""
    def __init__(self):
       
        # Screen Settings
        self.bg_color = (230,230,230)
        self.width = 1500
        self.height = 900
        
        #Bullet Settings
        self.bullet_speed_factor = 5
        self.bullet_width = 1000
        self.bullet_height = 20
        self.bullet_color = (60,60,60)
        
        # Alien Settings
        self.alien_speed_factor = 0.9
        self.fleet_drop_speed = 10
        self.fleet_direction  = 1

    def getSize(self):
        return (self.width,self.height)