#2.2 подвиг 8 Решающее дерево
class TreeObj:
    def __init__(self, indx, value=None):
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


class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        while root.value == None:
            if x[root.indx] == 1:
                root = root.left
            else:
                root = root.right
        return root.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node == None:
            return obj
        if left:
            node.left = obj
            return obj
        else:
            node.right = obj
            return obj
