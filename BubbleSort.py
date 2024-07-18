from SortMethod import Sort


class BubbleSort(Sort):
    def __init__(self, array: list[int]) -> None:
        self.array: list[int] = array
        self.index: int = 0
        self.change_color: list[int] = [-1, -1]

    def sort(self) -> None:
        self.change_color = [self.index, self.index + 1]
        if self.index == len(self.array) - 1:
            self.index = 0

        if self.array[self.index] > self.array[self.index + 1]:
            temp = self.array[self.index]
            self.array[self.index] = self.array[self.index + 1]
            self.array[self.index + 1] = temp

        self.index += 1
