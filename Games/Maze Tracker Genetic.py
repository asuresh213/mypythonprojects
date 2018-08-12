from Tkinter import *
import random
import time
from copy import deepcopy
import os

# window Properties
w = 500
h = 500
root = Tk()
canvas = Canvas(root, bg="black", height=h, width=w)
root.title("Maze Tracker")
canvas.pack()

# grid Properties
size = 50
cols = int(w/size)
rows = int(h/size)
grid = []
stack = []

# bot Properties
path = []
count = 0
completed = False
bot_run = 0
bot_path = []
bot_path_collection = []
bot_score_collection = []
bot_population = []
new_bot_population = []
max_bot_population = 5


# -------------------------------------------------------------------------------


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]
        self.visited = False
        self.bot_visited = False

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


class Bot:
    def __init__(self):
        self.score = 0
        self.grid_pos = grid[0]
        self.bot_path = []

    def followpath(self):
        for dir in self.bot_path:
            if(dir == 'u'):
                self.grid_pos = grid[Index(self.grid_pos.i, self.grid_pos.j - 1)]
                self.grid_pos.bot_visited = True
            if(dir == 'r'):
                self.grid_pos = grid[Index(self.grid_pos.i+1, self.grid_pos.j)]
                self.grid_pos.bot_visited = True
            if(dir == 'b'):
                self.grid_pos = grid[Index(self.grid_pos.i, self.grid_pos.j + 1)]
                self.grid_pos.bot_visited = True
            if(dir == 'l'):
                self.grid_pos = grid[Index(self.grid_pos.i-1, self.grid_pos.j)]
                self.grid_pos.bot_visited = True

            print("Final grid position:", self.grid_pos.i, self.grid_pos.j)

    def move_direction(self, grid):
        neighbor = []
        if(Index(self.grid_pos.i, self.grid_pos.j - 1) != -1):
            neighbor.append('u')

        if(Index(self.grid_pos.i + 1, self.grid_pos.j) != -1):
            neighbor.append('r')

        if(Index(self.grid_pos.i, self.grid_pos.j + 1) != -1):
            neighbor.append('b')

        if(Index(self.grid_pos.i - 1, self.grid_pos.j) != -1):
            neighbor.append('l')

        rand = random.choice(neighbor)
        if(rand == 'u'):
            next_grid = grid[Index(self.grid_pos.i, self.grid_pos.j - 1)]
        elif(rand == 'r'):
            next_grid = grid[Index(self.grid_pos.i+1, self.grid_pos.j)]
        elif(rand == 'b'):
            next_grid = grid[Index(self.grid_pos.i, self.grid_pos.j + 1)]
        elif(rand == 'l'):
            next_grid = grid[Index(self.grid_pos.i-1, self.grid_pos.j)]

        return [next_grid, rand]


# --------------------------Grid Functions--------------------------------------
def Index(i, j):
    if(i < 0 or j < 0 or i > cols-1 or j > rows - 1):
        return -1
    else:
        return i + (j*cols)


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

# -----------------------------Bot Functions-------------------------------------


def show_bot(a, b):
    x1 = a*size
    y1 = b*size
    canvas.create_rectangle(int(x1 - 5 + size/2), int(y1 - 5 + size/2), int(x1 + 5 + size/2),
                            int(y1 + 5 + size/2), fill='white')
    print("rectangle created at:", x1, y1)


# def Drawbot(a1, b1, a2, b2, not_stuck, path):
    # if(not_stuck == True):
    #x1 = a1*size + (size/2)
    #y1 = b1*size + (size/2)
    #x2 = a2*size + (size/2)
    #y2 = b2*size + (size/2)
    #path.append(canvas.create_line(x1, y1, x2, y2, fill='green', width=2))
    # else:
    # canvas.delete(path)
    #path = []


def Check_for_walls(a, b, dir, bot_path):
    if(dir == 'u' and b.grid_pos.bot_visited == False):
        if(a.grid_pos.walls[0] == False and b.grid_pos.walls[2] == False):
            bot_path.append(dir)
            return True
        else:
            return False

    elif(dir == 'r'and b.grid_pos.bot_visited == False):
        if(a.grid_pos.walls[1] == False and b.grid_pos.walls[3] == False):
            bot_path.append(dir)
            return True
        else:
            return False

    elif(dir == 'b' and b.grid_pos.bot_visited == False):
        if(a.grid_pos.walls[2] == False and b.grid_pos.walls[0] == False):
            bot_path.append(dir)
            return True
        else:
            return False

    elif(dir == 'l' and b.grid_pos.bot_visited == False):
        if(a.grid_pos.walls[3] == False and b.grid_pos.walls[1] == False):
            bot_path.append(dir)
            return True
        else:
            return False

# ------------------------------------------------------------------------------


def mazecreate():

    temp = True
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
# -------------------------------------------------------------------------------


mazecreate()

# Creating the first population
for i in range(max_bot_population):
    bot_population.append(Bot())

while(completed == False):
    not_stuck = True
    for member in bot_population:
        if(len(member.bot_path) > 0):
            member.grid_pos.bot_visited = True
            better_path_len = int(0.80*len(member.bot_path))
            del(member.bot_path[better_path_len:])
            print("New path is", member.bot_path)
            member.followpath()

    # Gathering Data from each population
    for bot_number in range(max_bot_population):
        bot_population[bot_number].grid_pos.bot_visited = True
        if (completed == True):
            break
        print("bot number:", bot_number+1)
        bot_run = 0
        while bot_run < 500:
            if(len(bot_population[bot_number].bot_path) > 0):
                print("bot path array", bot_population[bot_number].bot_path)
                print("bot score:", bot_population[bot_number].score)
                # show_bot(next_bot.grid_pos.i, next_bot.grid_pos.j)
            data = bot_population[bot_number].move_direction(grid)
            next_bot = Bot()
            next_bot.grid_pos = data[0]
            dir = data[1]
            print("chosen Direction", dir)
            path_exists = Check_for_walls(
                bot_population[bot_number], next_bot, dir, bot_population[bot_number].bot_path)
            if(path_exists == True):
                count = 0
                next_bot.grid_pos.bot_visited = True
                bot_population[bot_number].grid_pos = next_bot.grid_pos
                bot_population[bot_number].score += 1
                # print(bot_stack)
                print("current bot position:",
                      bot_population[bot_number].grid_pos.i, bot_population[bot_number].grid_pos.j)
            else:
                count += 1
                if (count == 50):
                    not_stuck = False
                    print("bot stuck!")
                    for i in range(len(grid)):
                        grid[i].bot_visited = False
                    break

            if(bot_population[bot_number].grid_pos.i == cols - 1 and bot_population[bot_number].grid_pos.j == rows - 1):
                print("completed!")
                print("solution is:", bot_population[bot_number].bot_path)
                completed = True
                break

            print("bot try number", bot_run)
            bot_run += 1
        bot_score_collection.append(bot_population[bot_number].score)

    max_bot_score = max(bot_score_collection)

    for m in range(max_bot_population):
        if(bot_population[m].score >= 0.8*max_bot_score):
            bot_population[m].grid_pos.i = 0
            bot_population[m].grid_pos.j = 0
            new_bot_population.append(deepcopy(bot_population[m]))

    while(len(new_bot_population) < max_bot_population):
        rand_bot = random.choice(new_bot_population)
        clone_bot = deepcopy(rand_bot)
        clone_bot.grid_pos.i = 0
        clone_bot.grid_pos.j = 0
        new_bot_population.append(clone_bot)

    bot_population = deepcopy(new_bot_population)
    new_bot_population = []
    if(completed == False):
        for k in range(len(bot_population)):
            print("bot start pos and bot score:",
                  bot_population[k].grid_pos.i, bot_population[k].grid_pos.j, bot_population[k].score, bot_population[k].bot_path)


mainloop()
