import pygame
from imagerect import ImageRect
from pill import Pill

class Maze:
    RED = (255, 0 , 0)
    BRICK_SIZE = 13

    def __init__(self, screen, pills, mazefile, brickfile, shieldfile, portalfile, powerpill, powerpill2):
        self.screen = screen
        self.pills = pills
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []
        self.shields = []
        self.hportals = []
        self.vportals = []
        self.powerpills = []
        self.powerpills2 = []

        sz = Maze.BRICK_SIZE
        self.brick = ImageRect(screen, brickfile, sz, sz)
        self.shield = ImageRect(screen, shieldfile, sz, sz)
        self.hportal = ImageRect(screen, portalfile, sz, 5 * sz)
        self.vportal = ImageRect(screen, portalfile, 5 * sz, sz)
        self.vportal.image = pygame.transform.rotate(self.hportal.image, 90)
        self.powerpill = ImageRect(screen, powerpill, int(0.5*sz), int(0.5*sz))
        self.powerpill2 = ImageRect(screen, powerpill2, sz, sz)

        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self):
        r = self.brick.rect
        rshield = self.shield.rect
        rhportal = self.hportal.rect
        rvportal = self.vportal.rect
        rpowerpill = self.powerpill.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'o':
                    self.shields.append(pygame.Rect(ncol * dx, nrow * dy, rshield.width, rshield.height))
                elif col == 'h':
                    self.hportals.append(pygame.Rect(ncol * dx, nrow * dy, rhportal.width, rhportal.height))
                elif col == 'v':
                    self.vportals.append(pygame.Rect(ncol * dx, nrow * dy, rvportal.width, rvportal.height))
                elif col == 'p':
                    x = ncol * dx + rpowerpill.width/2
                    y = nrow * dy + rpowerpill.height/2
                    big = False
                    pill = Pill(self.screen, x, y, big)
                    self.pills.add(pill)
                elif col == 'P':
                    x = ncol * dx
                    y = nrow * dy
                    big = True
                    pill = Pill(self.screen, x, y, big)
                    self.pills.add(pill)

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.shields:
            self.screen.blit(self.shield.image, rect)
        for rect in self.hportals:
            self.screen.blit(self.hportal.image, rect)
        for rect in self.vportals:
            self.screen.blit(self.vportal.image, rect)
        for pill in self.pills:
            pill.blitme()
        for rect in self.powerpills2:
            self.screen.blit(self.powerpill2.image, rect)