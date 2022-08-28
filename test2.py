class LinkedList:
    """объявите класс LinkedList, который будет представлять связный список в целом 
    и иметь набор следующих методов:
    И локальные публичные атрибуты:
    head - ссылка на первый объект связного списка (если список пустой, то head = None);
    tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        pass

    def add_obj(self, obj):
        """добавление нового объекта obj класса ObjList в конец связного списка;
        """
        if self.head == None:
            self.head = obj
        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
        self.tail = obj
        pass

    def remove_obj(self):
        """удаление последнего объекта из связного списка;
        """
        if self.tail.get_prev() == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_prev()
        pass

    def get_data(self):
        """получение списка из строк локального свойства __data всех объектов связного списка.
        """
        x = self.head
        l = []
        if self.head != None:
            while x.get_next() != None:
                l.append(x.get_data())
                x = x.get_next()
            l.append(x.get_data())
        return l
        


class ObjList:
    """Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
    __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
    __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
    __data - строка с данными.
    Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
    """
    def __init__(self,data) -> None:
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
    