from SortMethod import Sort
class BubbleSort(Sort):
    def __init__(self, array: list[int]) -> None:
        self.array: list[int] = array

    def sort(self, index: int) -> None:
        change_color = [index, index + 1]
        if index == len(self.array) - 1:
            index = 0

        if self.array[index] > self.array[index + 1]:
            temp = self.array[index]
            self.array[index] = self.array[index + 1]
            self.array[index + 1] = temp

        index += 1


e = BubbleSort([1,2])
