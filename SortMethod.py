from abc import ABC, abstractmethod


class Sort(ABC):

    @abstractmethod
    def __init__(self, array: list[int]) -> None:
        self.array: list[int] = array
        self.index: int = 0
        self.change_color: list[int] = [-1, -1]

    @abstractmethod
    def sort(self) -> None:
        pass

    def swap(self, a: int, b: int) -> None:
        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp


