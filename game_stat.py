class Game_Stat():
    """Track Statistics for Alien Invasion."""
    def __init__(self,settings):
        """Initialise Statistics."""
        self.game_active = False
        self.settings = settings
        self.reset_stats()

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
