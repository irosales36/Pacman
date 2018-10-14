import pygame
from pygame.sprite import Sprite
import sys

class Pill(Sprite):

    def __init__(self, screen, x, y, big):
        """Initialize the pill, and set its starting position."""
        super(Pill, self).__init__()
        self.screen = screen

        # Load the ship image, and get its rect.
        if big:
            self.image = pygame.image.load('images/powerpill2.png')
        elif not big:
            self.image = pygame.image.load('images/powerpill3.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.left = x
        self.rect.top = y

    def update(self): pass

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)