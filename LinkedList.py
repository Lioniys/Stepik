class LinkedList:

    def __init__(self) -> None:
        """
        head - ссылка на первый объект связного списка;
        tail - ссылка на последний объект связного списка.
        """
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """
        добавление нового объекта obj 
        класса ObjList в конец связного списка
        """
        if self.head == None:
            self.head = obj
        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
        self.tail = obj

    def remove_obj_last(self):
        """
        удаление последнего объекта 
        из связного списка
        """
        if self.tail.get_prev() == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_prev()

    def remove_obj(self, indx):
        """
        удаление объекта класса ObjList 
        из связного списка по его порядковому номеру (индексу); 
        индекс отсчитывается с нуля.
        """
        i = 0
        c = self.head
        if indx == 0:
            self.head = None
            self.tail = None
        else:
            while i != indx:
                c = c.get_next()
                i += 1
            if c.get_next() != None:
                c.get_next().set_prev(c.get_prev())
                c.get_prev().set_next(c.get_next())
            else:
                c.get_prev().set_next(None)
                self.tail = c.get_prev()

    def get_data(self):
        """
        получение списка из строк 
        локального свойства __data 
        всех объектов связного списка.
        """
        x = self.head
        l = []
        if self.head != None:
            while x.get_next() != None:
                l.append(x.get_data())
                x = x.get_next()
            l.append(x.get_data())
        return l

    def __len__(self):
        """
        при применении функции len к объекту класса
        возвращает число объектов в связном списке
        """
        return len(self.get_data())

    def __call__(self, indx):
        """
        при вызове объекта класса,возвращает строку __data, 
        хранящуюся в объекте класса ObjList, 
        расположенного под индексом indx (в связном списке).
        """
        return self.get_data()[indx]


class ObjList:

    def __init__(self, data) -> None:
        """
        __next - ссылка на следующий объект связного списка;
        __prev - ссылка на предыдущий объект связного списка;
        __data - строка с данными.
        """
        self.__next = None
        self.__prev = None
        self.__data = data
        pass

    def set_next(self, obj):
        """изменение приватного свойства __next на значение obj;
        """
        self.__next = obj
        pass

    def set_prev(self, obj):
        """изменение приватного свойства __prev на значение obj;
        """
        self.__prev = obj
        pass

    def get_next(self):
        """получение значения приватного свойства __next;
        """
        return self.__next

    def get_prev(self):
        """получение значения приватного свойства __prev;
        """
        return self.__prev

    def set_data(self, data):
        """изменение приватного свойства __data на значение data;
        """
        self.__data = data
        pass

    def get_data(self):
        """получение значения приватного свойства __data.
        """
        return self.__data
