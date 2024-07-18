#Sort Methods:
#Selection, Bubble, Insertion, Shell


# imports
import pygame
from Visualize import Graph
from CustomColor import Color
from BubbleSort import BubbleSort

# setup/global variables
pygame.init()
RESOLUTION_X = 1920
RESOLUTION_Y = 1080
window = pygame.display.set_mode((RESOLUTION_X, RESOLUTION_Y))
pygame.display.set_caption("Sort Graph")
FPS = 150
clock = pygame.time.Clock()


# main game loop

def main():
    white: Color = Color(255,255,255)
    red: Color = Color(255,0,0)
    green: Color = Color(0,255,0)
    new = Graph(500,100,1000, white, red, green,(RESOLUTION_X, RESOLUTION_Y), window)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill("black")

        new.render()
        pygame.display.update()

    pygame.quit()



main()
