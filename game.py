import pygame
from maze import Maze
from pacman import Pacman
from ghost import Ghost
from pygame.sprite import Group
import game_functions as gf
import random

def run_game():
    BLACK = (0, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((700, 780))
    pygame.display.set_caption("Pacman Portal")
    clock = pygame.time.Clock()
    start_tick = pygame.time.get_ticks()
    random.seed()

    # create pacman
    pacman = Pacman(screen)

    # create ghosts
    ghost1 = Ghost(screen, 1)
    ghost2 = Ghost(screen, 2)
    ghost3 = Ghost(screen, 3)
    ghost4 = Ghost(screen, 4)
    ghosts = Group(ghost1, ghost2, ghost3, ghost4)

    pills = Group()

    # create the maze
    maze = Maze(screen, pills, mazefile='images/pacmanportalmaze.txt', brickfile='blue_square',
                shieldfile='shield', portalfile='portal2', powerpill='powerpill', powerpill2='powerpill')

    # def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'

    while True:
        screen.fill(BLACK)
        seconds = int((pygame.time.get_ticks() - start_tick) / 500)
        rand_num = random.randint(0, 100)
        pacman.check_events()
        pacman.update()
        pacman.blitme()
        maze.blitme()
        for ghost in ghosts:
            ghost.get_direction(rand_num)
            ghost.update()
            ghost.blitme()

        gf.check_pill_collision(screen, pacman, pills)
        pygame.display.flip()

        print("seconds = " + str(seconds))

        # set the fps
        clock.tick(60)

run_game()
