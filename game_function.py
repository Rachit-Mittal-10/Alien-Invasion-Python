import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien


def check_events(shipObject,bullets,settings,screen,aliens,stat,play_button):
    """Respond to Mouse and Keyboard Events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stat,play_button,mouse_x,mouse_y,settings,screen,shipObject,aliens,bullets)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,shipObject,settings,screen,bullets,stat,aliens)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,shipObject,settings,screen,bullets)
        else:
            pass


def update_screen(setting,screen,ship,bullets,aliens,stat,play_button):
    """Update the screen"""
    screen.fill(setting.bg_color)
    if not stat.game_active:
        play_button.draw_button()
    else:
        ship.blitme()
        aliens.draw(screen)
        # Redraw all bullets behind ship and aliens
        for bullet in bullets.sprites():
            bullet.draw_bullet()
    pygame.display.flip()


def check_keydown_events(event,shipObject,settings,screen,bullets,stats,aliens):
    """Respond to Key Presses"""
    if event.key == pygame.K_RIGHT:
        shipObject.moving_right = True
    elif event.key == pygame.K_LEFT:
        shipObject.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(bullets,screen,settings,shipObject)
    elif event.key == pygame.K_q:
        sys.exit()
    elif stats.game_active == False and event.key in (pygame.K_p, pygame.K_RETURN, pygame.K_SPACE):
        start_game(stats,settings,screen,shipObject,aliens,bullets)


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


def check_bullet_collision(aliens,bullets,settings,screen,shipObject):
    "Checks the bullet collision."
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        create_fleet(settings,screen,aliens,shipObject)


def update_bullets_screen(bullets,aliens,settings,screen,shipObject):
    """Delete the bullets on the screen either collided or went out of screen"""
    bullets.update()
    delete_bullets(bullets)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True, True)
    check_bullet_collision(aliens,bullets,settings,screen,shipObject)
    

def get_number_aliens(settings,alien_width):
    """Gets the number of aliens possible in the row"""
    available_space_x = settings.width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x


def create_alien(settings,screen,aliens,alien_number,row_number):
    """Creates the alien and adds to the group"""
    alien = Alien(settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)


def get_number_rows(settings,alien_height,ship_height):
    available_space_y = settings.height - 13*alien_height - ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def create_fleet(settings,screen,aliens,shipObject):
    """Create the full fleet of aliens."""
    alienObject = Alien(settings,screen)
    alien_width = alienObject.rect.width
    alien_height = alienObject.rect.height
    ship_height = shipObject.rect.height
    number_aliens_x = get_number_aliens(settings,alien_width)
    number_rows = get_number_rows(settings,alien_height,ship_height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings,screen,aliens,alien_number,row_number)


def update_aliens(settings,aliens,shipObject,screen,stats,bullets):
    """Update the position of all the alien in the fleet"""
    check_fleet_edges(settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(shipObject,aliens):
        ship_hit(settings,stats,screen,shipObject,aliens,bullets)
    check_alien_bottom(settings,stats,screen,shipObject,aliens,bullets)


def check_fleet_edges(settings,aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings,aliens)
            break


def change_fleet_direction(settings,aliens):
    """Drop the entire fleet and change direction of fleet."""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def ship_hit(settings,stat,screen,shipObjet,aliens,bullets):
    """Responds to ship being hit by alien."""
    if stat.ship_left > 0:
        stat.ship_left -= 1
        aliens.empty()
        bullets.empty()
        settings.decrease_speed()
        create_fleet(settings,screen,aliens,shipObjet)
        shipObjet.center_ship()
        sleep(1)
    else:
        stat.game_active = False


def check_alien_bottom(settings,stat,screen,shipObject,aliens,bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings,stat,screen,shipObject,aliens,bullets)
            break


def check_play_button(stat,play_button,mouse_x,mouse_y,settings,screen,shipObject,aliens,bullets):
    """Start the New Game when Player clicks the play."""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stat.game_active:
        settings.initialise_dynamic_settings()
        start_game(stat,settings,screen,shipObject,aliens,bullets)
        pygame.mouse.set_visible(False)


def start_game(stat,settings,screen,shipObject,aliens,bullets):
    pygame.mouse.set_visible(False)
    stat.reset_stats()
    stat.game_active = True
    aliens.empty()
    bullets.empty()
    create_fleet(settings,screen,aliens,shipObject)
    shipObject.center_ship()
