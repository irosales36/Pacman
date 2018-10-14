import pygame

def check_pill_collision(screen, pacman, pills):
    """checks for pacman-powerpill collision"""
    collision = pygame.sprite.spritecollide(pacman, pills, True)
