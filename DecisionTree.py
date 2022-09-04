class DecisionTree:
    """
    Для работы с решающим деревом в целом
    """
    @classmethod
    def predict(cls, root, x):
        """
        Для построения прогноза 
        (прохода по решающему дереву) 
        для вектора x из корневого узла дерева root.
        """
        while root.value is None:
            if x[root.indx] == 1:
                root = root.left
            else:
                root = root.right
        return root.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """
        Для добавления вершин 
        в решающее дерево
        """
        if node is None:
            return obj
        if left:
            node.left = obj
            return obj
        else:
            node.right = obj
            return obj


class TreeObj:
    """
    Описание вершин и листьев решающего дерева
    """
    def __init__(self, indx, value=None):
        """
        indx - проверяемый индекс (целое число);
        value - значение с данными (строка);
        __left - ссылка на следующий объект дерева по левой ветви;
        __right - ссылка на следующий объект дерева по правой ветв.
        """
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self,left):
        self.__left = left

    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self,right):
        self.__right = right