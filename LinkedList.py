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
            obj.prev = self.tail
            self.tail.next = obj
        self.tail = obj

    def remove_obj_last(self):
        """
        удаление последнего объекта 
        из связного списка
        """
        if self.tail.prev == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev

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
                c = c.next
                i += 1
            if c.next != None:
                c.next.prev = c.prev
                c.prev.next = c.next
            else:
                c.prev.next = None
                self.tail = c.prev

    def get_data(self):
        """
        получение списка из строк 
        локального свойства __data 
        всех объектов связного списка.
        """
        x = self.head
        lst = []
        if self.head != None:
            while x.next != None:
                lst.append(x.data)
                x = x.next
            lst.append(x.data)
        return lst

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


class Descriptor:
    def __set_name__(self, owner, name):
        """
        Метод автоматически вызывается когда создается экземпляр класса
        self - ссылка на экземпляр класса, owner - ссылка на класс ObjList
        """
        self.name = '_' + name

    def __get__(self, instance, owner):
        """
        self - ссылка на экземпляр класса
        instance - ссылка на экзампляр класса из которого был вызван
        owner - ссылка на класс ObjList
        """
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """
        Срабатывает в момент присваивания из инициализатора
        self - ссылка на экземпляр класса
        instance - ссылка на экзампляр класса из которого был вызван
        value - значение которое будет присвоено
        """
        instance.__dict__[self.name] = value


class ObjList:
    next = Descriptor()
    prev = Descriptor()
    data = Descriptor()

    def __init__(self, data) -> None:
        """
        next - ссылка на следующий объект связного списка;
        prev - ссылка на предыдущий объект связного списка;
        data - строка с данными.
        """
        self.next = None
        self.prev = None
        self.data = data