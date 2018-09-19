import pygame
import sys

def check_events():
# Watch for keyboard and mouse events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Redraw screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Make the most recently drawn screen visable
    pygame.display.flip()
