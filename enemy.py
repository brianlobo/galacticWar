import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to represnt a single alien fleet'''
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien image and set its rect attribute
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store aliens extact position
        self.x = float(self.rect.x)

    def blitme(self):
        '''Draw the alien at its current location'''
        self.screen.blit(self.image, self.rect)
