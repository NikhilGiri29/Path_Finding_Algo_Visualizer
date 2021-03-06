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

def is_safe_node(row , col):
    if (row >=0 and col  >=0  and row < ROWS and col < COLS):
        if grid[row][col].color != BLACK:
            return True
    return False

def add_neighbour_node(row, col):
    array = []
    ##check right
    if (is_safe_node(row, col+1)):
        array.append(grid[row][col+1])
    
    ##check down
    if (is_safe_node(row +1, col)):
        array.append(grid[row+1][col])

    ##check left
    if (is_safe_node(row, col-1)):
        array.append(grid[row][col-1])
    
    ##check up
    if (is_safe_node(row -1, col)):
        array.append(grid[row-1][col])
    
    return array

def heuristic(alpha : Node, end_node : Node):
    x = abs(alpha.x - end_node.x)
    y = abs(alpha.y - end_node.y)
    return alpha.distance * (x + y)

if __name__ == "__main__":

    initialize()
    generate_obstacle()
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
        
        current_node = open_list[0]
        current_index = 0
        
        for node in open_list:
            if heuristic(node, end_node) < heuristic(current_node, end_node):
                current_node = node
                current_index = open_list.index(node)

        if (current_node.y == end_node.y and current_node.x == end_node.x):
            exit = True
            print("Path Found")
            break

        
        
        #print("Kayo",current_node.row, current_node.col)
        #print(add_neighbour_node(current_node.row, current_node.col))
        for next_node in add_neighbour_node(current_node.row, current_node.col):
            #print("Loop enter!!!")
            if current_node.distance + 1 < next_node.distance:
                grid[next_node.row][next_node.col].distance = current_node.distance + 1
                next_node.distance = current_node.distance + 1
                open_list.append(next_node)

                grid[next_node.row][next_node.col].prev = current_node
                next_node.open_node()
        
        open_list.pop(current_index)
        current_node.close_node()
        current_node.visited = True
        start_end()
        