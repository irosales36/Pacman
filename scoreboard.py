import pygame.font
from pygame.sprite import Group

from pacman import Pacman

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, screen):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.high_score = 0
        self.lives_limit = 3
        self.game_active = False
        self.reset_stats()

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.lives_left = self.lives_limit
        self.score = 0
        self.level = 1

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.score, -1))
        score_str = "{:,}".format(rounded_score)
        score_str = "Score: " + score_str
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            (20, 20, 20))

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        high_score_str = "High Score: " + high_score_str
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, (20, 20, 20))

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.level)
        level_str = "Level: " + level_str
        self.level_image = self.font.render(level_str, True,
                                            self.text_color, (20, 20, 20))

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 5

    def prep_lives(self):
        """Show how many lives are left."""
        lives_str = "Lives: "
        self.lives_image = self.font.render(lives_str, True,
                                            self.text_color, (20, 20, 20))
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.x = 15
        self.lives_rect.y = 10

        self.pacmans = Group()
        for pacman_number in range(self.lives_left):
            pacman = Pacman(self.screen)
            pacman.rect.x = 20 + self.lives_rect.width + pacman_number * (pacman.rect.width + 10)
            pacman.rect.y = 10
            self.pacmans.add(pacman)

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.lives_image, self.lives_rect)
        # Draw pacmans.
        self.pacmans.draw(self.screen)
