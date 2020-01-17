import numpy as np


class RandomPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        a = np.random.randint(self.game.getActionSize())
        valids = self.game.getValidMoves(board, 1)
        while valids[a] != 1:
            a = np.random.randint(self.game.getActionSize())
        return a


class HumanPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valids = self.game.getValidMoves(board, 1)
        while True:
            a = int(input('Nhập nước bạn đi'))
            if valids[a]:
                break
            else:
                print('Invalid')
        return a


class MinimaxPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, Board):
        key = -1
        bem = -99999999
        board = self.to_board(Board)
        print(Board)
        print(board)
        for i in range(7, 12):
            for j in range(0, 2):
                if board[i] != 0:
                    cpboard = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 1, 1]
                    for k in range(14):
                        cpboard[k] = board[k]
                    self.Move(i, j, cpboard)
                    mov = self.minimax(cpboard, 0, 1)

                    if mov > bem:
                        bem = mov
                        key = i + j * 100
        return key

    def to_board(self, board):
        Board = [10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 0, 0, 0, 0]
        # board.turn = self.turn
        Board[14] = board[0][7]
        Board[15] = board[1][7]
        Board[0] = board[0][5]
        Board[6] = board[1][5]
        for i in range(5):
            Board[i + 1] = board[0][i]
            Board[i + 7] = board[1][i]
        Board[12] = board[0][6]
        Board[13] = board[1][6]
        return Board

    def checkWin(self, board):
        global point1, point2
        p1 = 0
        p2 = 0
        point1 = board[12]
        point2 = board[13]
        if board[0] == 0 and board[6] == 0:
            p1 = point1 + board[1] + board[2] + board[3] + board[4] + board[5]
            p2 = point2 + board[7] + board[8] + board[9] + board[10] + board[11]
            if p1 > p2:
                return 1
            if p1 == p2:
                return 2
            else:
                return 0
        else:
            return 3

    def checkEat(self, position, direc, board):
        if direc == 1:
            if board[(position + 1) % 12] == 0 and board[(position + 2) % 12] != 0 and ((position + 1) % 12) % 6 != 0:
                self.eat((position + 2) % 12, board)
                self.checkEat((position + 2) % 12, direc, board)
        else:
            if board[(position - 1) % 12] == 0 and board[(position - 2) % 12] != 0 and ((position - 1) % 12) % 6 != 0:
                self.eat((position - 2) % 12, board)
                self.checkEat((position - 2) % 12, direc, board)

    def eat(self, position, board):
        global point1, point2
        if self[14] == 1:
            board[12] = board[12] + board[position]
        else:
            board[13] = board[13] + board[position]

        board[position] = 0

    def Move(self, position, direc, board):
        if board[position] != 0 and position != 0 and position != 6:
            if direc == 1:
                index = (position + 1) % 12
                while board[position] != 0:
                    board[position] = board[position] - 1
                    board[index] = board[index] + 1
                    index = (index + 1) % 12
                if board[index] == 0:
                    self.checkEat((index - 1 + 12) % 12, direc, board)
                else:
                    self.Move(index, direc, board)
            else:
                index = (position - 1) % 12
                while board[position] != 0:
                    board[position] = board[position] - 1
                    board[index] = board[index] + 1
                    index = (index - 1) % 12
                if board[index] == 0:
                    self.checkEat((index + 1 + 12) % 12, direc, board)
                else:
                    self.Move(index, direc, board)

    def minimax(self, board, depth, turn):
        if self.checkWin(board) == 1: return -9999
        if self.checkWin(board) == 0: return 9999
        if self.checkWin(board) == 2: return 0
        if depth == 5:
            return board[13] - board[12]
        if turn == 0:
            best = -1000
            for i in range(7, 12):
                for j in range(0, 2):
                    if (board[i] != 0):
                        cpboard = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 1, 1]
                        for k in range(14):
                            cpboard[k] = board[k]
                        self.Move(i, j, cpboard)
                        vl = self.minimax(cpboard, depth + 1, (turn + 1) % 2)
                        if vl > best:
                            best = vl
            return best
        else:
            best = 1000
            for i in range(1, 6):
                for j in range(0, 2):
                    if (board[i] != 0):
                        cpboard = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 1, 1]
                        for k in range(14):
                            cpboard[k] = board[k]
                        self.Move(i, j, cpboard)
                        vl = self.minimax(cpboard, depth + 1, (turn + 1) % 2)
                        if vl < best:
                            best = vl
            return best
