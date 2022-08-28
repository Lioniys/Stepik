#односвязный список
class StackObj:
    def __init__(self,data) -> None:
        self.__data = data
        self.__next = None
        pass

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        if isinstance(data,StackObj) or next == None:
            self.__data = data

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self,next):
        if isinstance(next,StackObj) or next == None:
            self.__next = next


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.last = None
        pass

    def push(self, obj):
        if self.top == None:
            self.top = obj
        else:
            self.last.next = obj
        self.last = obj
        pass

    def pop(self):
        i = self.top
        if i != None:
            if i.next == None:
                self.top = None
                return self.last
            else:
                while i.next.next != None:
                    i = i.next
                i.next = None
                return self.last  

    def get_data(self):
        l = []
        x = self.top
        if x != None:
            while x.next != None:
                l.append(x.data)
                x = x.next
            l.append(x.data)
        return l