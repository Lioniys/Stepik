from random import randint

class GamePole:
    """
    Управление игровым полем, 
    размером N x N клеток
    """
    def __init__(self, N, M):
        """
        N - размер поля; 
        M - общее число мин на поле.
        каждая клетка представляется объектом класса Cell 
        и все объекты хранятся в двумерном списке N x N элементов
        """
        self.n = N
        self.m = M
        self.pole = [[Cell() for x in range(self.n)] for y in range(self.n)]
        self.init()
        self.counter()
        
    def init(self):
        """
        Инициализация поля 
        с новой расстановкой M мин
        """
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
        """
        Подсчет мин вокруг клетки
        """
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.n):
            for y in range(self.n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x+i][y+j].mine for i, j in indx if 0 <= x+i < self.n and 0 <= y+j < self.n))
                    self.pole[x][y].around_mines = mines

    def show(self):
        """
        Отображение поля в консоли 
        в виде таблицы чисел открытых клеток
        """
        for x in self.pole:
            print(*map(lambda x: "#" if not x.fl_open else x.around_mines if not x.mine else "*", x))


class Cell:
    """
    Представление клетки игрового поля
    """
    def __init__(self, around_mines=0, mine=False):
        """
        around_mines - число мин вокруг клетки;
        mine - наличие мины в текущей клетке;
        fl_open - открыта/закрыта клетка.
        """
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False