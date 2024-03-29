import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A Class to represent the Alie"""
    def __init__(self,settings,screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load("./Images/alien.png")
        self.image = pygame.transform.scale(self.image,(35,35))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at the current location"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if the alien is at edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False
        
    