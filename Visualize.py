import pygame
import random
import CustomColor as C
import copy
import time
from SortMethod import Sort
from BubbleSort import BubbleSort

class Graph:
    def __init__(self, num_items: int, low: int, high: int, rect_color: C.Color, select_color: C.Color, check_color: C.Color, resolution: tuple[int, int], window) -> None:
        # Color variables
        self.rect_color: tuple[int,int,int] = rect_color.getColor()
        self.select_color: tuple[int,int,int] = select_color.getColor()
        self.check_color: tuple[int,int,int] = check_color.getColor()

        # Array initialization
        self.num_items: int = num_items
        self.low: int = low #note: bar height is calculated based on ratio of the biggest index and the resolution, do not set ratio of low/high to something too small otherwise some bars might not be visible
        self.high: int = high
        array: list[int] = [random.randint(self.low, self.high) for i in range(self.num_items)]
        self.sort_method: Sort = BubbleSort(array)
        self.sorted_array = copy.deepcopy(array) #create sorted array to check when self.array is fully sorted and stop program
        self.sorted_array.sort()

        # Pygame variables
        self.window = window
        self.resolution: tuple[int, int] = resolution
        self.scale: float = .9 # variable that controls the size of all objects rendered so that all objects are set in ratio to screen resolution

        # global trackers
        self.finish: bool = None #whatever

    def rect_params(self, index: int, curr_size: int) -> tuple[float, float, float, float]: #calculates width, height, x and y of each rectangle
        height: float = self.resolution[1] * (curr_size / max(self.sort_method.array)) - (self.resolution[1] * (1 - self.scale))  # calculates height based on ratio of resolution
        width: float = (self.resolution[0] * self.scale) / self.num_items  # constant
        x: float = (index * width) + ((self.resolution[0] * (1 - self.scale)) / 2) - 5
        y: float = self.resolution[1] - height

        return x,y,width,height

    def render(self) -> None:
        #renders in play button
        keys = pygame.key.get_pressed()
        tri_scale: float = (self.resolution[0] * (1 - self.scale)) / 3
        pygame.draw.polygon(self.window, (255, 0, 0), [(0, tri_scale), (0, 0), (tri_scale, tri_scale / 2)])
        self.__text() #renders text

        #starts sort animation if P key is pressed
        if keys[pygame.K_p]:
            self.finish = False
        if False == self.finish:
            self.sort_method.sort()

        #iterates through the array and renders all values based on ratio of the screen and biggest number
        for index, rectangle in enumerate(self.sort_method.array):
            color: tuple[int,int,int] = (self.select_color if (index in self.sort_method.change_color) else self.rect_color)
            if self.finish:
                color = self.check_color if (self.sort_method.change_color[0] <= index <= self.sort_method.change_color[1]) else self.rect_color
            pygame.draw.rect(self.window, color, self.rect_params(index, rectangle))  # x,y,width,height

        # checks if array is fully sorted:
        self.__sorted()

    def __sorted(self) -> None:
        if self.sort_method.array == self.sorted_array and not self.finish:
            self.finish = True
            self.sort_method.index = 0
            self.sort_method.change_color = [-1, -1] #set to redundant values to keep all bars white

        if self.finish:
            self.sort_method.change_color = [0, self.sort_method.index+1]
            self.sort_method.index += 1

    def __text(self) -> None:
        font = pygame.font.Font(None, int(self.resolution[0]/35))
        text_surface = font.render("P", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.resolution[0]/95, self.resolution[0]/60)
        self.window.blit(text_surface, text_rect)





