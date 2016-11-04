#!/usr/bin/python
import time
import pygame
import random
import sys
FPS = 25
WWIDTH = 660
WHEIGHT = 795
BOXSIZE = 20
BWIDTH = 32
BHEIGHT = 32
BLANK = '.'
GRAY = (185, 185, 185)
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (255,   0,   0)
BLUE = (0,   0, 255)
TEMPWIDTH = 5
TEMPHEIGHT = 5
SideMargin = int((WWIDTH - BWIDTH * BOXSIZE) / 2)
TopMargin = WHEIGHT - (BHEIGHT * BOXSIZE) - 5

S_SHAPE = [['.....',
            '.....',
            '..OO.',
            '.OO..',
            '.....'],
           ['.....',
            '..O..',
            '..OO.',
            '...O.',
            '.....']]

Z_SHAPE = [['.....',
            '.....',
            '.OO..',
            '..OO.',
            '.....'],
           ['.....',
            '..O..',
            '.OO..',
            '.O...',
            '.....']]

I_SHAPE = [['..O..',
            '..O..',
            '..O..',
            '..O..',
            '.....'],
           ['.....',
            '.....',
            'OOOO.',
            '.....',
            '.....']]

O_SHAPE = [['.....',
            '.....',
            '.OO..',
            '.OO..',
            '.....']]

L_SHAPE = [['.....',
            '...O.',
            '.OOO.',
            '.....',
            '.....'],
           ['.....',
            '..O..',
            '..O..',
            '..OO.',
            '.....'],
           ['.....',
            '.....',
            '.OOO.',
            '.O...',
            '.....'],
           ['.....',
            '.OO..',
            '..O..',
            '..O..',
            '.....']]

T_SHAPE = [['.....',
            '..O..',
            '.OOO.',
            '.....',
            '.....'],
           ['.....',
            '..O..',
            '..OO.',
            '..O..',
            '.....'],
           ['.....',
            '.....',
            '.OOO.',
            '..O..',
            '.....'],
           ['.....',
            '..O..',
            '.OO..',
            '..O..',
            '.....']]
# 6 shapes implemented
PIECES = {'S': S_SHAPE,
          'Z': Z_SHAPE,
          'I': I_SHAPE,
          'O': O_SHAPE,
          'T': T_SHAPE,
          'L': L_SHAPE}


def calcFallFreq(score):
    fq = 0.5 - (calcLevel(score) * 0.05)
    return fq


def calcLevel(score):  # levels where speed piece drop speedincreases in each level
    level = int(score / 250) + 1
    return level


def gameExit():
    sys.exit()


def onBoard(x, y):
    return x >= 0 and x < BWIDTH and y < BHEIGHT


def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def convToPixel(boxx, boxy):
    return (SideMargin + (boxx * BOXSIZE)), (TopMargin + (boxy * BOXSIZE))


def drawInfo(DisplaySurf, score, BASICFONT, level):
    scoreSurf = BASICFONT.render('Score: %s' % score, True, RED)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WWIDTH - 20, BHEIGHT)
    DisplaySurf.blit(scoreSurf, scoreRect)
    levSurf = BASICFONT.render('Level: %s' % level, True, RED)
    levRect = levSurf.get_rect()
    levRect.topleft = (WWIDTH - 20, BHEIGHT - 20)
    DisplaySurf.blit(levSurf, levRect)


def end(score, DisplaySurf):
    lfont = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf = lfont.render('Score:%s' % score, True, RED)
    TextRect = TextSurf.get_rect()
    TextRect.center = ((WWIDTH / 2), (WHEIGHT / 2))
    DisplaySurf.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)


