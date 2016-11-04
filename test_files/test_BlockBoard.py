import random

import BlockBoard
import Game
from essen import *


class Test_Board:
    
    def test_piece1(self):
        board = Game.createBoard()
        x = 0
        y = 0

        sha = random.choice(list(PIECES.keys()))
        newPiece = {'shape': sha,
                    'rotation': random.randint(0, len(PIECES[sha]) - 1),
                    'x': int(BWIDTH / 2) - int(5 / 2),
                    'y': -2,
                    'color': GRAY}
        out = BlockBoard.Board().checkPiecePos(board, newPiece, x, y)
        assert out

    def test_piece2(self):
        board = Game.createBoard()
        for i in range(BWIDTH):
            board[1][i] = GRAY
        sha = random.choice(list(PIECES.keys()))
        newPiece = {'shape': sha,
                    'rotation': random.randint(0, len(PIECES[sha]) - 1),
                    'x': int(BWIDTH / 2) - int(5 / 2),
                    'y': -2,
                    'color': GRAY}
        out = BlockBoard.Board().checkPiecePos(board, newPiece, adjX=2, adjY=0)
        assert out
    
    def test_piece3(self):
        board = Game.createBoard()
        for i in range(BWIDTH):
            board[i][9] = GRAY
        sha = random.choice(list(PIECES.keys()))
        newPiece = {'shape': sha,
                    'rotation': random.randint(0, len(PIECES[sha]) - 1),
                    'x': int(BWIDTH / 2) - int(5 / 2),
                    'y': -2,
                    'color': GRAY}
        out = BlockBoard.Board().checkPiecePos(board, newPiece, adjX=5, adjY=8)
        assert not out

    def test_piece4(self):
        board = Game.createBoard()
        for i in range(BWIDTH):
            board[i][1] = GRAY
        sha = random.choice(list(PIECES.keys()))
        newPiece = {'shape': sha,
                    'rotation': random.randint(0, len(PIECES[sha]) - 1),
                    'x': int(BWIDTH / 2) - int(5 / 2),
                    'y': 2,
                    'color': GRAY}
        out = BlockBoard.Board().checkPiecePos(board, newPiece)
        assert  out

    def test_fillPiece(self):
        board = Game.createBoard()
        sha = random.choice(list(PIECES.keys()))
        newPiece = {'shape': sha,
                    'rotation': random.randint(0, len(PIECES[sha]) - 1),
                    'x': int(BWIDTH / 2) - int(5 / 2),
                    'y': -2,
                    'color': GRAY}
        BlockBoard.Board().fillPiecePos(board, newPiece)
        out = True
        for x in range(5):
            for y in range(5):
                if PIECES[newPiece['shape']][newPiece['rotation']][y][x] != BLANK:
                    if board[x + newPiece['x']][y + newPiece['y']] != GRAY:
                        out = False
        assert out

class Test_Block:
    def test_moveLeft(self):
        bl_obj = BlockBoard.Block()
        bl_obj.moveLeft()
        ans = True
        if not bl_obj.returnleft() and bl_obj.returnright():
            ans = False
        assert ans

    def test_moveRight(self):
        bl_obj = BlockBoard.Block()
        bl_obj.moveRight()
        ans = True
        if not bl_obj.returnright() and bl_obj.returnleft():
            ans = False
        assert ans

    def test_dropDown(self):
        bl_obj = BlockBoard.Block()
        bl_obj.dropDown()
        ans = False
        if not bl_obj.returnright() and not bl_obj.returnleft() and not bl_obj.returndown():
            ans = True
        assert ans
