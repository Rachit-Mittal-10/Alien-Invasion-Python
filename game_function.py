import sys
import pygame

def check_events(shipObject):
    """Respond to Mouse and Keyboard Events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,shipObject)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,shipObject)
        else:
            pass

def update_screen(setting,screen,ship):
    """Update the screen"""
    screen.fill(setting.bg_color)
    ship.blitme()

    pygame.display.flip()

def check_keydown_events(event,shipObject):
    """Respond to Key Presses"""
    if event.key == pygame.K_RIGHT:
        shipObject.moving_right = True
    elif event.key == pygame.K_LEFT:
        shipObject.moving_left = True

def check_keyup_events(event,shipObject):
    """Respond to Key Releases"""
    if event.key == pygame.K_RIGHT:
        shipObject.moving_right = False
    elif event.key == pygame.K_LEFT:
        shipObject.moving_left = False

