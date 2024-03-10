import pygame

import settings
import ship
import game_function as gf

def run_game():
    pygame.init()
    setting = settings.Settings()
    screen = pygame.display.set_mode(setting.getSize())
    pygame.display.set_caption("Alien Invasion")

    shipObject = ship.Ship(screen)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()

    gf.create_fleet(setting,screen, aliens)

    while True:
        gf.check_events(shipObject,bullets,setting,screen)
        shipObject.update()
        gf.update_bullets_screen(bullets)
        gf.update_screen(setting,screen,shipObject,bullets,aliens)

run_game()