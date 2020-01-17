from __future__ import print_function
from Oanquan.Logic import Board
import numpy as np

import sys

sys.path.append('..')
from Game import Game


class OanquanGame(Game):
    def __init__(self, n=8):
        self.n = n

    def getInitBoard(self):
        b = Board(self.n)
        return np.array(b.rows)

    def getBoardSize(self):
        return (2, 8)

    def getActionSize(self):
        return 10

    def getNextState(self, board, player, action):
        b = Board(self.n)
        b.rows = np.copy(board)
        move = action
        b.execute_move(move, player)
        return (b.rows, -player)

    def getValidMoves(self, board, player):
        vailds = [0] * self.getActionSize()
        b = Board(self.n)
        b.rows = np.copy(board)
        legalMoves = b.get_legal_moves(player)

        for x in legalMoves:
            vailds[x] = 1
        return np.array(vailds)

    def getGameEnded(self, board, player):
        b = Board(self.n)
        b.rows = np.copy(board)
        if b.is_win(player): return 1
        if b.is_win(-player): return -1
        if b.has_legal_moves(): return 0
        return 1e-4

    def getCanonicalForm(self, board, player):
        if player == 1: return board
        if player == -1:
            b = Board(self.n)
            b.rows = np.copy(board)
            b.rows = np.flip(b.rows, 0)
            return b.rows

    def getSymmetries(self, board, pi):
        pi_board = np.reshape(pi[:-1], (2, 5))
        l = []
        l += [(board, list(pi.ravel()) + [pi[-1]])]
        # k dùng
        return l

    def stringRepresentation(self, board):
        return board.tostring()

    # def display(self):
    #     b = Board(self.n)
    #     b.display()

    @staticmethod
    def display(board):
        s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        s[0] = board[0][5]
        s[6] = board[1][5]
        for i in range(5):
            s[i + 1] = board[0][i]
            s[i + 7] = board[1][i]
        s[12] = board[0][6]
        s[13] = board[1][6]
        print("+---------%3d-----------+" % s[12])
        print("|   |%3d|%3d|%3d|%3d|%3d|   |" % (s[1], s[2], s[3], s[4], s[5]))
        print("|%3d|-------------------|%3d|" % (s[0], s[6]))
        print("|   |%3d|%3d|%3d|%3d|%3d|   |" % (s[11], s[10], s[9], s[8], s[7]))
        print("+--------%3d-----------+" % s[13])
