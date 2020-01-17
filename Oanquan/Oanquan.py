class Oanquan():
    def __init__(self):
        # ---------- [q1, d, d, d, d, d, q2, d, d, d, d, d,  p1, p2, t1, t2]+
        # ---------- [0 , 1, 2, 3, 4, 5, 6  ,7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.board = [10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5 , 5 , 0 , 0 , 0 , 0]
        # self.turn = 0

    def __getitem__(self, item):
        return self.board[item]

    def __setitem__(self, key, value):
        self.board[key] = value

    def Move(self, position, direc):
        if self[position] != 0 and position != 0 and position != 6:
            if (direc == 1):
                index = (position + 1) % 12
                while self[position] != 0:
                    self[position] = self[position] - 1
                    self[index] = self[index] + 1
                    index = (index + 1) % 12
                if self[index] == 0:
                    self.checkEat((index - 1 + 12) % 12, direc)
                else:
                    self.Move(index, direc)
            else:
                index = (position - 1) % 12
                while self[position] != 0:
                    self[position] = self[position] - 1
                    self[index] = self[index] + 1
                    index = (index - 1) % 12
                if self[index] == 0:
                    self.checkEat((index + 1 + 12) % 12, direc)
                else:
                    self.Move(index, direc)

    def checkEat(self, position, direc):
        if direc == 1:
            if self[(position + 1) % 12] == 0 and self[(position + 2) % 12] != 0 and ((position + 1) % 12) % 6 != 0:
                self.eat((position + 2) % 12)
                self.checkEat((position + 2) % 12, direc)
        else:
            if self[(position - 1) % 12] == 0 and self[(position - 2) % 12] != 0 and ((position - 1) % 12) % 6 != 0:
                self.eat((position - 2) % 12)
                self.checkEat((position - 2) % 12, direc)

    def eat(self, position):
        if self[14] == 1:
            self[12] = self[12] + self[position]
        if self[15] == 1:
            self[13] = self[13] + self[position]

        self[position] = 0


