#!/usr/bin/python
from pygame.locals import *
import time
import pygame
import random,sys
from essen import *
from BlockBoard import *

def createBoard():
    board = []
    for i in range(BWIDTH):
        board.append([BLANK] * BHEIGHT)
    return board

class Gameplay(Board,Block):                            #inheritance
    __WWIDTH=800                                        #private member
    __WHEIGHT=800                                       #private member

    def __init__(self):                                 #Constructor
        self.__running=True                             #private member

    def on_init(self):
        pygame.init()
        self.board=createBoard()
        self.CLOCK= pygame.time.Clock()
        self.DisplaySurf=pygame.display.set_mode((self.__WWIDTH,self.__WHEIGHT),pygame.HWSURFACE)
        pygame.display.set_caption('Tetris')
        self._running=True
        self.lastDownTime = time.time()
        self.lastSidewaysTime = time.time()
        self.lastFallTime = time.time()
        self.currentPiece = self.selectPiece()
        self.nextPiece=self.selectPiece()
        self.score = 0
        self.level=calcLevel(self.score)
        self.fallFreq = calcFallFreq(self.score)
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    def on_event(self,event):
        if event.type == QUIT:
            self._running= False

    def on_cleanup(self):
        end(self.score,self.DisplaySurf)
        pygame.quit()

    def on_execute(self):
        if self.on_init()==False:
            self.__running=False
            sys.quit()

        while self.__running:
            if self.currentPiece==None:
                self.currentPiece=self.nextPiece
                self.nextPiece=self.selectPiece()
                self.lastFallTime=time.time()
                if not self.checkPiecePos(self.board, self.currentPiece):
                    end(self.score,self.DisplaySurf)
                    return

            for event in pygame.event.get():
                if event.type==KEYUP:
                    if event.key == K_a:
                        self.movingLeft = False
                    elif event.key == K_d:
                        self.movingRight = False
                    elif event.key == K_SPACE:
                        self.movingDown=False

                elif event.type==KEYDOWN:
                    if event.key==K_a and self.checkPiecePos(self.board, self.currentPiece, adjX=-1):
                        self.currentPiece['x'] -= 1
                        self.moveLeft()
                        self.lastSidewaysTime = time.time()

                    elif event.key==K_s:
                        self.currentPiece['rotation'] = (self.currentPiece['rotation'] + 1) % len(PIECES[self.currentPiece['shape']])
                        if not self.checkPiecePos(self.board, self.currentPiece):
                            self.currentPiece['rotation'] = (self.currentPiece['rotation'] - 1) % len(PIECES[self.currentPiece['shape']])

                    elif event.key==K_SPACE:
                        self.dropDown()
                        for i in range(1, BHEIGHT):
                            if not self.checkPiecePos(self.board, self.currentPiece, adjY=i):
                                break
                        self.currentPiece['y'] += i - 1

                    elif event.key==K_d and self.checkPiecePos(self.board, self.currentPiece, adjX=+1):
                        self.currentPiece['x'] += 1
                        self.moveRight()
                        self.lastSidewaysTime = time.time()

                    if event.key==K_ESCAPE:
                        self.__running=False

            if time.time() - self.lastFallTime > self.fallFreq:
                if not self.checkPiecePos(self.board, self.currentPiece, adjY=1):
                    self.fillPiecePos(self.board, self.currentPiece)
                    self.score += (self.__removeRowFull()*100)+10
                    self.fallFreq = calcFallFreq(self.score)
                    self.level=calcLevel(self.score)
                    self.currentPiece = None
                else:
                    self.currentPiece['y'] += 1
                    self.lastFallTime = time.time()

            self.DisplaySurf.fill(BLACK)
            self.drawBoard(self.DisplaySurf,self.board)
            drawInfo(self.DisplaySurf,self.score,self.BASICFONT,self.level)
            self.drawNextPiece(self.DisplaySurf,self.nextPiece,self.BASICFONT)
            if self.currentPiece != None:
                self.drawPiece(self.DisplaySurf,self.currentPiece)
            pygame.display.update()
            self.CLOCK.tick(FPS)

        self.on_cleanup()

    def __checkRowFull(self, y):                        #private method accessible only through class methods
        for x in range(BWIDTH):
            if self.board[x][y] == BLANK:
                return False
        return True

    def __removeRowFull(self):                          #private method accessible only through class methods
        numLinesRemoved = 0
        y = BHEIGHT - 1
        while y >= 0:
            if self.__checkRowFull(y):
                for pullDownY in range(y, 0, -1):
                    for x in range(BWIDTH):
                        self.board[x][pullDownY] = self.board[x][pullDownY-1]
                for x in range(BWIDTH):
                    self.board[x][0] = BLANK
                numLinesRemoved += 1
            else:
                y -= 1
        return numLinesRemoved

    def selectPiece(self):
        sha = random.choice(list(PIECES.keys()))
        newPiece = {'shape': sha,
                    'rotation': random.randint(0, len(PIECES[sha]) - 1),
                    'x': int(BWIDTH / 2) - int(5 / 2),
                    'y': -2,
                    'color': GRAY}
        return newPiece

if __name__ == '__main__':
    app=Gameplay()
    app.on_execute()
