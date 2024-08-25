class Edge:

    def __init__(self, vertex_1: str, vertex_2: str, weight: int = None):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.weight = weight

    def __str__(self) -> str:
        return self.vertex_1 + \
               '-' + \
               (('(' + str(self.weight) + ')') if self.weight != None else '') + \
               '-' + \
               self.vertex_2
    
    def __eq__(self, other) -> bool:
        return self.vertex_1 == other.get_vertex_1() and \
               self.vertex_2 == other.get_vertex_2()

    def __hash__(self) -> int:
        hash = ''

        for i in range(len(self.vertex_1)):
            hash += str(ord(self.vertex_1[i]))

        for i in range(len(self.vertex_2)):
            hash += str(ord(self.vertex_2[i]))

        return eval(hash)

    def set_vertex_1(self, vertex_1: str) -> None:
        self.vertex_1 = vertex_1

    def set_vertex_2(self, vertex_2: str) -> None:
        self.vertex_2 = vertex_2

    def set_weight(self, weight: int) -> None:
        self.weight = weight

    def get_vertex_1(self) -> str:
        return self.vertex_1
    
    def get_vertex_2(self) -> str:
        return self.vertex_2
    
    def get_weight(self) -> int:
        return self.weight