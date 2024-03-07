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

    while True:
        gf.check_events(shipObject)
        shipObject.update()
        gf.update_screen(setting,screen,shipObject)

run_game()