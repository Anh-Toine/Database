from typing import Generic, List,TypeVar

V = TypeVar('V')
class DBUtil(Generic[V]):
    def __init__(self) -> None:
        self.resultset: List[V] = []
    
    