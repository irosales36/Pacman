import pygame
import sys
from button import Button



def check_button(play_button, sb):
    """checks if the play button has been pressed"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
            if button_clicked and not sb.game_active:
                pygame.mouse.set_visible(False)

                sb.game_active = True
                sb.prep_score()
                sb.prep_high_score()
                sb.prep_level()
                sb.prep_lives()
                # sb.reset_stats()


def check_pill_collision(pacman, pills, sb, maze):
    """checks for pacman-powerpill collision"""
    collision = pygame.sprite.spritecollide(pacman, pills, True)
    chomp_sound = pygame.mixer.Sound('music/pacman_chomp.wav')
    if collision:
        chomp_sound.play()
        sb.score += 10
        sb.prep_score()
        if sb.score > sb.high_score:
            sb.high_score = sb.score
            sb.prep_high_score()

    if len(pills) == 0:
        # If all the pills are eaten, start a new level
        maze.build()
        # Increase level
        sb.level += 1
        sb.prep_level()
        sb.game_active = False


def check_ghost_collision(pacman, ghosts, sb):
    """checks for pacman-ghost collision"""
    collision = pygame.sprite.spritecollide(pacman, ghosts, False)
    death_sound = pygame.mixer.Sound('music/pacman_death.wav')
    if collision:
        death_sound.play()
        sb.lives_left -= 1
        sb.prep_lives()
        sb.game_active = False

def reset(): pass