from Tkinter import *
import random
import time
import os


size = 15
w = 500
h = 500
temp = True
grid = []
stack = []
cols = int(w/size)
rows = int(h/size)
root = Tk()
canvas = Canvas(root, bg="black", height=h, width=w)
root.title("Maze Tracker")
canvas.pack()


def Index(i, j):
    if(i < 0 or j < 0 or i > cols-1 or j > rows - 1):
        return -1
    else:
        return i + (j*cols)


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]
        self.visited = False

    def show(self):
        x = self.i*size
        y = self.j*size
        if(self.walls[0]):
            canvas.create_line(x, y, x+size, y, fill='white', width=2)
        if(self.walls[1]):
            canvas.create_line(x+size, y, x+size, y+size, fill='white', width=2)
        if(self.walls[2]):
            canvas.create_line(x+size, y+size, x, y+size, fill='white', width=2)
        if(self.walls[3]):
            canvas.create_line(x, y+size, x, y, fill='white', width=2)
        if(self.visited == True):
            canvas.create_rectangle(x, y, x+size, y+size, width=0)

    def checkNeighbors(self, i, j):
        neighbors = []
        top_exists = True
        right_exists = True
        bottom_exists = True
        left_exists = True

        if(Index(i, j-1) != -1):
            top = grid[Index(i, j-1)]
        else:
            top_exists = False

        if(Index(i+1, j) != -1):
            right = grid[Index(i+1, j)]
        else:
            right_exists = False

        if(Index(i, j+1) != -1):
            bottom = grid[Index(i, j+1)]
        else:
            bottom_exists = False

        if(Index(i-1, j) != -1):
            left = grid[Index(i-1, j)]
        else:
            left_exists = False

        if(top_exists and top.visited == False):
            neighbors.append(top)
        if(right_exists and right.visited == False):
            neighbors.append(right)
        if(bottom_exists and bottom.visited == False):
            neighbors.append(bottom)
        if(left_exists and left.visited == False):
            neighbors.append(left)

        if (len(neighbors) > 0):
            randnum = int(random.randrange(0, len(neighbors)))
            return neighbors[randnum]
        else:
            return -1


# ------------------------------------------------------------------------------
def removeWalls(a, b):
    x = a.i - b.i
    if(x == 1):
        a.walls[3] = False
        b.walls[1] = False
    elif(x == -1):
        a.walls[1] = False
        b.walls[3] = False

    y = a.j - b.j
    if(y == 1):
        a.walls[0] = False
        b.walls[2] = False
    elif(y == -1):
        a.walls[2] = False
        b.walls[0] = False
# -------------------------------------------------------------------------------


for j in range(rows):
    for i in range(cols):
        cell = Cell(i, j)
        grid.append(cell)

current = grid[0]


while temp:
    canvas.delete("all")
    for i in range(len(grid)):
        grid[i].show()
    canvas.create_oval(5, 5, size-5, size-5, fill='green', width=0)
    canvas.create_oval(w-size+5, h-size+5, w-5, h-5, fill='red', width=0)
    current.visited = True
    next = current.checkNeighbors(current.i, current.j)
    if(next != -1):
        next.visited = True

        stack.append(current)
        removeWalls(current, next)

        current = next
    elif(len(stack) > 0):
        current = stack.pop()

    else:
        temp = False

    root.update()


mainloop()
