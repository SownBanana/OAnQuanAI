import numpy as np
# Người chơi 1 là 1 người 2 là -1 mặc định rows[0] lưu điểm vào rows[x][6]
# move 1-5 7-11
from Oanquan.Oanquan import Oanquan


class Board():
    def __init__(self, n=8):
        self.n = n
        # self.turn = 0
        # self.rows[2]=0
        self.rows = [None] * 2
        # [d, d, d, d, d, q, point, turn]
        self.rows[0] = [5, 5, 5, 5, 5, 10, 0, 1]
        self.rows[1] = [5, 5, 5, 5, 5, 10, 0, 0]

    def __getitem__(self, item):
        return self.rows[item]

    def get_legal_moves(self, player):
        moves = set()
        if player == 1:
            y = 0
        if player == -1:
            y = 1
        for x in range(5):
            if self[y][x] != 0:
                newmove = x
                moves.add(newmove)
        for x in range(5):
            if self[y][x] != 0:
                newmove = (x + 5)
                moves.add(newmove)
        return list(moves)

    def has_legal_moves(self):
        if self[0][5] != 0 or self[1][5] != 0:
            return True
        return False

    def is_win(self, player):
        if self[0][5] == 0 and self[1][5] == 0:

            for i in range(5):
                self[0][6] = self[0][6] + self[0][i]
                self[0][i] = 0
                self[1][6] = self[1][6] + self[1][i]
                self[1][i] = 0
            if self[0][6] > self[1][6] and player == 1: return True
            if self[0][6] < self[1][6] and player == -1: return True
        return False

    def to_board(self):
        board = Oanquan()
        # board.turn = self.turn
        board[14] = self[0][7]
        board[15] = self[1][7]
        board[0] = self[0][5]
        board[6] = self[1][5]
        for i in range(5):
            board[i + 1] = self[0][i]
            board[i + 7] = self[1][i]
        board[12] = self[0][6]
        board[13] = self[1][6]
        return board

    def board_to_self(self, board):
        self[0][7] = board[14]
        self[1][7] = board[15]
        self[0][5] = board[0]
        self[1][5] = board[6]
        for i in range(5):
            self[0][i] = board[i + 1]
            self[1][i] = board[i + 7]
        self[0][6] = board[12]
        self[1][6] = board[13]

    def execute_move(self, move, player):
        # turn right of max player
        if (move > 4):
            y = 1
            x = move - 5
        # turn left of max player
        else:
            y = 0
            x = move
        if player == 1:
            x = x + 1
            self[0][7] = 1
            self[1][7] = 0
        if player == -1:
            x = x + 7
            self[0][7] = 0
            self[1][7] = 1
        board = self.to_board()
        board.Move(x, y)
        self.board_to_self(board)
        # self.turn = self.turn + 1
        # if player == 1: self[0][7] = self[0][7] + 1
        # if player == -1: self[1][7] = self[1][7] + 1
        for i in range(2):
            if (self[i][0] + self[i][1] + self[i][2] + self[i][3] + self[i][4]) == 0:
                for j in range(5):
                    self[i][j] = 1
                self[i][6] -= 5

    def display(self):
        print("+------------" + str(self[0][6]) + "---------------+")
        print("|   |%3d|%3d|%3d|%3d|%3d|   |" % (self[0][0], self[0][1], self[0][2], self[0][3], self[0][4]))
        print("|%3d|-------------------|%3d|" % (self[0][5], self[1][5]))
        print("|   |%3d|%3d|%3d|%3d|%3d|   |" % (self[0][0], self[0][1], self[0][2], self[0][3], self[0][4]))
        print("+------------" + str(self[1][6]) + "---------------+")
# b=Board()
# b.execute_move((1,1),1)
#
# print(np.array(b.rows).shape)
