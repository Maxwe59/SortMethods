from SortMethod import Sort


class BubbleSort(Sort):
    def __init__(self, array: list[int]) -> None:
        self.array: list[int] = array
        self.index: int = 0
        self.change_color: list[int] = [-1, -1]

        #bubble sort unique vars (keeps track of indicies at the end of array to skip)
        self.skip_indices: int = 1

    def sort(self) -> None:
        self.change_color = [self.index, self.index + 1]
        if self.index == len(self.array) - self.skip_indices:
            self.skip_indices += 1
            self.index = 0

        if self.array[self.index] > self.array[self.index + 1]:
            self.swap(self.index, self.index+1)

        self.index += 1
