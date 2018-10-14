import pygame
from pygame.sprite import Sprite
import sys

class Pacman(Sprite):

    def __init__(self, screen):
        """Initialize pacman, and set its starting position."""
        super(Pacman, self).__init__()
        self.screen = screen

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('images/pacman_right.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.right / 2
        self.rect.centery = 434

        # Store a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_pacman(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.center

    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right or self.moving_left:
            if ((self.moving_down and self.rect.centery < self.screen_rect.bottom - 90)
                    and (self.rect.centerx == 122 or self.rect.centerx == 188 or self.rect.centerx == 254
                    or self.rect.centerx == 320 or self.rect.centerx == 383 or self.rect.centerx == 446
                    or self.rect.centerx == 515 or self.rect.centerx == 617 or self.rect.centerx == 83 or self.rect.centerx == 578)):
                self.image = pygame.image.load('images/pacman_down.png')
                self.centery += 3

            elif ((self.moving_up and self.rect.centery > 95)\
                    and (self.rect.centerx == 122 or self.rect.centerx == 188 or self.rect.centerx == 254
                    or self.rect.centerx == 320 or self.rect.centerx == 383 or self.rect.centerx == 446
                    or self.rect.centerx == 515 or self.rect.centerx == 617  or self.rect.centerx == 83 or self.rect.centerx == 578)):
                self.image = pygame.image.load('images/pacman_up.png')
                self.centery -= 3

            elif ((self.moving_right and self.rect.centerx < self.screen_rect.right - 85)\
                    and (self.rect.centery == 95 or self.rect.centery == 173 or self.rect.centery == 236
                    or self.rect.centery == 302 or self.rect.centery == 371 or self.rect.centery == 434 or self.rect.centery == 500
                    or self.rect.centery == 563 or self.rect.centery == 623 or self.rect.centery == 630 or self.rect.centery == 692)):
                self.image = pygame.image.load('images/pacman_right.png')
                self.centerx += 3

            elif ((self.moving_left and self.rect.centerx > 85)\
                    and (self.rect.centery == 95 or self.rect.centery == 173 or self.rect.centery == 236
                    or self.rect.centery == 302 or self.rect.centery == 371 or self.rect.centery == 434 or self.rect.centery == 500
                    or self.rect.centery == 563 or self.rect. centery == 623 or self.rect.centery == 630 or self.rect.centery == 692)):
                self.image = pygame.image.load('images/pacman_left.png')
                self.centerx -= 3

        elif self.moving_up or self.moving_down:
            if ((self.moving_right and self.rect.centerx < self.screen_rect.right - 85)\
                    and (self.rect.centery == 95 or self.rect.centery == 173 or self.rect.centery == 236
                    or self.rect.centery == 302 or self.rect.centery == 371 or self.rect.centery == 434 or self.rect.centery == 500
                    or self.rect.centery == 563 or self.rect.centery == 623 or self.rect.centery == 630 or self.rect.centery == 692)):
                self.image = pygame.image.load('images/pacman_right.png')
                self.centerx += 3

            elif ((self.moving_left and self.rect.centerx > 85)\
                    and (self.rect.centery == 95 or self.rect.centery == 173 or self.rect.centery == 236
                    or self.rect.centery == 302 or self.rect.centery == 371 or self.rect.centery == 434 or self.rect.centery == 500
                    or self.rect.centery == 563 or self.rect. centery == 623 or self.rect.centery == 630 or self.rect.centery == 692)):
                self.image = pygame.image.load('images/pacman_left.png')
                self.centerx -= 3

            elif ((self.moving_down and self.rect.centery < self.screen_rect.bottom - 90)
                    and (self.rect.centerx == 122 or self.rect.centerx == 188 or self.rect.centerx == 254
                    or self.rect.centerx == 320 or self.rect.centerx == 383 or self.rect.centerx == 446
                    or self.rect.centerx == 515 or self.rect.centerx == 617 or self.rect.centerx == 83 or self.rect.centerx == 578)):
                self.image = pygame.image.load('images/pacman_down.png')
                self.centery += 3

            elif ((self.moving_up and self.rect.centery > 95)\
                    and (self.rect.centerx == 122 or self.rect.centerx == 188 or self.rect.centerx == 254
                    or self.rect.centerx == 320 or self.rect.centerx == 383 or self.rect.centerx == 446
                    or self.rect.centerx == 515 or self.rect.centerx == 617  or self.rect.centerx == 83 or self.rect.centerx == 578)):
                self.image = pygame.image.load('images/pacman_up.png')
                self.centery -= 3

        # Update rect object from self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        # print('x = ' + str(self.rect.centerx))
        # print('y = ' + str(self.rect.centery))

    def check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
            self.moving_left = False
        if event.key == pygame.K_LEFT:
            self.moving_left = True
            self.moving_right = False
        if event.key == pygame.K_UP:
            self.moving_up = True
            self.moving_down = False
        if event.key == pygame.K_DOWN:
            self.moving_down = True
            self.moving_up = False
        if event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.moving_left = False
        elif event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            # elif event.type == pygame.KEYUP:
            #     self.check_keyup_events(event)
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     mouse_x, mouse_y = pygame.mouse.get_pos()
            #     self.check_play_button(screen, stats, sb, play_button, mouse_x, mouse_y)

