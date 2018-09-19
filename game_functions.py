import pygame
import sys

def check_events(ship):
# Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship):
    # Responds to keypresses
    if event.key == pygame.K_RIGHT:
        ship.movement_right = True
    elif event.key == pygame.K_LEFT:
        ship.movement_left = True

def check_keyup_events(event, ship):
    # Responds to key releases
    if event.key == pygame.K_RIGHT:
        ship.movement_right = False
    elif event.key == pygame.K_LEFT:
        ship.movement_left = False

def update_screen(ai_settings, screen, ship):
    # Updates the images on the screen and flip to new screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Make the most recently drawn screen visable
    pygame.display.flip()
