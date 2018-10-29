import pygame
from maze import Maze
from pacman import Pacman
from ghost import Ghost
from pygame.sprite import Group
from button import Button
from time import sleep
from scoreboard import Scoreboard
import game_functions as gf
import start_screen as ss
import game_over as go
import random

def run_game():
    BLACK = (0, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((700, 780))
    pygame.display.set_caption("Pacman Portal")
    clock = pygame.time.Clock()
    start_tick = pygame.time.get_ticks()
    random.seed()
    play_button = Button(screen, "Play")
    sb = Scoreboard(screen)

    # create pacman
    pacman = Pacman(screen)

    # create ghosts
    ghost1 = Ghost(screen, 1)
    ghost2 = Ghost(screen, 2)
    ghost3 = Ghost(screen, 3)
    ghost4 = Ghost(screen, 4)
    ghosts = Group(ghost1, ghost2, ghost3, ghost4)

    # create a group for the pills
    pills = Group()

    # create the maze
    maze = Maze(screen, pills, mazefile='images/pacmanportalmaze.txt', brickfile='blue_square',
                shieldfile='shield', portalfile='portal2', powerpill='powerpill', powerpill2='powerpill')

    # def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'

    # pacman intro sound
    intro_music = pygame.mixer.Sound('music/pacman_beginning.wav')
    intro_music.play()

    # show the start screen
    ss.Start_Screen(screen, play_button, sb)

    # game main loop
    while True:

        if sb.game_active:
            screen.fill(BLACK)
            # seconds = int((pygame.time.get_ticks() - start_tick) / 500)
            rand_num = random.randint(0, 100)
            pacman.check_events()
            pacman.update()
            pacman.blitme()
            maze.blitme()


            for ghost in ghosts:
                ghost.get_direction(rand_num)
                ghost.update()
                ghost.blitme()

            gf.check_pill_collision(pacman, pills, sb, maze)
            gf.check_ghost_collision(pacman, ghosts, sb)
            sb.show_score()
            pygame.display.flip()

            # checks if no lives are left and displays the "game over" screen
            if sb.lives_left == 0:
                sb.game_active = False
                sleep(1)
                go.Game_Over(screen, play_button, sb)
                sb.reset_stats()
                maze.build()
                pacman.reset()
                for ghost in ghosts:
                    ghost.reset()
                sb.prep_score()
                sb.prep_high_score()
                sb.prep_level()
                sb.prep_lives()
                pygame.display.flip()
            # print("Game Active")

        else:
            pygame.mouse.set_visible(True)
            pacman.reset()
            for ghost in ghosts:
                ghost.reset()

            play_button.draw_button()
            pygame.display.flip()
            while not sb.game_active:
                gf.check_button(play_button, sb)

        # print("seconds = " + str(seconds))

        # set the fps
        clock.tick(60)

run_game()
