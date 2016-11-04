from essen import *
from pygame.locals import *
import pygame


class Block:

    def __init__(self):  # constructor
        self.movingLeft = False
        self.movingRight = False
        self.movingDown = False
        pass

    def moveLeft(self):
        self.movingLeft = True
        self.movingRight = False

    def returnleft(self):
        return self.movingLeft

    def moveRight(self):
        self.movingRight = True
        self.movingLeft = False

    def returnright(self):
        return self.movingRight

    def dropDown(self):
        self.movingLeft = False
        self.movingRight = False
        self.movingDown = False

    def returndown(self):
        return self.movingDown

    def __drawBox(self, DisplaySurf, x, y, color, pixelx=None, pixely=None):  # private method
        if color == BLANK:
            return
        if pixelx == None and pixely == None:
            pixelx, pixely = convToPixel(x, y)
        pygame.draw.rect(DisplaySurf, GRAY,
                         (pixelx, pixely, BOXSIZE - 1, BOXSIZE - 1))
        pygame.draw.rect(DisplaySurf, BLUE, (pixelx + 1,
                                             pixely + 1, BOXSIZE - 5, BOXSIZE - 5))

    def drawBoard(self, DisplaySurf, board):
        pygame.draw.rect(DisplaySurf, WHITE, (SideMargin - 3, TopMargin - 7,
                                              (BWIDTH * BOXSIZE) + 8, (BHEIGHT * BOXSIZE) + 8), 5)
        pygame.draw.rect(DisplaySurf, BLACK, (SideMargin,
                                              TopMargin, BOXSIZE * BWIDTH, BOXSIZE * BHEIGHT))
        for x in range(BWIDTH):
            for y in range(BHEIGHT):
                self.__drawBox(DisplaySurf, x, y, board[x][y])

    def drawPiece(self, DisplaySurf, piece, pixelx=None, pixely=None):
        shape = PIECES[piece['shape']][piece['rotation']]
        if pixelx == None and pixely == None:
            pixelx, pixely = convToPixel(piece['x'], piece['y'])
        for x in range(TEMPWIDTH):
            for y in range(TEMPHEIGHT):
                if shape[y][x] != BLANK:
                    self.__drawBox(DisplaySurf, None, None, GRAY,
                                   pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))

    def drawNextPiece(self, DisplaySurf, piece, BASICFONT):
        nextSurf = BASICFONT.render('Next:', True, RED)
        nextRect = nextSurf.get_rect()
        nextRect.topleft = (WWIDTH - 20, 80)
        DisplaySurf.blit(nextSurf, nextRect)
        self.drawPiece(DisplaySurf, piece, pixelx=WWIDTH - 20, pixely=100)


class Board:

    def checkPiecePos(self, board, piece, adjX=0, adjY=0):
        for x in range(5):
            for y in range(5):
                isAbove = y + piece['y'] + adjY < 0
                if isAbove or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                    continue
                if not onBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                    return False
                if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                    return False
        return True

    def fillPiecePos(self, board, piece):
        for x in range(5):
            for y in range(5):
                if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                    board[x + piece['x']][y + piece['y']] = GRAY
