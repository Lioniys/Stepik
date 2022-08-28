from random import randint

# Сапер
class Cell:
    def __init__(self, around_mines=0, mine=False) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False
        pass


class GamePole:
    def __init__(self, N, M) -> None:
        self.n = N
        self.m = M
        self.pole = [[Cell() for x in range(self.n)] for y in range(self.n)]
        self.init()
        self.counter()
        pass

    def init(self):
        m = 0
        while m < self.m:
            x = randint(0, self.n-1)
            y = randint(0, self.n-1)
            if self.pole[x][y].mine:
                continue
            else:
                self.pole[x][y].mine = True
            m += 1

    def counter(self):
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.n):
            for y in range(self.n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x+i][y+j].mine for i, j in indx if 0 <= x+i < self.n and 0 <= y+j < self.n))
                    self.pole[x][y].around_mines = mines

    def show(self):
        for x in self.pole:
            print(*map(lambda x: "#" if not x.fl_open else x.around_mines if not x.mine else "*", x))


pole_game = GamePole(10, 12)
pole_game.show()