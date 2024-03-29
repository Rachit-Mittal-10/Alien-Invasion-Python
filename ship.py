import pygame

class Ship():
    def __init__(self,screen,settings):
        self.screen = screen
        self.image = pygame.image.load("./Images/ship.png")
        self.image = pygame.transform.scale(self.image,(50,50))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.moving_left = False
        self.moving_right = False

        self.settings = settings

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_left and self.rect.left > 0: 
            self.center -= self.settings.ship_speed
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed    
        
        self.rect.centerx = self.center

    def center_ship(self):
        """Centers the ship.."""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
