import edge.py

class Vertex:

    def __init__(self, name: str) -> None:
        self.name = name

    def __init__(self, name: str, edges: set[Edge]) -> None:
        self.name = name
        self.edges = edges

    def __eq__(self, other) -> bool:
        return self.name == other.get_name()

    def __hash__(self) -> int:
        return ord(self.name)
    
    def __str__(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def add_edge(self, edge: Edge) -> None:
        self.edges.add(edge)

    def del_edge(self, name: str) -> None:
        

    def get_name(self) -> str:
        return self.name
    
    def get_edges(self) -> set[Edge]:
        return self.edges