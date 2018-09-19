import pygame
import sys

def check_events():
# Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    # Updates the images on the screen and flip to new screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Make the most recently drawn screen visable
    pygame.display.flip()
