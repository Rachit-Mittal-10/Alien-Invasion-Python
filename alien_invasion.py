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

    while True:
        gf.check_events(shipObject,bullets,setting,screen)
        shipObject.update()
        bullets.update()
        gf.delete_bullets(bullets)
        gf.update_screen(setting,screen,shipObject,bullets)

run_game()