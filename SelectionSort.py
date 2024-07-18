from SortMethod import Sort

class SelectionSort(Sort):
    def __init__(self, array: list[int]) -> None:
        self.array: list[int] = array
        self.index: int = 0
        self.change_color: list[int] = [-1, -1]

        #selection sort unique variables (both measuring in index, not value)
        self.curr_min: int = 0
        self.skip_indices: int = 0

    def sort(self) -> None:
        if self.array[self.curr_min] > self.array[self.index]:
            # when a new current min is met:
            self.curr_min = self.index

        if self.index == len(self.array) - 1:
            # when reaches end of list
            temp = self.array[self.skip_indices]
            self.array[self.skip_indices] = self.array[self.curr_min]
            self.array[self.curr_min] = temp
            self.skip_indices += 1
            self.curr_min, self.index = self.skip_indices, self.skip_indices

        self.change_color = [self.curr_min, self.index]
        self.index += 1






