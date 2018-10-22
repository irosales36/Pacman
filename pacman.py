import pygame
from pygame.sprite import Sprite
import sys

class Pacman(Sprite):

    def __init__(self, screen):
        """Initialize pacman, and set its starting position."""
        super(Pacman, self).__init__()
        self.screen = screen
        self.priority = True

        # Load the pacman image, and get its rect.
        self.image = pygame.image.load('images/pacman_right.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start pacman near the center of the screen
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

    def reset(self):
        """Center pacman on the screen."""
        self.rect.centerx = self.screen_rect.right / 2
        self.rect.centery = 434
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.image = pygame.image.load('images/pacman_right.png')

    def update(self):
        """Updates pacman's position based on movement flags."""

        if not self.priority:

            # check if pacman is moving down
            if ((self.moving_down and self.rect.centery < self.screen_rect.bottom - 90)
                    and ((self.rect.centerx == 83 and ((self.rect.centery > 94 and self.rect.centery < 236)
                                                       or (self.rect.centery > 499 and self.rect.centery < 563)
                                                       or (self.rect.centery > 625 and self.rect.centery < 692)))
                         or (self.rect.centerx == 122 and (self.rect.centery > 562 and self.rect.centery < 626))
                         or (self.rect.centerx == 188 and (self.rect.centery > 94 and self.rect.centery < 626))
                         or (self.rect.centerx == 254 and ((self.rect.centery > 172 and self.rect.centery < 236)
                                                     or (self.rect.centery > 301 and self.rect.centery < 500)
                                                     or (self.rect.centery > 562 and self.rect.centery < 626)))
                         or (self.rect.centerx == 320 and ((self.rect.centery > 94 and self.rect.centery < 173)
                                                     or (self.rect.centery > 235 and self.rect.centery < 302)
                                                     or (self.rect.centery > 499 and self.rect.centery < 563)
                                                     or (self.rect.centery > 625 and self.rect.centery < 692)))
                         or (self.rect.centerx == 383 and ((self.rect.centery > 94 and self.rect.centery < 173)
                                                     or (self.rect.centery > 235 and self.rect.centery < 302)
                                                     or (self.rect.centery > 499 and self.rect.centery < 563)
                                                     or (self.rect.centery > 625 and self.rect.centery < 692)))
                         or (self.rect.centerx == 446 and ((self.rect.centery > 172 and self.rect.centery < 236)
                                                     or (self.rect.centery > 301 and self.rect.centery < 500)
                                                     or (self.rect.centery > 562 and self.rect.centery < 626)))
                         or (self.rect.centerx == 515 and (self.rect.centery > 94 and self.rect.centery < 626))
                         or (self.rect.centerx == 578 and (self.rect.centery > 562 and self.rect.centery < 626))
                         or (self.rect.centerx == 617 and ((self.rect.centery > 94 and self.rect.centery < 236)
                                                     or (self.rect.centery > 499 and self.rect.centery < 563)
                                                     or (self.rect.centery > 625 and self.rect.centery < 692))))):
                self.image = pygame.image.load('images/pacman_down.png')
                self.centery += 3

            # check if pacman is moving up
            elif ((self.moving_up and self.rect.centery > 95) \
                  and ((self.rect.centerx == 83 and ((self.rect.centery > 95 and self.rect.centery < 237)
                                                     or (self.rect.centery > 500 and self.rect.centery < 564)
                                                     or (self.rect.centery > 626 and self.rect.centery < 693)))
                       or (self.rect.centerx == 122 and (self.rect.centery > 563 and self.rect.centery < 627))
                       or (self.rect.centerx == 188 and (self.rect.centery > 95 and self.rect.centery < 627))
                       or (self.rect.centerx == 254 and ((self.rect.centery > 173 and self.rect.centery < 237)
                                                     or (self.rect.centery > 302 and self.rect.centery < 501)
                                                     or (self.rect.centery > 563 and self.rect.centery < 627)))
                       or (self.rect.centerx == 320 and ((self.rect.centery > 95 and self.rect.centery < 174)
                                                     or (self.rect.centery > 236 and self.rect.centery < 303)
                                                     or (self.rect.centery > 500 and self.rect.centery < 564)
                                                     or (self.rect.centery > 626 and self.rect.centery < 693)))
                       or (self.rect.centerx == 383 and ((self.rect.centery > 95 and self.rect.centery < 174)
                                                     or (self.rect.centery > 236 and self.rect.centery < 303)
                                                     or (self.rect.centery > 500 and self.rect.centery < 564)
                                                     or (self.rect.centery > 626 and self.rect.centery < 693)))
                       or (self.rect.centerx == 446 and ((self.rect.centery > 173 and self.rect.centery < 237)
                                                     or (self.rect.centery > 302 and self.rect.centery < 501)
                                                     or (self.rect.centery > 563 and self.rect.centery < 627)))
                       or (self.rect.centerx == 515 and (self.rect.centery > 95 and self.rect.centery < 627))
                       or (self.rect.centerx == 578 and (self.rect.centery > 563 and self.rect.centery < 627))
                       or (self.rect.centerx == 617 and ((self.rect.centery > 95 and self.rect.centery < 237)
                                                     or (self.rect.centery > 500 and self.rect.centery < 564)
                                                     or (self.rect.centery > 626 and self.rect.centery < 693))))):
                self.image = pygame.image.load('images/pacman_up.png')
                self.centery -= 3

            # check if pacman is moving right
            elif ((self.moving_right and self.rect.centerx < self.screen_rect.right - 85) \
                    and ((self.rect.centery == 95 and ((self.rect.centerx > 82 and self.rect.centerx < 320)
                                                      or (self.rect.centerx > 382 and self.rect.centerx < 618)))
                         or (self.rect.centery == 173 and (self.rect.centerx > 82 and self.rect.centerx < 618))
                         or (self.rect.centery == 236 and ((self.rect.centerx > 82 and self.rect.centerx < 188)
                                                         or (self.rect.centerx > 253 and self.rect.centerx < 320)
                                                         or (self.rect.centerx > 382 and self.rect.centerx < 446)
                                                         or (self.rect.centerx > 514 and self.rect.centerx < 617)))
                         or (self.rect.centery == 302 and (self.rect.centerx > 253 and self.rect.centerx < 446))
                         or (self.rect.centery == 371 and ((self.rect.centerx > 82 and self.rect.centerx < 254)
                                                    or (self.rect.centerx > 445 and self.rect.centerx < 617)))
                         or (self.rect.centery == 434 and (self.rect.centerx > 253 and self.rect.centerx < 446))
                         or (self.rect.centery == 500 and ((self.rect.centerx > 82 and self.rect.centerx < 320)
                                                    or (self.rect.centerx > 382 and self.rect.centerx < 618)))
                         or (self.rect.centery == 563 and ((self.rect.centerx > 82 and self.rect.centerx < 122)
                                                    or (self.rect.centerx > 187 and self.rect.centerx < 515)
                                                    or (self.rect.centerx > 577 and self.rect.centerx < 617)))
                         or (self.rect.centery == 626 and ((self.rect.centerx > 82 and self.rect.centerx < 188)
                                                         or (self.rect.centerx > 253 and self.rect.centerx < 320)
                                                         or (self.rect.centerx > 382 and self.rect.centerx < 446)
                                                         or (self.rect.centerx > 514 and self.rect.centerx < 617)))
                         or self.rect.centery == 692)):
                self.image = pygame.image.load('images/pacman_right.png')
                self.centerx += 3
                self.rect.centerx = self.centerx

            # check if pacman is moving left
            elif ((self.moving_left and self.rect.centerx > 85) \
                  and ((self.rect.centery == 95 and ((self.rect.centerx > 82 and self.rect.centerx < 321)
                                                    or (self.rect.centerx > 383 and self.rect.centerx < 618)))
                       or (self.rect.centery == 173 and (self.rect.centerx > 82 and self.rect.centerx < 618))
                       or (self.rect.centery == 236 and ((self.rect.centerx > 82 and self.rect.centerx < 189)
                                                         or (self.rect.centerx > 254 and self.rect.centerx < 321)
                                                         or (self.rect.centerx > 383 and self.rect.centerx < 447)
                                                         or (self.rect.centerx > 515 and self.rect.centerx < 618)))
                       or (self.rect.centery == 302 and (self.rect.centerx > 254 and self.rect.centerx < 447))
                       or (self.rect.centery == 371 and ((self.rect.centerx > 83 and self.rect.centerx < 255)
                                                    or (self.rect.centerx > 446 and self.rect.centerx < 618)))
                       or (self.rect.centery == 434 and (self.rect.centerx > 254 and self.rect.centerx < 447))
                       or (self.rect.centery == 500 and ((self.rect.centerx > 82 and self.rect.centerx < 321)
                                                    or (self.rect.centerx > 383 and self.rect.centerx < 618)))
                       or (self.rect.centery == 563 and ((self.rect.centerx > 82 and self.rect.centerx < 123)
                                                    or (self.rect.centerx > 188 and self.rect.centerx < 516)
                                                    or (self.rect.centerx > 578 and self.rect.centerx < 618)))
                       or (self.rect.centery == 626 and ((self.rect.centerx > 82 and self.rect.centerx < 189)
                                                         or (self.rect.centerx > 254 and self.rect.centerx < 321)
                                                         or (self.rect.centerx > 383 and self.rect.centerx < 447)
                                                         or (self.rect.centerx > 515 and self.rect.centerx < 618)))
                       or self.rect.centery == 692)):
                self.image = pygame.image.load('images/pacman_left.png')
                self.centerx -= 3
                self.rect.centerx = self.centerx

        elif self.priority:

            # check if pacman is moving right
            if ((self.moving_right and self.rect.centerx < self.screen_rect.right - 85) \
                  and ((self.rect.centery == 95 and ((self.rect.centerx > 82 and self.rect.centerx < 320)
                                                    or (self.rect.centerx > 382 and self.rect.centerx < 618)))
                       or (self.rect.centery == 173 and (self.rect.centerx > 82 and self.rect.centerx < 618))
                       or (self.rect.centery == 236 and ((self.rect.centerx > 82 and self.rect.centerx < 188)
                                                         or (self.rect.centerx > 253 and self.rect.centerx < 320)
                                                         or (self.rect.centerx > 382 and self.rect.centerx < 446)
                                                         or (self.rect.centerx > 514 and self.rect.centerx < 617)))
                       or (self.rect.centery == 302 and (self.rect.centerx > 253 and self.rect.centerx < 446))
                       or (self.rect.centery == 371 and ((self.rect.centerx > 82 and self.rect.centerx < 254)
                                                    or (self.rect.centerx > 445 and self.rect.centerx < 617)))
                       or (self.rect.centery == 434 and (self.rect.centerx > 253 and self.rect.centerx < 446))
                       or (self.rect.centery == 500 and ((self.rect.centerx > 82 and self.rect.centerx < 320)
                                                    or (self.rect.centerx > 382 and self.rect.centerx < 618)))
                       or (self.rect.centery == 563 and ((self.rect.centerx > 82 and self.rect.centerx < 122)
                                                    or (self.rect.centerx > 187 and self.rect.centerx < 515)
                                                    or (self.rect.centerx > 577 and self.rect.centerx < 617)))
                       or (self.rect.centery == 626 and ((self.rect.centerx > 82 and self.rect.centerx < 188)
                                                         or (self.rect.centerx > 253 and self.rect.centerx < 320)
                                                         or (self.rect.centerx > 382 and self.rect.centerx < 446)
                                                         or (self.rect.centerx > 514 and self.rect.centerx < 617)))
                       or self.rect.centery == 692)):
                self.image = pygame.image.load('images/pacman_right.png')
                self.centerx += 3
                self.rect.centerx = self.centerx

            # check if pacman is moving left
            elif ((self.moving_left and self.rect.centerx > 85) \
                  and ((self.rect.centery == 95 and ((self.rect.centerx > 82 and self.rect.centerx < 321)
                                                    or (self.rect.centerx > 383 and self.rect.centerx < 618)))
                       or (self.rect.centery == 173 and (self.rect.centerx > 82 and self.rect.centerx < 618))
                       or (self.rect.centery == 236 and ((self.rect.centerx > 82 and self.rect.centerx < 189)
                                                    or (self.rect.centerx > 254 and self.rect.centerx < 321)
                                                    or (self.rect.centerx > 383 and self.rect.centerx < 447)
                                                    or (self.rect.centerx > 515 and self.rect.centerx < 618)))
                       or (self.rect.centery == 302 and (self.rect.centerx > 254 and self.rect.centerx < 447))
                       or (self.rect.centery == 371 and ((self.rect.centerx > 83 and self.rect.centerx < 255)
                                                    or (self.rect.centerx > 446 and self.rect.centerx < 618)))
                       or (self.rect.centery == 434 and (self.rect.centerx > 254 and self.rect.centerx < 447))
                       or (self.rect.centery == 500 and ((self.rect.centerx > 82 and self.rect.centerx < 321)
                                                    or (self.rect.centerx > 383 and self.rect.centerx < 618)))
                       or (self.rect.centery == 563 and ((self.rect.centerx > 82 and self.rect.centerx < 123)
                                                    or (self.rect.centerx > 188 and self.rect.centerx < 516)
                                                    or (self.rect.centerx > 578 and self.rect.centerx < 618)))
                       or (self.rect.centery == 626 and ((self.rect.centerx > 82 and self.rect.centerx < 189)
                                                         or (self.rect.centerx > 254 and self.rect.centerx < 321)
                                                         or (self.rect.centerx > 383 and self.rect.centerx < 447)
                                                         or (self.rect.centerx > 515 and self.rect.centerx < 618)))
                       or self.rect.centery == 692)):
                self.image = pygame.image.load('images/pacman_left.png')
                self.centerx -= 3
                self.rect.centerx = self.centerx

            # check if pacman is moving down
            elif ((self.moving_down and self.rect.centery < self.screen_rect.bottom - 90)
                  and ((self.rect.centerx == 83 and ((self.rect.centery > 94 and self.rect.centery < 236)
                                                     or (self.rect.centery > 499 and self.rect.centery < 563)
                                                     or (self.rect.centery > 625 and self.rect.centery < 692)))
                       or (self.rect.centerx == 122 and (self.rect.centery > 562 and self.rect.centery < 626))
                       or (self.rect.centerx == 188 and (self.rect.centery > 94 and self.rect.centery < 626))
                       or (self.rect.centerx == 254 and ((self.rect.centery > 172 and self.rect.centery < 236)
                                                     or (self.rect.centery > 301 and self.rect.centery < 500)
                                                     or (self.rect.centery > 562 and self.rect.centery < 626)))
                       or (self.rect.centerx == 320 and ((self.rect.centery > 94 and self.rect.centery < 173)
                                                     or (self.rect.centery > 235 and self.rect.centery < 302)
                                                     or (self.rect.centery > 499 and self.rect.centery < 563)
                                                     or (self.rect.centery > 625 and self.rect.centery < 692)))
                       or (self.rect.centerx == 383 and ((self.rect.centery > 94 and self.rect.centery < 173)
                                                     or (self.rect.centery > 235 and self.rect.centery < 302)
                                                     or (self.rect.centery > 499 and self.rect.centery < 563)
                                                     or (self.rect.centery > 625 and self.rect.centery < 692)))
                       or (self.rect.centerx == 446 and ((self.rect.centery > 172 and self.rect.centery < 236)
                                                     or (self.rect.centery > 301 and self.rect.centery < 500)
                                                     or (self.rect.centery > 562 and self.rect.centery < 626)))
                       or (self.rect.centerx == 515 and (self.rect.centery > 94 and self.rect.centery < 626))
                       or (self.rect.centerx == 578 and (self.rect.centery > 562 and self.rect.centery < 626))
                       or (self.rect.centerx == 617 and ((self.rect.centery > 94 and self.rect.centery < 236)
                                                     or (self.rect.centery > 499 and self.rect.centery < 563)
                                                     or (self.rect.centery > 625 and self.rect.centery < 692))))):
                self.image = pygame.image.load('images/pacman_down.png')
                self.centery += 3

            # check if pacman is moving up
            elif ((self.moving_up and self.rect.centery > 95) \
                  and ((self.rect.centerx == 83 and ((self.rect.centery > 95 and self.rect.centery < 237)
                                                     or (self.rect.centery > 500 and self.rect.centery < 564)
                                                     or (self.rect.centery > 626 and self.rect.centery < 693)))
                       or (self.rect.centerx == 122 and (self.rect.centery > 563 and self.rect.centery < 627))
                       or (self.rect.centerx == 188 and (self.rect.centery > 95 and self.rect.centery < 627))
                       or (self.rect.centerx == 254 and ((self.rect.centery > 173 and self.rect.centery < 237)
                                                     or (self.rect.centery > 302 and self.rect.centery < 501)
                                                     or (self.rect.centery > 563 and self.rect.centery < 627)))
                       or (self.rect.centerx == 320 and ((self.rect.centery > 95 and self.rect.centery < 174)
                                                     or (self.rect.centery > 236 and self.rect.centery < 303)
                                                     or (self.rect.centery > 500 and self.rect.centery < 564)
                                                     or (self.rect.centery > 626 and self.rect.centery < 693)))
                       or (self.rect.centerx == 383 and ((self.rect.centery > 95 and self.rect.centery < 174)
                                                     or (self.rect.centery > 236 and self.rect.centery < 303)
                                                     or (self.rect.centery > 500 and self.rect.centery < 564)
                                                     or (self.rect.centery > 626 and self.rect.centery < 693)))
                       or (self.rect.centerx == 446 and ((self.rect.centery > 173 and self.rect.centery < 237)
                                                     or (self.rect.centery > 302 and self.rect.centery < 501)
                                                     or (self.rect.centery > 563 and self.rect.centery < 627)))
                       or (self.rect.centerx == 515 and (self.rect.centery > 95 and self.rect.centery < 627))
                       or (self.rect.centerx == 578 and (self.rect.centery > 563 and self.rect.centery < 627))
                       or (self.rect.centerx == 617 and ((self.rect.centery > 95 and self.rect.centery < 237)
                                                     or (self.rect.centery > 500 and self.rect.centery < 564)
                                                     or (self.rect.centery > 626 and self.rect.centery < 693))))):
                self.image = pygame.image.load('images/pacman_up.png')
                self.centery -= 3


        # Update rect object from self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        # print('y = ' + str(self.rect.centery))
        # print('x = ' + str(self.rect.centerx))

    def check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
            self.moving_left = False
            self.priority = True
        if event.key == pygame.K_LEFT:
            self.moving_left = True
            self.moving_right = False
            self.priority = True
        if event.key == pygame.K_UP:
            self.moving_up = True
            self.moving_down = False
            self.priority = False
        if event.key == pygame.K_DOWN:
            self.moving_down = True
            self.moving_up = False
            self.priority = False
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

