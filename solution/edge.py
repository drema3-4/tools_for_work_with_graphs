class Edge:
    '''Класс ребра графа.
    У каждого ребра есть два конца - две вершины,
    считается, (в случае ориентированного графа) что ребро направлено
    от vertex_1 к vertex_2.
    Так же, в случае взвешенного графа, у ребра есть вес.
    Два ребра считаются одинаковыми, если их vertex_1 и vertex_2 совпадают.'''

    def __init__(self, vertex_1: str, vertex_2: str, weight: int = None):
        '''Конструктор'''
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.weight = weight

    def __str__(self) -> str:
        '''Строковое представление ребра.'''
        return self.vertex_1 + \
               '-' + \
               (('(' + str(self.weight) + ')') if self.weight != None else '') + \
               '-' + \
               self.vertex_2
    
    def __eq__(self, other) -> bool:
        '''Сравнение двух рёбер.
        Два ребра считаются одинаковыми, если их vertex_1 и vertex_2 совпадают.'''
        return self.vertex_1 == other.get_vertex_1() and \
               self.vertex_2 == other.get_vertex_2()

    def __hash__(self) -> int:
        '''Хэш код ребра.'''
        hash = ''

        for i in range(len(self.vertex_1)):
            hash += str(ord(self.vertex_1[i]))

        for i in range(len(self.vertex_2)):
            hash += str(ord(self.vertex_2[i]))

        return eval(hash)

    def set_vertex_1(self, vertex_1: str) -> None:
        '''Сеттер вершины 1.'''
        self.vertex_1 = vertex_1

    def set_vertex_2(self, vertex_2: str) -> None:
        '''Сеттер вершины 2.'''
        self.vertex_2 = vertex_2

    def set_weight(self, weight: int) -> None:
        '''Сеттер веса ребра.'''
        self.weight = weight

    def get_vertex_1(self) -> str:
        '''Геттер вершины 1.'''
        return self.vertex_1
    
    def get_vertex_2(self) -> str:
        '''Геттер вершины 2.'''
        return self.vertex_2
    
    def get_weight(self) -> int:
        '''Геттер веса ребра.'''
        return self.weight