from SortMethod import Sort


class InsertionSort(Sort):
    def __init__(self, array: list[int]) -> None:
        self.array: list[int] = array
        self.index: int = 1
        self.change_color: list[int] = [-1, -1]

        # InsertionSort unique variables
        self.backwards: int = 0

    def sort(self) -> None:
        if self.index == 0:
            self.index = self.backwards

        if self.array[self.index] < self.array[self.index-1]:
            self.swap(self.index, self.index-1)
            self.index -= 1
            self.backwards += 1

        else:
            self.backwards = 0
            self.index += 1

        self.change_color = [self.index, self.index-1]