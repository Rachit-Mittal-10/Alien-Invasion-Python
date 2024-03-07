import pygame

class Ship():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("./Images/ship.png")
        self.image = pygame.transform.scale(self.image,(50,50))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_left = False
        self.moving_right = False

        self.ship_speed = 1.25

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_left and self.rect.x > 0: 
            self.rect.centerx -= self.ship_speed
        if self.moving_right and self.rect.x < 1449:
            self.rect.centerx += self.ship_speed