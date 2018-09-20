import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from enemy import Alien
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

    # Make the ship, bullets, and group of aliens
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Creates a fleet of enemies
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        game_functions.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        game_functions.update_bullets(bullets)
        game_functions.update_aliens(ai_settings, aliens)
        game_functions.update_screen(ai_settings, screen, ship, aliens, bullets)

if __name__ == '__main__':
    run_game()
