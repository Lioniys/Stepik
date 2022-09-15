from random import randint


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return True if not self.value else False


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

    def __bool__(self):
        return not any((self.is_draw, self.is_human_win, self.is_computer_win))

    @staticmethod
    def valid_indx(item):
        if type(item[0]) != int or not 0 <= item[0] <= 2 or type(item[1]) != int or not 0 <= item[1] <= 2:
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.valid_indx(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.valid_indx(key)
        self.pole[key[0]][key[1]].value = value
        self.valid_win()

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

    def show(self):
        for x in self.pole:
            for y in x:
                print(y.value, end=" ")
            print()


    def human_go(self):
        self.go_in_free_cell(self.HUMAN_X)
        self.valid_win()

    def computer_go(self):
        self.go_in_free_cell(self.COMPUTER_O)
        self.valid_win()

    def go_in_free_cell(self, use):
        s = 0
        while s != 1:
            x = randint(0, 2)
            y = randint(0, 2)
            if not self.pole[y][x]:
                continue
            self.pole[y][x].value = use
            s += 1

    def valid_win(self):
        for row in self.pole:
            if all(x.value == self.HUMAN_X for x in row):
                self.is_human_win = True
                return
            if all(x.value == self.COMPUTER_O for x in row):
                self.is_computer_win = True
                return
        for i in range(3):
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)):
                self.is_human_win = True
                return
            if all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)):
                self.is_computer_win = True
                return
        if all(self.pole[i][i].value == self.HUMAN_X for i in range(3)) or \
                all(self.pole[i][-1 - i].value == self.HUMAN_X for i in range(3)):
            self.is_human_win = True
            return
        if all(self.pole[i][i].value == self.COMPUTER_O for i in range(3)) or \
                all(self.pole[i][-1 - i].value == self.COMPUTER_O for i in range(3)):
            self.is_computer_win = True
            return
        if all(x.value != self.FREE_CELL for row in self.pole for x in row):
            self.is_draw = True
