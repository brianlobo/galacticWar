import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions


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
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        game_functions.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # Updates the images on the screen and flip to new screen
        game_functions.update_screen(ai_settings, screen, ship, bullets)

if __name__ == '__main__':
    run_game()
