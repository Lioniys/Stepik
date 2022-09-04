class Stack:
    def __init__(self) -> None:
        self.top = None
        self.last = None
        pass

    def __add__(self, other):
        """
        Добавление нового
        объекта класса StackObj
        в конец односвязного списка
        """
        self.push_back(other)
        return self

    def __mul__(self, other: list):
        """
        Добавление нескольких объектов
        в конец односвязного списка
        """
        for i in [StackObj(x) for x in other]:
            self.push_back(i)
        return self

    def push_back(self, obj):
        """
        Добавляет элемент
        в конец стека
        """
        if self.top is None:
            self.top = obj
        else:
            self.last.next = obj
        self.last = obj

    def pop_back(self):
        """
        Удаляет последний елемент
        и возвращяет его
        """
        top = self.top
        if top is not None:
            if top.next is None:
                self.top = None
                return self.last
            else:
                while top.next.next is not None:
                    top = top.next
                top.next = None
                return self.last

    def get_data(self):
        """
        Возвращяет список данных
        из всех елементов стека
        """
        lst = []
        top = self.top
        if top is not None:
            while top.next is not None:
                lst.append(top.data)
                top = top.next
            lst.append(top.data)
        return lst


class StackObj:
    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None
        pass

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if isinstance(data, StackObj) or next is None:
            self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj