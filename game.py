import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Init game and create a screen object
    pygame.init()
    ai_settings = Settings()
    # Setting screen dimensions
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
    # Setting caption
    pygame.display.set_caption("Galactic War")

    # Make the ship
    ship = Ship(screen)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Redraw screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # Make the most recently drawn screen visable
        pygame.display.flip()

if __name__ == '__main__':
    run_game()
