import sys
import pygame

from bullet import Bullet


def check_events(shipObject,bullets,settings,screen):
    """Respond to Mouse and Keyboard Events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,shipObject,settings,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,shipObject,settings,screen,bullets)
        else:
            pass

def update_screen(setting,screen,ship,bullets):
    """Update the screen"""
    screen.fill(setting.bg_color)
    ship.blitme()
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()

def check_keydown_events(event,shipObject,settings,screen,bullets):
    """Respond to Key Presses"""
    if event.key == pygame.K_RIGHT:
        shipObject.moving_right = True
    elif event.key == pygame.K_LEFT:
        shipObject.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(bullets,screen,settings,shipObject)

def check_keyup_events(event,shipObject,setting,screen,bullets):
    """Respond to Key Releases"""
    if event.key == pygame.K_RIGHT:
        shipObject.moving_right = False
    elif event.key == pygame.K_LEFT:
        shipObject.moving_left = False

def delete_bullets(bullets):
    """This function deletes the bullets when their y co-ordinate becomes less than 0.
    This prevents the memory leakage and processing power."""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(bullets,screen,settings,shipObject):
    new_bullet = Bullet(screen,settings,shipObject)
    bullets.add(new_bullet)
