from random import randint


class GamePole:
    """
    Управление игровым полем,
    размером N x M клеток
    """
    __singleton = None

    def __new__(cls, *args, **kwargs):
        """
        Создание только одного
        объекта класса GamePole
        паттерн Singleton
        """
        if cls.__singleton is None:
            cls.__singleton = super().__new__(cls)
        return cls.__singleton

    def __del__(self):
        GamePole.__singleton = None

    def __init__(self, N, M, total_mines):
        """
        N x M - размер поля;
        total_mines - общее число мин на поле.
        каждая клетка представляется объектом класса Cell
        и все объекты хранятся в двумерном списке N x M элементов
        """
        self.n = N
        self.m = M
        self.total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(self.m)) for _ in range(self.n))

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        """
        Инициализация поля
        с новой расстановкой мин
        """
        m = 0
        while m < self.total_mines:
            x = randint(0, self.n - 1)
            y = randint(0, self.m - 1)
            if self.pole[x][y].is_mine:
                continue
            else:
                self.pole[x][y].is_mine = True
            m += 1
        self.counter()

    def counter(self):
        """
        Подсчет мин вокруг клетки
        """
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.n):
            for y in range(self.m):
                if not self.pole[x][y].is_mine:
                    mines = sum((self.pole[x + i][y + j].is_mine for i, j in indx
                                 if 0 <= x + i < self.n and 0 <= y + j < self.m))
                    self.pole[x][y].number = mines

    def show_pole(self):
        """
        Отображение поля в консоли
        в виде таблицы чисел открытых клеток
        """
        for x in self.pole:
            print(*map(lambda x: "#" if not x.is_open else x.number if not x.is_mine else "*", x))

    def open_cell(self, i, j):
        """
        Открывает ячейку
        """
        self.pole[i][j].is_open = True


class Descriptor:
    def __set_name__(self, owner, name):
        """
        Метод автоматически вызывается когда создается экземпляр класса
        self - ссылка на экземпляр класса, owner - ссылка на класс Cell
        """
        self.name = '_' + name

    def __get__(self, instance, owner):
        """
        self - ссылка на экземпляр класса
        instance - ссылка на экзампляр класса из которого был вызван
        owner - ссылка на класс Cell
        """
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """
        Срабатывает в момент присваивания из инициализатора
        self - ссылка на экземпляр класса
        instance - ссылка на экзампляр класса из которого был вызван
        value - значение которое будет присвоено
        """
        if value not in [True, False] + list(range(0, 9)):
            raise ValueError("недопустимое значение атрибута")
        instance.__dict__[self.name] = value


class Cell:
    """
    Представление клетки игрового поля
    """
    is_mine = Descriptor()
    number = Descriptor()
    is_open = Descriptor()

    def __init__(self):
        """
        __is_mine - булево значение True/False;
        __number - число мин вокруг клетки;
        __is_open - флаг того, открыта клетка или закрыта.
        """
        self.is_mine = False
        self.number = 0
        self.is_open = False

    def __bool__(self):
        """
        Возвращает True, если клетка закрыта
        и False - если открыта
        """
        return not self.is_open
