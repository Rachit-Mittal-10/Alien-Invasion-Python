import sys
import pygame

def check_events(shipObject):
    """Respond to Mouse and Keyboard Events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                shipObject.moving_right = True
            elif event.key == pygame.K_LEFT:
                shipObject.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                shipObject.moving_right = False
            elif event.key == pygame.K_LEFT:
                shipObject.moving_left = False
        else:
            pass

def update_screen(setting,screen,ship):
    """Update the screen"""
    screen.fill(setting.bg_color)
    ship.blitme()

    pygame.display.flip()

