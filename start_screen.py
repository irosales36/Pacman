import pygame
from pygame.time import Clock
from button import Button
import game_functions as gf

def Start_Screen(screen, play_button, sb):
    """creates a start screen"""
    intro = True

    while intro:
        """shows the start screen until the player clicks the play button"""
        screen.fill((20, 20, 20))
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        mediumText = pygame.font.Font('freesansbold.ttf', 60)
        smallText =  pygame.font.Font('freesansbold.ttf', 30)
        smallerText = pygame.font.Font('freesansbold.ttf', 20)


        Text1Surf = largeText.render("PACMAN", True, (255, 128, 0))
        Text1Rect = Text1Surf.get_rect()
        Text2Surf = mediumText.render("PORTAL", True, (0, 60, 255))
        Text2Rect = Text2Surf.get_rect()


        Text3Surf = smallText.render("Blinky", True, (255, 255, 255))
        Text3Rect = Text3Surf.get_rect()
        Image3Surf = pygame.image.load('images/ghost1.png')
        Image3Rect = Image3Surf.get_rect()

        Text5Surf = smallText.render("Pinky", True, (255, 255, 255))
        Text5Rect = Text5Surf.get_rect()
        Image5Surf = pygame.image.load('images/ghost2.png')
        Image5Rect = Image5Surf.get_rect()

        Text6Surf = smallText.render("Inkey", True, (255, 255, 255))
        Text6Rect = Text6Surf.get_rect()
        Image6Surf = pygame.image.load('images/ghost3.png')
        Image6Rect = Image6Surf.get_rect()

        Text7Surf = smallText.render("Clyde", True, (255, 255, 255))
        Text7Rect = Text7Surf.get_rect()
        Image7Surf = pygame.image.load('images/ghost4.png')
        Image7Rect = Image7Surf.get_rect()

        Text8Surf = smallText.render("Pacman", True, (255, 255, 255))
        Text8Rect = Text8Surf.get_rect()
        Image8Surf = pygame.image.load('images/pacman.png')
        Image8Rect = Image8Surf.get_rect()

        Text4Surf = smallerText.render("By: Ivan Rosales", True, (255, 255, 255))
        Text4Rect = Text4Surf.get_rect()

        Text1Rect.center = ((700 / 2), (780 / 20) * 3)
        screen.blit(Text1Surf, Text1Rect)
        Text2Rect.center = ((700 / 2), (780 / 20) * 5)
        screen.blit(Text2Surf, Text2Rect)

        Text3Rect.center = ((700 / 2) + 40, (780 / 20) * 7)
        screen.blit(Text3Surf, Text3Rect)
        Image3Rect.centery = Text3Rect.centery
        Image3Rect.centerx = Text3Rect.centerx - 100
        screen.blit(Image3Surf, Image3Rect)

        Text5Rect.center = ((700 / 2) + 40, (780 / 40) * 17)
        screen.blit(Text5Surf, Text5Rect)
        Image5Rect.centery = Text5Rect.centery
        Image5Rect.centerx = Text5Rect.centerx - 100
        screen.blit(Image5Surf, Image5Rect)

        Text6Rect.center = ((700 / 2) + 40, (780 / 40) * 20)
        screen.blit(Text6Surf, Text6Rect)
        Image6Rect.centery = Text6Rect.centery
        Image6Rect.centerx = Text6Rect.centerx - 100
        screen.blit(Image6Surf, Image6Rect)

        Text7Rect.center = ((700 / 2) + 40, (780 / 40) * 23)
        screen.blit(Text7Surf, Text7Rect)
        Image7Rect.centery = Text7Rect.centery
        Image7Rect.centerx = Text7Rect.centerx - 100
        screen.blit(Image7Surf, Image7Rect)

        Text8Rect.center = ((700 / 2) + 40, (780 / 40) * 26)
        screen.blit(Text8Surf, Text8Rect)
        Image8Rect.centery = Text8Rect.centery
        Image8Rect.centerx = Text8Rect.centerx - 100
        screen.blit(Image8Surf, Image8Rect)

        Text4Rect.center = ((700 / 2), (780 / 20) * 17)
        screen.blit(Text4Surf, Text4Rect)


        # checks if the play button has been pressed
        play_button.draw_button()
        gf.check_button(play_button, sb)
        if sb.game_active:
            intro = False

        pygame.display.update()

