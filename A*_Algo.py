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
    
    def node_draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.x + SIZE, self.y + SIZE))

grid = []

def initialize():
    
    for i in range(ROWS):
        grid.append([])
        for j in range(COLS):
            grid[i].append(Node(i, j))

def generate_obstacle():
    for i in range(ROWS):
        for j in range(COLS):
            n = random.random()
            if n < 0.1:
                grid[i][j].color = BLACK


def start_end():

    start_color = BLUE
    end_color = RED
    start_node = grid[0][0]
    end_node = grid[ROWS-1][COLS-1]

    start_node.color = start_color
    end_node.color = end_color
    return start_node, end_node

def draw_grid(rows, cols, size):
    for i in range(rows):
        pygame.draw.line(screen, GREY, (i*size, 0), (i*size, WIDTH))
        for j in range(cols):
            pygame.draw.line(screen, GREY, (0, j*size), (WIDTH, j*size))


def draw():
    screen.fill(WHITE)
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, WIDTH))
    
    for i in range(ROWS):
        for j in range(COLS):
            grid[i][j].node_draw(screen)
    
    draw_grid(ROWS, COLS, SIZE)

    pygame.display.update()

open_list = []

if __name__ == "__main__":

    initialize()
    generate_obstacle(0.4)
    start_node, end_node = start_end()
    open_list.append(start_node)
    exit = False
    start_node.distance = 0
    while(len(open_list)):
        #print("Heyo!!!")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        draw()