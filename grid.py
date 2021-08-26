import math
import pygame
import random

WIDTH = 800

SIZE = 20
ROWS = WIDTH//SIZE
COLS = WIDTH//SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)




screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Path Finder')


class Node():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col*SIZE
        self.y = row*SIZE
        self.color = WHITE
        self.distance = float('inf')
        self.prev : Node = None
        self.visited = False


def draw_grid(rows, cols, size):
    for i in range(rows):
        pygame.draw.line(screen, GREY, (i*size, 0), (i*size, WIDTH))
        for j in range(cols):
            pygame.draw.line(screen, GREY, (0, j*size), (WIDTH, j*size))


def draw():
    screen.fill(WHITE)
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, WIDTH))

    
    draw_grid(ROWS, COLS, SIZE)

    pygame.display.update()



while(True):
    draw()
