import edge.py

class Vertex:
    '''Данный класс отвечает за вершину графа.
    У вершины есть имя (строка).
    Две вершины считаются одинаковыми, если их имена совпадают.'''

    def __init__(self, name: str) -> None:
        '''Конструктор'''
        self.name = name

    def __str__(self) -> str:
        '''Строковое представление вершины.'''
        return self.name
    
    def __hash__(self) -> int:
        '''Хэш вершины'''
        return int(''.join([str(ord(symb)) for symb in self.name]))
    
    def __eq__(self, other) -> bool:
        '''Сравнение вершин.
        Две вершины считаются одинаковыми, если их имена равны.'''
        return self.name == other.get_name()
    
    def get_name(self) -> str:
        '''Возвращает имя вершины'''
        return self.name