#!/usr/bin/python
import Game
from essen import *


class Test_Game:
    def test_select(self):
        piece = Game.Gameplay().selectPiece()
        out = False
        if piece['y'] == -2 and piece['color'] == GRAY:
            out = True
        assert out

    def test_rowFull(self):
        board = []
        for i in range(BWIDTH):
            board.append([BLANK] * BHEIGHT)

        for i in range(BWIDTH):
            board[i][9] = GRAY
        gameplay = Game.Gameplay()
        gameplay.setmyvar(board)
        out = gameplay.getval(board, 9)
        assert out

    def test_removePiece(self):
        board = []
        for i in range(BWIDTH):
            board.append([BLANK] * BHEIGHT)

        for i in range(BWIDTH):
            board[i][9] = GRAY
        for i in range(BWIDTH):
            board[i][7] = GRAY
        gameplay = Game.Gameplay()
        gameplay.setmyvar(board)
        ans = gameplay.getans()
        assert ans == 2

    def test_createBoard(self):
        board = Game.createBoard()
        out = True
        for i in range(BWIDTH):
            for j in range(BHEIGHT):
                if board[i][j] != '.':
                    out = False
        assert out
