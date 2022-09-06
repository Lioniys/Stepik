class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        """
        step - шаг смещения окна по горизонтали и вертикали;
        size - размер окна по горизонтали и вертикали.
        """
        self.step = step
        self.size = size

    @staticmethod
    def valid(matrix):
        s = len(matrix[0])
        for lst in matrix:
            if len(lst) != s:
                raise ValueError("Неверный формат для первого параметра matrix.")
            for i in lst:
                if type(i) not in (int, float):
                    raise ValueError("Неверный формат для первого параметра matrix.")

    def max_pooling(self, matrix):
        """
        Сканирование прямоугольной матрицы
        окном определенного размера
        (size) и выбора наибольшего значения
        в пределах этого окна
        если окна выходят за пределы матрицы,
        то они пропускаются.
        должна создаваться новая таблица
        из результатов сканирования.
        """
        counter = 0
        result = []
        for x in range(0, len(matrix), self.step[1]):
            counter += 1
            for y in range(0, len(matrix[0]), self.step[0]):
                try:
                    result.append(max(matrix[x][y:y + self.size[0]] + matrix[x + self.size[1]-1][y:y + self.size[0]]))
                except IndexError:
                    continue
        finich = []
        for i in range(0, len(result), counter):
            finich.append(result[i:i + int(len(result) / counter)])
        return finich

    def __call__(self, matrix):
        MaxPooling.valid(matrix)
        return self.max_pooling(matrix)