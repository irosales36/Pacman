import pygame
from maze import Maze
from pacman import Pacman
from pygame.sprite import Group
import game_functions as gf

def run_game():
    BLACK = (0, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((700, 780))
    pygame.display.set_caption("Pacman Portal")
    clock = pygame.time.Clock()

    # create pacman
    pacman = Pacman(screen)
    pills = Group()


    # create the maze
    maze = Maze(screen, pills, mazefile='images/pacmanportalmaze.txt', brickfile='blue_square',
                shieldfile='shield', portalfile='portal2', powerpill='powerpill', powerpill2='powerpill')

    # def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'

    while True:
        screen.fill(BLACK)
        pacman.check_events()
        pacman.update()
        pacman.blitme()
        maze.blitme()
        gf.check_pill_collision(screen, pacman, pills)
        pygame.display.flip()

        # set the fps
        clock.tick(60)

run_game()
