import pygame
import sys
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
# Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # Responds to keypresses
    if event.key == pygame.K_RIGHT:
        ship.movement_right = True
    elif event.key == pygame.K_LEFT:
        ship.movement_left = True
    elif event.key == pygame.K_SPACE:
        # Creat new bullet and add it to bullets group
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    # Responds to key releases
    if event.key == pygame.K_RIGHT:
        ship.movement_right = False
    elif event.key == pygame.K_LEFT:
        ship.movement_left = False

def update_screen(ai_settings, screen, ship, bullets):
    # Updates the images on the screen and flip to new screen
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Make the most recently drawn screen visable
    pygame.display.flip()

def update_bullets(bullets):
    '''Updates position of bullets and gets ride of old bullets'''
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    '''Fires bullet if limit isnt reached'''
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
