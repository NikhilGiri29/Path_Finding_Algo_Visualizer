import math
import pygame
import random

WIDTH = 500


SIZE = 20
ROWS = WIDTH//SIZE
COLS = WIDTH//SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)

SPACE = 100
PAD = SPACE//2


screen = pygame.display.set_mode((WIDTH + SPACE, WIDTH + SPACE))
pygame.display.set_caption('Path Finder')
screen.fill(GREY)
class Node():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = (col*SIZE)  +PAD
        self.y = (row*SIZE)  +PAD
        self.color = WHITE
        self.distance = float('inf')
        self.prev : Node = None
        self.visited = False
    
    def node_draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y,SIZE,SIZE))

    def open_node(self):
        self.color = GREEN
    
    def close_node(self):
        self.color = ORANGE

    def final_node(self):
        self.color = YELLOW


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

    start_node.distance = 0
    start_node.color = start_color
    end_node.color = end_color
    return start_node, end_node


def draw_grid(rows, cols, size):

    for i in range(rows):
        pygame.draw.line(screen, GREY, ((i*size + PAD), PAD), ((i*size) + PAD, WIDTH + PAD))
    for j in range(cols):
        pygame.draw.line(screen, GREY, (PAD, (j*size) + PAD), (WIDTH + PAD, (j*size) + PAD))

def draw():
    #screen.fill(WHITE)
    pygame.draw.rect(screen, WHITE, (PAD, PAD, WIDTH , WIDTH ))
    
    for i in range(ROWS):
        for j in range(COLS):
            grid[i][j].node_draw(screen)
    start_end()
    draw_grid(ROWS, COLS, SIZE)

    pygame.display.update()


open_list= []


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


def update_open_list(current_node, current_index):

    for next_node in add_neighbour_node(current_node.row, current_node.col):
            
            if current_node.distance + 1 < next_node.distance:
                grid[next_node.row][next_node.col].distance = current_node.distance + 1
                next_node.distance = current_node.distance + 1
                open_list.append(next_node)

                grid[next_node.row][next_node.col].prev = current_node
                next_node.open_node()
    
    open_list.pop(current_index)
    current_node.close_node()
    current_node.visited = True

    return open_list

def A_Star(open_list, end_node):
    current_node = open_list[0]
    current_index = 0
    exit = False
    for node in open_list:
        if heuristic(node, end_node) < heuristic(current_node, end_node):
            current_node = node
            current_index = open_list.index(node)
    
    if (current_node.y == end_node.y and current_node.x == end_node.x):
            exit = True
            print("Path Found")
    
    open_list = update_open_list(current_node, current_index)
    return current_node, current_index ,open_list ,exit
    

def Dijkstra(open_list, end_node):
    current_node = open_list[0]
    current_index = 0
    exit = False
    for node in open_list:
        if node.distance < current_node.distance:
            current_node = node
            current_index = open_list.index(node)
    
    if (current_node.y == end_node.y and current_node.x == end_node.x):
            exit = True
            print("Path Found")
    
    open_list = update_open_list(current_node, current_index)
    return current_node, current_index ,open_list ,exit

def BFS(open_list, end_node):
    current_node = open_list[0]
    current_index = 0
    exit = False

    if (current_node.y == end_node.y and current_node.x == end_node.x):
            exit = True
            print("Path Found")
    
    open_list = update_open_list(current_node, current_index)
    return current_node, current_index ,open_list ,exit


def DFS(open_list, end_node):
    current_node = open_list[-1]
    current_index = len(open_list) -1 # Lifo Logic
    exit = False

    if (current_node.y == end_node.y and current_node.x == end_node.x):
            exit = True
            print("Path Found")
    
    open_list = update_open_list(current_node, current_index)
    return current_node, current_index ,open_list ,exit


def plot_path():
    start_node, end_node = start_end()
    pointer = end_node
    while (pointer.row != start_node.row) or  (pointer.col != start_node.col):
        pointer = pointer.prev
        pathFound.append(pointer)
        pointer.final_node()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()

if __name__ == "__main__":

    initialize()
    generate_obstacle()
    start_node, end_node = start_end()
    open_list.append(start_node)
    exit = False
    
    while(len(open_list)):

        draw()
        current_node, current_index, open_list, exit = A_Star(open_list, end_node)

        if exit :
            break
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
    pathFound = []
    if exit:
        plot_path()
    else : 
        print("Path Not Found!!")

print("Eternal Loop")
while True:
    draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()