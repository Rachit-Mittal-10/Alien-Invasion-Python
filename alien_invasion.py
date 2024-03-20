import pygame

import settings
import ship
import game_function as gf
import button
import game_stat as gs

def run_game():
    pygame.init()
    setting = settings.Settings()
    screen = pygame.display.set_mode(setting.getSize())
    pygame.display.set_caption("Alien Invasion")
    
    play_button = button.Button(setting,screen,"Play")
    shipObject = ship.Ship(screen,setting)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    stat = gs.Game_Stat(setting) 

    gf.create_fleet(setting,screen, aliens,shipObject)

    while True:
        gf.check_events(shipObject,bullets,setting,screen,aliens,stat,play_button)
        if stat.game_active:
            shipObject.update()
            gf.update_bullets_screen(bullets,aliens,setting,screen,shipObject)
            gf.update_aliens(setting,aliens,shipObject,screen,stat,bullets)
        gf.update_screen(setting,screen,shipObject,bullets,aliens,stat,play_button)

run_game()