from abc import ABC, abstractmethod

class Sort(ABC):

    @abstractmethod
    def __init__(self, array: list[int]) -> None:
        self.array: list[int] = array

    @abstractmethod
    def sort(self, index: int) -> list[int]:
        pass